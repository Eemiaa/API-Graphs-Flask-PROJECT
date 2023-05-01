from Model.GrafoModel import Grafo


class Operacoes(Grafo):
    def __init__(self, teste):
        self.teste = teste
    
    def representacao_listas_adjacencias(self):
        return {self.vertices:self.arestas}
    
    def representacao_matrizes_adjacencias(self):
        return {self.vertices:self.arestas}
    
    def grafo_aretas_adjacentes(self):
        return {self.vertices:self.arestas}
    
    def grafo_vertices_adjacentes(self):
        return {self.vertices:self.arestas}