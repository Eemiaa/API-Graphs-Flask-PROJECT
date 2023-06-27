
class Vertice():
    def __init__(self, antecessor="", d="", f="", cor ="", adj=[], tipo=int):
        self.antecessor = antecessor
        self.d = d
        self.f = f
        self.cor = cor
        self.adj = adj
        self.tipo = tipo
