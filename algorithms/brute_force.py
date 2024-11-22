import numpy as np
from utils.validation import check_coloring

def exhaustive_search(G: dict, q: int, coloring: list) -> list:
    """ Algoritmo para encontrar uma q-coloracao para o grafo G, caso exista.
    Args:
        G (dict): Grafo na estrutura de lista de adjacencias, representado por um dicionario
        q (int): Quantidade de cores da coloracao desejada
        coloring (list): Coloracao ate a presente chamada recursiva
    Returns:
        list: q-coloracao encontrada, [] caso nao exista
    """
    V = G.keys()
    # Caso seja uma coloracao sobrejetiva, verifica se ela e valida
    if len(V) == len(coloring):
        # A coloracao completa deve ter q cores (*)
        if len(set(coloring)) < q:
            return []
        # Verifica se a a coloracao satisfaz a definicao
        if check_coloring(G, coloring):
            return coloring
        return []
    else:
        # Preenche a coloracao ate que ela seja sobrejetiva
        for each_color in range(q):
            next_vertex_coloring = coloring.copy()
            next_vertex_coloring.append(each_color)
            
            # Caso uma das proximas coloracoes seja uma q-coloracao valida, repassa-a para a chamada que a chamou
            next_vertex_coloring = exhaustive_search(G, q, next_vertex_coloring)
            
            if next_vertex_coloring != []:
                return next_vertex_coloring
        return []