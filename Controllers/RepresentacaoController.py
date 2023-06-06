import json
import os
import re
import pandas as pd
from Controllers.CRUDController import Grafo

class Representacoes():
    def __init__(self, nome=str):
        Grafo.__init__(self, nome=nome)

    def grafo_numero_vertices(self):

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

        vertice = re.sub("|\[|\]|'|\ ","", spamreader.vertices[numLinha]).split(",")

        return "Sucesso", len(vertice)

    def grafo_numero_arestas(self):

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

        aresta = re.sub("|\[|\]|\"|\ ","", spamreader.arestas[numLinha]).split(",")

        return "Sucesso", len(aresta)
    
    def representacao_matrizes_adjacencias(self):

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

        aresta = re.sub("|\[|\]|\"|\ ","", spamreader.arestas[numLinha]).split(",")
        vertice = re.sub("|\[|\]|'|\ ","", spamreader.vertices[numLinha]).split(",")

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

        return "Sucesso", matrizAdj
    
    def representacao_listas_adjacencias(self):

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

        return "Sucesso", listaAdj
    
    def grafo_aretas_adjacentes(self, a, b):

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

        if not aux: return "A aresta não existe!", None
        if len(arestasadjacentes) == 0: return "Não existe aresta adjacente à ela!", None
        
        return "Sucesso", arestasadjacentes
