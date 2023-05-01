from flask import jsonify
import csv
import os
import pandas as pd
import json

class Grafo():

    #Atributos
    def __init__(self, vertices= [], arestas= [], nome= ""):
        self.vertices = vertices
        self.arestas = arestas
        self.nome = nome

    #Métodos
    def adicionar_grafo(self):

        #manupilação no csv
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
        #manupilação no csv
        with open('db_grafos.csv','a', newline='', encoding='utf-8') as bd:

            if os.path.getsize('db_grafos.csv') == 0 : 
                return jsonify(mensagem = "O csv está vazio!")
            #pesquisa o nome do grafo
            aux = False
            cont = 0
            spamreader = pd.read_csv('db_grafos.csv')
            for coluna in spamreader.nome:
                if(self.nome == coluna):
                    aux = True
                    break
                cont+=1        
            if (aux == False): return jsonify(mensagem = "O grafo não existe!")

            #adicionar aresta
            #aresta = json.loads(spamreader.arestas[cont].replace("'","\""))
            aresta = spamreader.arestas[cont].replace("[","").replace("]","").split(",")

            aresta.append({a:b})
            spamreader.arestas[cont] = aresta

            #adicionar vertice

            vertice = spamreader.vertices[cont].replace("[","").replace("]","").replace("'","").replace(" ","").split(",")
            #print(vertice, a, b)
            if not(a in vertice): vertice.append(a)
            if not(b in vertice): vertice.append(b)
            spamreader.vertices[cont] = vertice


            spamreader.to_csv('db_grafos.csv', index=False)

            bd.close()

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
        if os.path.getsize('db_grafos.csv') == 0 : return jsonify(mensagem = "O csv está vazio!")
        #pesquisa o nome do grafo
        aux = False
        cont = 0
        spamreader = pd.read_csv('db_grafos.csv')
        for coluna in spamreader.nome:
            if(self.nome == coluna):
                aux = True
                break
            cont+=1        
        if (aux == False): return jsonify(mensagem = "O grafo não existe!")
        vertice = spamreader.vertices[cont].replace("[","").replace("]","").replace("'","").replace(" ","").split(",")

        return jsonify(numVertices=len(vertice))
    def grafo_numero_arestas(self):
        if os.path.getsize('db_grafos.csv') == 0 : return jsonify(mensagem = "O csv está vazio!")
        #pesquisa o nome do grafo
        aux = False
        cont = 0
        spamreader = pd.read_csv('db_grafos.csv')
        for coluna in spamreader.nome:
            if(self.nome == coluna):
                aux = True
                break
            cont+=1        
        if (aux == False): return jsonify(mensagem = "O grafo não existe!")
        aresta = spamreader.arestas[cont].replace("[","").replace("]","").split(",")
        return jsonify(numArestas=len(aresta))
    
    
        







        return jsonify(arestas = self.arestas, vertices = self.vertices)   
    
    def representacao_matrizes_adjacencias(self):
        return jsonify(arestas = self.arestas, vertices = self.vertices)
    def representacao_listas_adjacencias(self):

        if os.path.getsize('db_grafos.csv') == 0 : 
            return jsonify(mensagem = "O csv está vazio!")
        #pesquisa o nome do grafo
        aux = False
        cont = 0
        spamreader = pd.read_csv('db_grafos.csv')
        for coluna in spamreader.nome:
            if(self.nome == coluna):
                aux = True
                break
            cont+=1        
        if (aux == False): return jsonify(mensagem = "O grafo não existe!")
        arestas = spamreader.arestas[cont].replace("[","").replace("]","").replace("\"","").replace(" ","").split(",")
        vertice = spamreader.vertices[cont].replace("[","").replace("]","").replace("'","").replace(" ","").split(",")

        listaAdj = {}
        for i in vertice:
            listaAdj[i] = []

        for v in vertice:
            for a in vertice:
                if(a != v):
                    for i in arestas:

                        temp = json.loads(i.replace("'","\""))
                        
                        if str({v:a}).replace(" ","") == i or str({a:v}).replace(" ","") == i: 
                            listaAdj[v].append(a)


        return jsonify(listaAdjacencia = listaAdj)
    

    def grafo_aretas_adjacentes(self, a, b):
        if os.path.getsize('db_grafos.csv') == 0 : 
            return jsonify(mensagem = "O csv está vazio!")
        #pesquisa o nome do grafo
        aux = False
        cont = 0
        spamreader = pd.read_csv('db_grafos.csv')
        for coluna in spamreader.nome:
            if(self.nome == coluna):
                aux = True
                break
            cont+=1        
        if (aux == False): return jsonify(mensagem = "O grafo não existe!")

        #adicionar aresta
        aresta = spamreader.arestas[cont].replace("[","").replace("]","").replace("\"","").replace(" ","").split(",")

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

       
    