from flask import jsonify
import os
import pandas as pd
import re
import csv

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

        return "Grafo adicionado com sucesso!", [self.nome, self.vertices, self.arestas]
    
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


        return "Aresta adicionada com sucesso!"

    def adicionar_vertice(self):
        return jsonify(arestas = self.arestas, vertices = self.vertices)
    def remover_grafo(self):
        return jsonify(arestas = self.arestas, vertices = self.vertices)
    def remover_vertice(self):
        return jsonify(arestas = self.arestas, vertices = self.vertices)
    def remover_aresta(self):
        return jsonify(arestas = self.arestas, vertices = self.vertices)
    
    
    

    






    