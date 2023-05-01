from flask import jsonify
import csv
import os
import pandas as pd
import json

class Grafo():

    #Atributos
    def __init__(self, vertices= [], arestas= {}, nome= ""):
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

            #adicionar aresta
            aresta = json.loads(spamreader.arestas[cont].replace("'","\""))
            aresta[a] = b
            spamreader.arestas[cont] = aresta

            #adicionar vertice

            vertice = spamreader.vertices[cont].replace("[","").replace("]","").replace("'","").replace(" ","").split(",")
            print(vertice, a, b)
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