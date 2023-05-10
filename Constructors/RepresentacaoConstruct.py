import json
import os
import re
import pandas as pd
from flask import jsonify
from Constructors.CRUDConstruct import Grafo

class Representacoes():
    def __init__(self, nome=str):
        Grafo.__init__(self, nome=nome)

    def grafo_numero_vertices(self):

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

        vertice = re.sub("|\[|\]|'|\ ","", spamreader.vertices[numLinha]).split(",")

        return jsonify(quantidadeVertices = len(vertice))

    def grafo_numero_arestas(self):

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

        return jsonify(quantidadeArestas = len(aresta))
    
    def representacao_matrizes_adjacencias(self):

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

        print(aresta)
        dataAdj = []
        
        for l in vertice:
            auxcoluna = []
            for j in range(len(vertice)):
                auxcoluna.append(0)

            for c in range(len(vertice)):
                for i in aresta:

                    temp = json.loads(i.replace("'","\""))
                    if str({l:vertice[c]}).replace(" ","") == i: 
                        auxcoluna[c] = 1
            dataAdj.append(auxcoluna)

        matrizAdj = pd.DataFrame(dataAdj, index = vertice, columns = vertice)

        return jsonify( matrizAdjacencia = matrizAdj.to_json(orient="split"))
    
    def representacao_listas_adjacencias(self):

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

        listaAdj = {}
        for i in vertice:
            listaAdj[i] = []

        for v in vertice:
            for a in vertice:
                for i in aresta:

                    temp = json.loads(i.replace("'","\""))
                    
                    if str({v:a}).replace(" ","") == i or str({a:v}).replace(" ","") == i: 
                        listaAdj[v].append(a)

        return jsonify( listaAdjacencia = listaAdj)
    
    def grafo_aretas_adjacentes(self, a, b):

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

        #adicionar aresta
        aresta = re.sub("|\[|\]|\"|\ ","", spamreader.arestas[numLinha]).split(",")
        arestasadjacentes = []
        aux = False
        for i in aresta:
            
            if str({a:b}).replace(" ","") == i:
                aux = True
            temp = json.loads(i.replace("'","\""))
            
            if not(str({a:b}).replace(" ","") == i):
                if a == [*temp.values()][0] or b == [*temp.values()][0]:
                    arestasadjacentes.append(i)
                elif a == [*temp][0] or b == [*temp][0]:
                    arestasadjacentes.append(i)

        if not aux: return jsonify(mensagem = "A aresta não existe!")
        if len(arestasadjacentes) == 0: return jsonify(mensagem = "Não existe aresta adjacente à ela!")
        
        return jsonify(arestasAdjacentes = arestasadjacentes)
