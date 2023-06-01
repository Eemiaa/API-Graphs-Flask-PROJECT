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
        
    def iniciar_arvore(self, v_inicial=None):
        arvore = {}
        art1 = []
        art2 = []

        for art in self.arestas:
            aux = re.sub("|{|}|'","", art).split(":")
            art1.append(aux[0])
            art2.append(aux[1])
        
        if v_inicial is not None:
            for v in self.vertices:
                if v != v_inicial:
                    arvore[v] = Vertice(d=inf, antecessor=None, adj = [])
                else:
                    arvore[v] = Vertice(d=0, adj = [])

                for adjs in range(len(art1)):
                    if v == art1[adjs]:arvore[v].adj.append(art2[adjs])
        else:
            for v in self.vertices:
                arvore[v] = Vertice(adj = [], cor = "B")
            for adjs in range(len(art1)):
                if v == art1[adjs]:arvore[v].adj.append(art2[adjs])
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

    def matriz_peso(self, peso, aresta, vertice):

        dataAdj = []

        for l in vertice:
            auxcoluna = []
            for j in range(len(vertice)):
                auxcoluna.append(0)

            for c in range(len(vertice)):
                for i in aresta:

                    temp = json.loads(i.replace("'","\""))
                    if str({l:vertice[c]}).replace(" ","") == i: 
                        auxcoluna[c] = peso[str({l:vertice[c]}).replace(" ","")]
            dataAdj.append(auxcoluna)

        matrizAdj = pd.DataFrame(dataAdj, index = vertice, columns = vertice)

        return matrizAdj

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
    
    def Bellman_Ford(self, v_inicial, pesos):
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
        #algoritmo em si
        for i in range(1, len(self.vertices)):
            for arest in self.arestas:
                aux = re.sub("|{|}|'","", arest).split(":")
                arvore = self.relax(peso, arvore, aux[0], aux[1])

        resposta = {}
        for vrt in arvore.keys():
            resposta[vrt] = json.dumps(arvore[vrt].__dict__)

        for arest in self.arestas:
            aux = re.sub("|{|}|'","", arest).split(":") 
            if arvore[aux[1]].d > arvore[aux[0]].d + peso[str({aux[0]:aux[1]}).replace(" ","")]:
                return jsonify(arvore = resposta, msg = "Existe um ciclo negativo.")
    
        return jsonify(arvore = resposta, msg = "Não existe um ciclo negativo.")
    
    def Floyd_Warshall(self, pesos):

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
        
        #print(len(self.arestas))
        if len(pesos) != len(self.arestas):
            return jsonify(mensagem = "A quantidade de pesos não correspondem com a quantidade de arestas.")
        #inicia os pesos
        peso = self.iniciando_peso(pesos)

        #inicia a matriz de pesos
        matriz_peso = self.matriz_peso(peso, self.arestas, self.vertices)

        #algoritmo em si
        antecessores = {}
        for k in range(len(self.vertices)):
            for v in range(len(self.vertices)):
                for w in range(len(self.vertices)):

                    if matriz_peso.loc[self.vertices[v] , self.vertices[k]] + matriz_peso.loc[self.vertices[k], self.vertices[w]] < matriz_peso.loc[self.vertices[v], self.vertices[w]]:
                        matriz_peso.loc[self.vertices[v] , self.vertices[w]] = matriz_peso.loc[self.vertices[v], self.vertices[k]] + matriz_peso.loc[self.vertices[k], self.vertices[w]]
                        antecessores[self.vertices[v]] = self.vertices[k]

        return jsonify(matriz_peso = matriz_peso.to_json(orient="split"), lista_antecessores = antecessores)
        
    def Componentes_Conexos(self):

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

        componentes = {}
        arvore = self.iniciar_arvore()
        id = 0

        for i in self.vertices:
            if(arvore[i].cor == "B"):
                componentes[id] = []
                self.DFS(inicial=i, arvore = arvore, componentes=componentes[id])
        return jsonify(Componentes_Conectados = componentes )
                
    def DFS_VISIT(self, arvore, u, tempo, componentes):
        arvore[u].cor = "C"
        arvore[u].d = int(tempo)
        tempo += 1
        for v in arvore[u].adj:
            if arvore[v].cor == "B":
                print(arvore[v])
                arvore[v].antecessor = u
                tempo = self.DFS_VISIT(arvore, v, tempo)

        arvore[u].cor = "P"
        componentes.append(u)
        arvore[u].f = int(tempo)
        tempo += 1
        return tempo
    
    def DFS(self, inicial, arvore, componentes=[]):
        tempo = 0
        
        arvore[inicial].antecessor=None
        arvore[inicial].d=int(tempo)
        
        for u in self.vertices:
            if arvore[u].cor == "B":
                self.DFS_VISIT(arvore, u, tempo, componentes)
            
        resposta = {}
        for vrt in arvore.keys():
            resposta[vrt] = json.dumps(arvore[vrt].__dict__)

        
