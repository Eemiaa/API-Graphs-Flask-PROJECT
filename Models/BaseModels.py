
class Vertice():
    def __init__(self, antecessor=str, d=str, f=str, cor =str, adj=[]):
        self.antecessor = antecessor
        self.d = d
        self.f = f
        self.cor = cor
        self.adj = adj


    
def DFS_VISIT(arvore, u, tempo):
    arvore[u].cor = "C"
    arvore[u].d = int(tempo)
    tempo += 1
    for v in arvore[u].adj:
        if arvore[v].cor == "B":
            arvore[v].antecessor = u
            tempo = DFS_VISIT(arvore, v, tempo)

    arvore[u].cor = "P"
    arvore[u].f = int(tempo)
    tempo += 1
    return tempo