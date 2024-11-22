import numpy as np
from typing import Dict, Any, List

def get_vertices_degrees(graph: Dict[Any, Any]) -> Dict[Any, int]:
    """Encontra o grau de cada vértice de um dado grafo.

    Args:
        graph (Dict[Any, Any]): Dicionário que representa o grafo, onde as chaves são
                                vértices e os valores são listas de vizinhos.

    Returns:
        Dict[Any, int]: Dicionário onde as chaves são vértices do grafo dado e os valores
                        são os graus dos vértices.
    """

    vertices = list(graph.keys())
    return {v: len(graph[v]) for v in vertices}

def random_ordering(graph: Dict[Any, Any]) -> List[Any]:
    """Gera uma ordem aleatória dos vértices do grafo dado.

    Args:
        graph (Dict[Any, Any]): Dicionário que representa o grafo, onde as chaves são
                                vértices e os valores são listas de vizinhos.

    Returns:
        List[Any]: Lista que representa uma ordem aleatória dos vértices.
    """

    order = list(graph.keys())
    np.random.shuffle(order) # Embaralha a lista
    return order

def largest_first_ordering(graph: Dict[Any, Any]) -> List[Any]:
    """Implementa ordenação por maior-grau-primeiro dos vértices do grafo dado.

    Args:
        graph (Dict[Any, Any]): Dicionário que representa o grafo, onde as chaves são
                                vértices e os valores são listas de vizinhos.

    Returns:
        List[Any]: Lista que representa a ordenação por maior-grau-primeiro dos vértices
                do grafo dado.
    """

    vertices = list(graph.keys())
    degrees = get_vertices_degrees(graph)
    return sorted(vertices, key = lambda v: degrees[v], reverse = True) # Ordena decrescentemente

def smallest_last_ordering(graph: Dict[Any, Any]) -> List[Any]:
    """Implementa a ordenação menor-por-último dos vértices do grafo dado.

    Args:
        graph (Dict[Any, Any]): Dicionário que representa o grafo, onde as chaves são
                                vértices e os valores são listas de vizinhos.

    Returns:
        List[Any]: Lista que representa a ordenação menor-por-último dos vértices do
                grafo dado.
    """

    graph_copy = {v: list(adjs) for v, adjs in graph.items()}
    order = []
    degrees = {v: len(adjs) for v, adjs in graph_copy.items()}
    
    while degrees:
        # Encontra o vértice com menor grau atual
        min_vertex = min(degrees.items(), key=lambda x: x[1])[0]
        
        # Adiciona o vértice no início da ordem
        order.insert(0, min_vertex)
        
        # Remove o vértice do grafo e atualiza os graus
        adjs = graph_copy[min_vertex]
        del degrees[min_vertex]
        del graph_copy[min_vertex]
        
        # Atualiza os graus dos vizinhos
        for adj in adjs:
            if adj in degrees:  # Verifica se o vizinho ainda está no grafo
                graph_copy[adj].remove(min_vertex)
                degrees[adj] = len(graph_copy[adj])
    
    return order