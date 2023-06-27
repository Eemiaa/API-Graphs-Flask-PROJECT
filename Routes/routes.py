from Controllers.FluxodeRedesController import Redes
from flask import jsonify, make_response, Blueprint, request
from Controllers.CRUDController import Grafo
from Controllers.CaminhosController import Caminhos
from Controllers.RepresentacaoController import Representacoes
from Controllers.BuscaController import Buscas

routes_bp = Blueprint('Routes',__name__)

#ok
@routes_bp.route('/grafo/adicionar', methods=['POST'])
def grafo_adicionar():
    entrada = request.get_json()
    vertices, arestas, nome = entrada['vertices'], entrada['arestas'], entrada['nome']
    grafos = Grafo(vertices,arestas, nome)

    msg, grafo = grafos.adicionar_grafo()

    return make_response(jsonify(mensagem = msg, grafo =grafo))

#ok  
@routes_bp.route('/grafo/adicionar/aresta', methods=['POST'])
def grafo_adicionar_aresta():
    entrada = request.get_json()
    nome, a, b = entrada['nome'], entrada['a'], entrada['b']
    grafos = Grafo(nome=nome)
    
    msg, resposta = grafos.adicionar_aresta(a, b)
    
    return make_response(jsonify(mensagem = msg))

#ok
@routes_bp.route('/representacaoGrafos/listasAdjacencias', methods=['GET'])
def listas_adjacencias():
    entrada = request.get_json()
    nome = entrada['nome']
    grafos = Representacoes(nome=nome)

    msg, listaAdj = grafos.representacao_listas_adjacencias()

    return make_response(jsonify(mensagem = msg, lista_adjacencia = listaAdj))

#ok    
@routes_bp.route('/representacaoGrafos/matrizesAdjacencias', methods=['GET'])
def matrizes_adjacencias():
    entrada = request.get_json()
    nome = entrada['nome']
    grafo = Representacoes(nome=nome)

    msg, matrizAdj = grafo.representacao_matrizes_adjacencias()

    return make_response(jsonify(mensagem = msg, matriz_adjacencia = matrizAdj.to_json(orient="split")))

#ok    
@routes_bp.route('/grafo/adjacentes/arestas', methods=['GET'])
def grafo_adjacentes_arestas():
    entrada = request.get_json()
    nome, a, b = entrada['nome'], entrada['a'], entrada['b']
    grafos = Representacoes(nome=nome)

    msg, arestasAdj = grafos.grafo_aretas_adjacentes(a, b)

    return make_response(jsonify(mensagem = msg, arestas_adjacentes = arestasAdj))

#ok
@routes_bp.route('/grafo/quantidade/vertices', methods=['GET'])
def grafo_quantidade_vertices():
    entrada = request.get_json()
    nome = entrada['nome']
    grafo = Representacoes(nome=nome)

    msg, qtd_vertice = grafo.grafo_numero_vertices()

    return make_response(jsonify(mensagem = msg, quantidade_vertices = qtd_vertice))

#ok
@routes_bp.route('/grafo/quantidade/arestas', methods=['GET'])
def grafo_quantidade_arestas():
    entrada = request.get_json()
    nome = entrada['nome']
    grafo = Representacoes(nome=nome)

    msg, qtdVertices = grafo.grafo_numero_arestas()

    return make_response(jsonify(mensagem = msg, quantidadeVertices = qtdVertices))

#ok
@routes_bp.route('/grafo/busca/DFS',methods=['GET'])
def dfs_alg():
    entrada = request.get_json()
    nome, inicial = entrada['nome'], entrada['inicial']
    grafo = Buscas(nome=nome)
    
    msg, response = grafo.DFS(inicial)

    return make_response(jsonify(mensagem = msg, resposta = response[0]))

#ok
@routes_bp.route('/grafo/busca/BFS',methods=['GET'])
def bfs_alg():
    entrada = request.get_json()
    nome, inicial = entrada['nome'], entrada['inicial']
    grafo = Buscas(nome=nome)

    msg, resposta = grafo.BFS(inicial)

    return make_response(jsonify(mensagem = msg, resposta = resposta))


#ok
@routes_bp.route('/grafo/caminhos/Dijkstra',methods=['GET'])
def dijkstra_alg():
    entrada = request.get_json()
    nome, inicial,pesos = entrada['nome'], entrada['inicial'], entrada['pesos']
    grafo = Caminhos(nome=nome)
    
    msg, resposta = grafo.Dijkstra(inicial, pesos)

    return make_response(jsonify(mensagem = msg, S = resposta[0], arvore = resposta[1]))

#ok
@routes_bp.route('/grafo/caminhos/Bellman_Ford',methods=['GET'])
def bellman_ford_alg():
    entrada = request.get_json()
    nome, inicial, pesos = entrada['nome'], entrada['inicial'], entrada['pesos']
    grafo = Caminhos(nome=nome)

    msg, resposta = grafo.Bellman_Ford(inicial, pesos)

    return make_response(jsonify(mensagem = msg, resposta = resposta))

#ok
@routes_bp.route('/grafo/caminhos/Floyd_Warshall',methods=['GET'])
def floyd_warshall_alg():
    entrada = request.get_json()
    nome, pesos= entrada['nome'], entrada['pesos']
    grafo = Caminhos(nome=nome)

    msg, resposta = grafo.Floyd_Warshall(pesos)

    return make_response(jsonify(mensagem = msg, matriz_peso = resposta[0].to_json(orient="split"), lista_antecessores = resposta[1]))

#ok
@routes_bp.route('/grafo/caminhos/Componentes_Conexos',methods=['GET'])
def componentes_conexos_alg():
    entrada = request.get_json()
    nome = entrada['nome']
    grafo = Caminhos(nome=nome)

    msg, componentes = grafo.Componentes_Conexos()

    return make_response(jsonify(mensagem = msg, componentes_conectados = componentes ))

#ok
@routes_bp.route('/grafo/caminhos/Warshall',methods=['GET'])
def warshall_alg():
    entrada = request.get_json()
    nome = entrada['nome']
    grafo = Caminhos(nome=nome)

    msg, fecho = grafo.Warshall()

    return make_response(jsonify(mensagem = msg, matriz_fecho_transitivo = fecho.to_json(orient="split") ))

@routes_bp.route('/grafo/redes/FordFulkerson',methods=['GET'])
def fordfulkerson_alg():
    entrada = request.get_json()
    nome, inicial, sink, pesos = entrada['nome'], entrada['inicial'], entrada['sink'], entrada['pesos']
    grafo = Redes(nome=nome)

    msg, resposta = grafo.FordFulkerson(inicial=inicial, sink=sink, pesos=pesos)

    return make_response(jsonify(mensagem = msg, fluxo_maximo = resposta ))

