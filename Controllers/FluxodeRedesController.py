from math import inf
import math
import os
import re
import pandas as pd
from Controllers.BuscaController import Buscas
from Controllers.CRUDController import Grafo
from Controllers.RepresentacaoController import Representacoes
from Models.BaseModels import Vertice

class Redes():
    def __init__(self, nome=str):
        Grafo.__init__(self, nome=nome)

    def iniciando_peso(self, pesos):
        peso = {}     
        for i in range(len(self.arestas)):
            peso[self.arestas[i]] = pesos[i]
        return peso
    
    def iniciar_arvore(self, inicial=str):
        arvore = {}
        art1 = []
        art2 = []
        
        for art in self.arestas:
            aux = re.sub("|{|}|'","", art).split(":")
            art1.append(aux[0])
            art2.append(aux[1])

        for u in self.vertices:
            if u != inicial:
                arvore[u] = Vertice(cor="B", adj = [], d = math.inf, antecessor=None)
            else:
                arvore[u] = Vertice(cor="C", adj = [], d = 0, antecessor=None)
            for adjs in range(len(art1)):
                if u == art1[adjs]: arvore[u].adj.append(art2[adjs])
                
        return arvore

    def BFS(self, inicial, sink, pesos, arvore):
        tempo = 0
        Q = []
        Q.append(inicial)
        
        while len(Q) != 0:
            u = Q[0]
            Q.pop(0)
            for v in arvore[u].adj:
                if arvore[v].cor == 'B' and pesos[str({u:v}).replace(" ","")] > 0:
                    Q.append(v)
                    arvore[v].cor = 'C'
                    arvore[v].d = arvore[u].d + 1
                    arvore[v].antecessor = u
                    if v == sink:
                        return True
            arvore[u].cor = 'P'

        return False
    

    def FordFulkerson(self, inicial, sink, pesos):
        #verifica se o banco de dados está vazio:
        if os.path.getsize('db_grafos.csv') == 0 : return "O csv está vazio!", None
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
        if (aux == False): return "O grafo não existe!", None
        self.arestas = re.sub("|\[|\]|\"|\ ","", spamreader.arestas[numLinha]).split(",")
        self.vertices = re.sub("|\[|\]|'|\ ","", spamreader.vertices[numLinha]).split(",")
        if inicial not in self.vertices: return "Essa aresta não existe no mapa.", None

        #inicia os pesos
        if len(pesos) != len(self.arestas):
            return "A quantidade de pesos não correspondem com a quantidade de arestas.", None
        peso = self.iniciando_peso(pesos)
        #inicia a arvore
        arvore = arvore = self.iniciar_arvore(inicial=inicial)

        representacoes = Representacoes(nome=self.nome)
        msg, qtd_vertice = representacoes.grafo_numero_vertices()

        max_fluxo = 0

        while self.BFS(inicial=inicial, sink=sink, pesos=peso, arvore=arvore):
            fluxo_caminho = math.inf
            s = sink
            while s != inicial:
                if str({arvore[s].antecessor:s}).replace(" ","") in self.arestas: fluxo_caminho = min(fluxo_caminho, peso[str({arvore[s].antecessor:s}).replace(" ","")])
                s = arvore[s].antecessor
            
            max_fluxo += fluxo_caminho

            v = sink

            while v != inicial:
                u = arvore[v].antecessor
                if str({u:v}).replace(" ","") in self.arestas: peso[str({u:v}).replace(" ","")] -= fluxo_caminho
                if str({v:u}).replace(" ","") in self.arestas: peso[str({v:u}).replace(" ","")] -= fluxo_caminho
                v = arvore[v].antecessor
        return 'ok', max_fluxo
