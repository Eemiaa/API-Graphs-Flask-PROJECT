import json
import os
import re
from flask import jsonify
import pandas as pd
from Constructors.CRUDConstruct import Grafo
from Models.BaseModels import Vertice

class Buscas():
    def __init__(self, nome=str):
        Grafo.__init__(self, nome=nome)
        
    def DFS_VISIT(self, arvore, u, tempo):
        arvore[u].cor = "C"
        arvore[u].d = int(tempo)
        tempo += 1
        for v in arvore[u].adj:
            if arvore[v].cor == "B":
                arvore[v].antecessor = u
                tempo = self.DFS_VISIT(arvore, v, tempo)

        arvore[u].cor = "P"
        arvore[u].f = int(tempo)
        tempo += 1
        return tempo
    
    def DFS(self, inicial):
        
        #verifica se o banco de dados está vazio:
        if os.path.getsize('db_grafos.csv') == 0 : return jsonify(mensagem = "O csv está vazio!")
        aux = False
        numLinha = 0
        #le o banco de dados
        spamreader = pd.read_csv('db_grafos.csv')
        #verifica se o grafo existe, a partir do nome
        for coluna in spamreader.nome:
            if(self.nome == coluna):
                aux = True
                break
            numLinha+=1        
        if (aux == False): return jsonify(mensagem = "O grafo não existe!")
        aresta = re.sub("|\[|\]|\"|\ ","", spamreader.arestas[numLinha]).split(",")
        vertice = re.sub("|\[|\]|'|\ ","", spamreader.vertices[numLinha]).split(",")
        if inicial not in vertice: return jsonify(mensagem = "Essa aresta não existe no mapa.")
        
        tempo = 0
        arvore = {}
        art1 = []
        art2 = []
        
        for art in aresta:
            aux = re.sub("|{|}|'","", art).split(":")
            art1.append(aux[0])
            art2.append(aux[1])

        for u in vertice:
            arvore[u] = Vertice(cor="B", adj = [])

            for adjs in range(len(art1)):
                if u == art1[adjs]: arvore[u].adj.append(art2[adjs])
                elif u == art2[adjs]: arvore[u].adj.append(art1[adjs])


        arvore[inicial].antecessor=None
        arvore[inicial].d=int(tempo)
        
        for u in vertice:
            if arvore[u].cor == "B":
                self.DFS_VISIT(arvore, u, tempo)
            
        resposta = {}
        for vrt in vertice:
            resposta[vrt] = json.dumps(arvore[vrt].__dict__)

        return jsonify( DFS = resposta)


