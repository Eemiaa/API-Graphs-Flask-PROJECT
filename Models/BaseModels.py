
class Vertice():
    def __init__(self, antecessor="", d="", f="", cor ="", adj=[]):
        self.antecessor = antecessor
        self.d = d
        self.f = f
        self.cor = cor
        self.adj = adj

#ele vai ter q fornecer o peso das arestas em ordem 