
class Vertice():
    def __init__(self, antecessor=str, d=str, f=str, cor =str, adj=[]):
        self.antecessor = antecessor
        self.d = d
        self.f = f
        self.cor = cor
        self.adj = adj


    
def DFS_VISIT(arvore, u, tempo):
    arvore[u].cor = "C"
    tempo += 1
    arvore[u].d = tempo
    for v in arvore[u].adj:
        if arvore[v].cor ==  "B":
            arvore[v].antecessor = u
            DFS_VISIT(arvore, v, tempo)
    arvore[u].cor = "P"
    tempo += 1
    arvore[u].f = tempo