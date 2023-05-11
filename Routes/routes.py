from flask import jsonify, make_response, Blueprint, request
from Constructors.CRUDConstruct import Grafo
from Constructors.RepresentacaoConstruct import Representacoes
from Constructors.BuscaConstruct import Buscas

routes_bp = Blueprint('Routes',__name__)


@routes_bp.route('/grafo/adicionar', methods=['POST'])
def grafo_adicionar():
    entrada = request.get_json()

    vertices, arestas, nome = entrada['vertices'], entrada['arestas'], entrada['nome']
    grafos = Grafo(vertices,arestas, nome)

    return make_response(grafos.adicionar_grafo())
    
@routes_bp.route('/grafo/adicionar/aresta', methods=['POST'])
def grafo_adicionar_aresta():
    entrada = request.get_json()
    nome, a, b = entrada['nome'], entrada['a'], entrada['b']

    grafos = Grafo(nome=nome)
    return make_response(grafos.adicionar_aresta(a, b))




@routes_bp.route('/representacaoGrafos/listasAdjacencias', methods=['GET'])
def listas_adjacencias():
    entrada = request.get_json()

    nome = entrada['nome']
    grafo = Representacoes(nome=nome)
    return make_response(grafo.representacao_listas_adjacencias())
    
@routes_bp.route('/representacaoGrafos/matrizesAdjacencias', methods=['GET'])
def matrizes_adjacencias():
    entrada = request.get_json()

    nome = entrada['nome']
    grafo = Representacoes(nome=nome)
    return make_response(grafo.representacao_matrizes_adjacencias())
    
@routes_bp.route('/grafo/adjacentes/arestas', methods=['GET'])
def grafo_adjacentes_arestas():
    entrada = request.get_json()

    nome, a, b = entrada['nome'], entrada['a'], entrada['b']
    grafos = Representacoes(nome=nome)
    return make_response(grafos.grafo_aretas_adjacentes(a, b))

@routes_bp.route('/grafo/quantidade/vertices', methods=['GET'])
def grafo_quantidade_vertices():
    entrada = request.get_json()

    nome = entrada['nome']
    grafo = Representacoes(nome=nome)
    return make_response(grafo.grafo_numero_vertices())

@routes_bp.route('/grafo/quantidade/arestas', methods=['GET'])
def grafo_quantidade_arestas():
    entrada = request.get_json()

    nome = entrada['nome']
    grafo = Representacoes(nome=nome)
    return make_response(grafo.grafo_numero_arestas())

@routes_bp.route('/grafo/busca/DFS',methods=['GET'])
def dfs_alg():
    entrada = request.get_json()
    nome, inicial = entrada['nome'], entrada['inicial']
    grafo = Buscas(nome=nome)
    return make_response(grafo.DFS(inicial))

@routes_bp.route('/grafo/busca/BFS',methods=['GET'])
def bfs_alg():
    entrada = request.get_json()
    nome, inicial = entrada['nome'], entrada['inicial']
    grafo = Buscas(nome=nome)
    return make_response(grafo.BFS(inicial))








