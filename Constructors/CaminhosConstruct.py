import json
import os
import re
import pandas as pd
import heapq
from heapq import heapify, heappop
from flask import jsonify
from Constructors.CRUDConstruct import Grafo
from Models.BaseModels import Vertice
from math import inf


class Caminhos():
    
    def __init__(self, nome=str):
        Grafo.__init__(self, nome=nome)
        
    
    def iniciar_arvore(self, v_inicial):
        arvore = {}
        art1 = []
        art2 = []

        for art in self.arestas:
            aux = re.sub("|{|}|'","", art).split(":")
            art1.append(aux[0])
            art2.append(aux[1])
        
        print(self.vertices)
        for v in self.vertices:
            if v != v_inicial:
                arvore[v] = Vertice(d=inf, antecessor=None, adj = [])
            else:
                arvore[v] = Vertice(d=0, adj = [])

            for adjs in range(len(art1)):
                if v == art1[adjs]:arvore[v].adj.append(art2[adjs]), print(v, arvore[v].adj)
        
        return arvore

    def relax(sef, peso, arvore, v_meio, v_final):

        if arvore[v_final].d > arvore[v_meio].d + peso[str({v_meio:v_final}).replace(" ","")]:
            arvore[v_final].d = arvore[v_meio].d + peso[str({v_meio:v_final}).replace(" ","")]
            arvore[v_final].antecessor = v_meio
        return arvore

    def iniciando_peso(self, pesos):
        peso = {}     
        for i in range(len(self.arestas)):
            peso[self.arestas[i]] = pesos[i]
        return peso

    def Dijkstra(self, v_inicial, pesos):
        
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
        self.arestas = re.sub("|\[|\]|\"|\ ","", spamreader.arestas[numLinha]).split(",")
        self.vertices = re.sub("|\[|\]|'|\ ","", spamreader.vertices[numLinha]).split(",")
        
        #inicia os pesos
        if len(pesos) != len(self.arestas):
            return jsonify(mensagem = "A quantidade de pesos não correspondem com a quantidade de arestas.")
        peso = self.iniciando_peso(pesos)
        #inicia a arvore
        arvore = self.iniciar_arvore(v_inicial)
        #algoritmo de fato
        S = []
        Q = self.vertices.copy()
        heapify(Q)

        while len(Q) != 0:
            u = heappop(Q)
            S.append(u)
            for v in arvore[u].adj:
                arvore = self.relax(peso, arvore, u, v)
        resposta = {}
        for vrt in arvore.keys():
            resposta[vrt] = json.dumps(arvore[vrt].__dict__)
        
        return jsonify( S = S, arvore = resposta)
    
    def Bellman_Ford(self):
        return jsonify(msg = 'ok')
    
    def Floyd_Warshall(self):
        return jsonify(msg = 'ok')
    
    def Componentes_Conexos(self):
        return jsonify(msg = 'ok')