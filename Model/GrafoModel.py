from flask import jsonify
class Grafo():
    #Atributos
    def __init__(self, vertices: list, arestas: dict):
        self.vertices = vertices
        self.arestas = arestas
    #Métodos
    def adicionar_grafo(self):
        return jsonify(arestas = self.arestas, vertices = self.vertices)
    def adicionar_aresta(self):
        return {self.vertices:self.arestas}
    def adicionar_vertice(self):
        return {self.vertices:self.arestas}
    
    
    def remover_grafo(self):
        return {self.vertices:self.arestas}
    def remover_vertice(self):
        return {self.vertices:self.arestas}
    def remover_aresta(self):
        return {self.vertices:self.arestas}