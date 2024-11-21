def contract_edge(graph, u, v):
	"""Contrai uma aresta no grafo, unindo os vertices u e v em um unico vertice.

	Args:
		graph (dict): O grafo, representado como um dicionario de vertices e seus vizinhos.
		u (int): O primeiro vertice da aresta.
		v (int): O segundo vertice da aresta.

	Returns:
		dict: Um novo grafo, obtido apos a contracao da aresta.
	"""
	contracted_graph = {}
	for vertex, neighbors in graph.items():
		if vertex != v:
			contracted_graph[vertex] = [neighbor for neighbor in neighbors if neighbor != v]

	for neighbor in graph[v]:
		if neighbor != u:
			contracted_graph[u].append(neighbor)
			contracted_graph[neighbor].append(u)
		contracted_graph[neighbor] = list(set(contracted_graph[neighbor]))
		
	contracted_graph[u] = list(set(contracted_graph[u]))

	return contracted_graph