from flask import jsonify
import csv
import os
import pandas as pd

class Grafo():

    #Atributos
    def __init__(self, vertices: list, arestas: dict, nome: str):
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
    
    def adicionar_aresta(self):
        return jsonify(arestas = self.arestas, vertices = self.vertices)
    def adicionar_vertice(self):
        return jsonify(arestas = self.arestas, vertices = self.vertices)
    
    
    def remover_grafo(self):
        return jsonify(arestas = self.arestas, vertices = self.vertices)
    def remover_vertice(self):
        return jsonify(arestas = self.arestas, vertices = self.vertices)
    def remover_aresta(self):
        return jsonify(arestas = self.arestas, vertices = self.vertices)