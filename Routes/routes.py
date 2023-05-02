from flask import make_response, Blueprint, request
from Model.GrafoModel import Grafo

routes_bp = Blueprint('Routes',__name__)


@routes_bp.route('/grafo/adicionar', methods=['POST'])
def grafo_adicionar():
    #return make_response(jsonify(b = entrada['b']))
    #vertices, arestas, nome = request.form.get('vertices','arestas','nome')
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

@routes_bp.route('/grafo/adicionar/vertice', methods=['POST'])
def grafo_adicionar_vertice():
    grafos = Grafo(['a','b'],{'a':'b'})
    return make_response(grafos.adicionar_vertice())

@routes_bp.route('/grafo/remover', methods=['POST'])
def grafo_remover():
    grafos = Grafo(['a','b'],{'a':'b'})
    return make_response(grafos.remover_grafo())

@routes_bp.route('/grafo/remover/vertice', methods=['POST'])
def grafo_remover_vertice():
    grafos = Grafo(['a','b'],{'a':'b'})
    return make_response(grafos.remover_vertice())

@routes_bp.route('/grafo/remover/aresta', methods=['POST'])
def grafo_remover_aresta():
    grafos = Grafo(['a','b'],{'a':'b'})
    return make_response(grafos.remover_aresta())


@routes_bp.route('/representacaoGrafos/listasAdjacencias', methods=['GET'])
def listas_adjacencias():
    entrada = request.get_json()

    nome = entrada['nome']
    grafo = Grafo(nome=nome)
    return make_response(grafo.representacao_listas_adjacencias())
    
@routes_bp.route('/representacaoGrafos/matrizesAdjacencias', methods=['GET'])
def matrizes_adjacencias():
    entrada = request.get_json()

    nome = entrada['nome']
    grafo = Grafo(nome=nome)
    return make_response(grafo.representacao_matrizes_adjacencias())
    

@routes_bp.route('/grafo/adjacentes/arestas', methods=['GET'])
def grafo_adjacentes_arestas():
    entrada = request.get_json()

    nome, a, b = entrada['nome'], entrada['a'], entrada['b']
    grafos = Grafo(nome=nome)
    return make_response(grafos.grafo_aretas_adjacentes(a, b))


@routes_bp.route('/grafo/adjacentes/vertices', methods=['GET'])
def grafo_adjacentes_vertices():
    return make_response(
        {"Hello":"world"}
    )

@routes_bp.route('/grafo/quantidade/vertices', methods=['GET'])
def grafo_quantidade_vertices():
    entrada = request.get_json()

    nome = entrada['nome']
    grafo = Grafo(nome=nome)
    return make_response(grafo.grafo_numero_vertices())

@routes_bp.route('/grafo/quantidade/arestas', methods=['GET'])
def grafo_quantidade_arestas():
    entrada = request.get_json()

    nome = entrada['nome']
    grafo = Grafo(nome=nome)
    return make_response(grafo.grafo_numero_arestas())
    










