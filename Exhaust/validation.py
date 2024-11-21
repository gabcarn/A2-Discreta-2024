import numpy as np

def check_coloring(G: dict, coloring: list) -> bool:
    """ Verifica se uma coloracao e valida, isto e, se para toda aresta e = (v, w) em E, f(v) != f(w).
    Args:
        G (dict): Grafo a ser analisado.
        coloring (list): Coloracao a ser checada.
    Returns:
        bool: True caso valida, False caso invalida.
    """
    V = G.keys()
    visited = np.zeros(len(V))
    # Passa por cada vertice nao visitado adjacente ao atual
    for each_vertex in V:
        for each_adjacent_vertex in G[each_vertex]:
            if not visited[each_adjacent_vertex]:
                # Alguma aresta liga dois vertices de mesma cor
                if coloring[each_adjacent_vertex] == coloring[each_vertex]:
                    return False
        visited[each_vertex] = 1
    return True