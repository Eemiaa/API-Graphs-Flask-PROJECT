from flask import jsonify
import os
import pandas as pd
import json
import re
import csv
from Models.BaseModels import Vertice, DFS_VISIT

class Grafo():

    #Atributos
    def __init__(self, vertices= [], arestas= [], nome= ""):
        self.vertices = vertices
        self.arestas = arestas
        self.nome = nome
        
    #Métodos
    def adicionar_grafo(self):
        #verifica se o banco de dados está vazio:
        with open('db_grafos.csv','a', newline='', encoding='utf-8') as bd:
            
            #objeto de gravação
            spamwriter = csv.writer(bd, delimiter=',')
            if os.path.getsize('db_grafos.csv') != 0 :
                spamreader = pd.read_csv('db_grafos.csv')
                print(spamreader)
                for coluna in spamreader.nome:
                    if(self.nome == coluna):
                       return jsonify(mensagem = "O grafo já existe!")
            else:
                spamwriter.writerow(["nome", "vertices", "arestas"])
            #gravando
            spamwriter.writerow([self.nome, self.vertices, self.arestas])
            bd.close()

        return jsonify(mensagem = "Grafo adicionado com sucesso!", 
                       grafo = [self.nome, self.vertices, self.arestas])
    
    def adicionar_aresta(self, a, b):

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

        #pega a lista de aresta correta e trata os dados
        aresta = re.sub("|\[|\]|\"|\ ","", spamreader.arestas[numLinha]).split(",")
        #adiciona a nova aresta na lista
        aresta.append(str({a:b}).replace(" ",""))
        #adiciona a nova lista na tabela
        spamreader.arestas[numLinha] = aresta
        

        #pega a lista de vertice correta e trata os dados
        vertice = re.sub("|\[|\]|'|\ ","", spamreader.vertices[numLinha]).split(",")
        #adiciona os vértices caso eles não existam
        if not(a in vertice): vertice.append(a)
        if not(b in vertice): vertice.append(b)       
        #adiciona a nova lista na tabela
        spamreader.vertices[numLinha] = vertice
        #confirma as alterações
        spamreader.to_csv('db_grafos.csv', index=False)


        return jsonify(mensagem = "Aresta adicionada com sucesso!")

    def adicionar_vertice(self):
        return jsonify(arestas = self.arestas, vertices = self.vertices)
    
    
    def remover_grafo(self):
        return jsonify(arestas = self.arestas, vertices = self.vertices)
    def remover_vertice(self):
        return jsonify(arestas = self.arestas, vertices = self.vertices)
    def remover_aresta(self):
        return jsonify(arestas = self.arestas, vertices = self.vertices)
    
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

        return jsonify(numVertices=len(vertice))

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

        return jsonify(numArestas=len(aresta))
    
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

        return jsonify(matrizAdjacência = matrizAdj.to_json(orient="split"))
    
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

        return jsonify(listaAdjacencia = listaAdj)
    
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
        return jsonify(ArestasAdj = arestasadjacentes)

    def grafo_vertices_adjacentes(self):
        return jsonify(arestas = self.arestas, vertices = self.vertices)
    

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
        arvore[inicial].d=tempo
        
        for u in vertice:
            if arvore[u].cor == "B":
                DFS_VISIT(arvore, u, tempo)

        resposta = {}
        for vrt in vertice:
            resposta[vrt] = json.dumps(arvore[vrt].__dict__)

        return resposta







    