import copy

def delete_edge(graph, u, v):
	"""Deleta uma aresta do grafo.

	Args:
		graph (dict): O grafo, representado como um dicionario de vertices e seus vizinhos.
		u (int): O primeiro vertice da aresta.
		v (int): O segundo vertice da aresta.

	Returns:
		dict: Um novo grafo, obtido apos a remocao da aresta.
	"""
	
	graph_without_edge = copy.deepcopy(graph)

	if v in graph_without_edge[u]:
		graph_without_edge[u].remove(v)
	if u in graph_without_edge[v]:
		graph_without_edge[v].remove(u)

	return graph_without_edge