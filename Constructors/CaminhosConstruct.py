import os
import re
from turtle import pd
from flask import jsonify
from Constructors.CRUDConstruct import Grafo
from Models.BaseModels import Vertice
from math import inf

class Caminhos():
    
    def __init__(self, nome=str):
        Grafo.__init__(self, nome=nome)
        

    def initialize_Single_Source(self, v_inicial):
        arvore = {}
        for v in self.Grafo.vertices:
            if v != v_inicial:
                arvore[v_inicial] = Vertice(d=inf, antecessor=None)
            else:
                arvore[v_inicial] = Vertice(d=0)
        return arvore

    def relax(peso, arvore, v_meio, v_final):
        if arvore[v_final].d > arvore[v_meio].d + peso[str({v_meio:v_final}).replace(" ","")]:
            arvore[v_final].d = arvore[v_meio] + peso[str({v_meio:v_final}).replace(" ","")]
            arvore[v_final].antecessor = v_meio
        return arvore

    def iniciando_peso(self, pesos):
        peso = {}     
        for i in range(len(self.arestas)):
            peso[self.arestas[i]] = pesos[i]
        return peso

    def Dijkstra(self, v_inicial, pesos, tipo):

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
        self.aresta = re.sub("|\[|\]|\"|\ ","", spamreader.arestas[numLinha]).split(",")

        if len(pesos) != len(self.arestas):
            return jsonify(mensagem = "A quantidade de pesos não correspondem com a quantidade de arestas.")
        peso = self.iniciando_peso(pesos)


        return jsonify( peso = peso)

    def Bellman_Ford(self):
        print('ok')
    
    def Floyd_Warshall(self):
        print('ok')
    
    def Componentes_Conexos(self):
        print('ok')