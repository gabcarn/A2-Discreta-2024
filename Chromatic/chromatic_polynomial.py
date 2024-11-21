import copy
import numpy as np
from contraction import contract_edge
from deletion import delete_edge

def chromatic_polynomial(graph, vertex, original_graph=None):
    """Calcula os coeficientes do polinomio cromatico de um grafo usando o metodo de contracao-delecao.
    Args:
        graph (dict): O grafo, representado como um dicionario de vertices e seus vizinhos.
    Returns:
        list: Uma lista contendo os coeficientes do polinomio cromatico.
    """

    def is_empty(graph):
        """Verifica se o grafo e vazio, ou seja, se nao possui arestas.
        Args:
            graph (dict): O grafo, representado como um dicionario de vertices e seus vizinhos.
        Returns:
            bool: Retorna True se o grafo nao possui arestas. Caso contrario, retorna False.
        """
        return all(len(adj) == 0 for adj in graph.values())

    if original_graph is None:
        original_graph = copy.deepcopy(graph)

    n = len(graph)

    if is_empty(graph):
        coefficients = np.append(np.zeros(n), 1)
        coefficients = np.append(coefficients, [0]*(vertex-n))
        return coefficients
    
    u, v = next((u, v) for u, neighbors in graph.items() for v in neighbors)
    
    contracted_graph = contract_edge(graph, u, v)
    contracted_poly = chromatic_polynomial(contracted_graph, vertex, original_graph)

    deleted_graph = delete_edge(graph, u, v)
    deleted_poly = chromatic_polynomial(deleted_graph, vertex, original_graph)
    

    coefficients = deleted_poly - contracted_poly
    return coefficients