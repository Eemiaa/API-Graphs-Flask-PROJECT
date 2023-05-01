from flask import make_response, Blueprint, request, jsonify
from Model.GrafoModel import Grafo
from Model.OperacoesModel import Operacoes

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
    grafos = Grafo(['a','b'],{'a':'b'})
    return make_response(grafos.adicionar_aresta())

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
    return make_response(
        {"Hello":"world"}
    )
@routes_bp.route('/representacaoGrafos/matrizesAdjacencias', methods=['GET'])
def matrizes_adjacencias():
    return make_response(
        {"Hello":"world"}
    )

@routes_bp.route('/grafo/adjacentes/arestas', methods=['GET'])
def grafo_adjacentes_arestas():
    return make_response(
        {"Hello":"world"}
    )
@routes_bp.route('/grafo/adjacentes/vertices', methods=['GET'])
def grafo_adjacentes_vertices():
    return make_response(
        {"Hello":"world"}
    )










