from flask import jsonify
from Model.GrafoModel import Grafo

class Operacoes(Grafo):
    #Atributos
    def __init__(self, teste):
        self.teste = teste
        
    #Métodos
    def representacao_listas_adjacencias(self):
        return jsonify(arestas = self.arestas, vertices = self.vertices)
    
    def representacao_matrizes_adjacencias(self):
        return jsonify(arestas = self.arestas, vertices = self.vertices)
    
    def grafo_aretas_adjacentes(self):
        return jsonify(arestas = self.arestas, vertices = self.vertices)
    
    def grafo_vertices_adjacentes(self):
        return jsonify(arestas = self.arestas, vertices = self.vertices)