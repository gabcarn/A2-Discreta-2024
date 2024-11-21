import numpy as np
from typing import Dict, Any, List

def greedy_coloring(graph: Dict[Any, Any],
                    vertices_order: List[Any] = None) -> Dict[Any, int]:
    """Colore um grafo G dado seguindo a ordem de vertices dada.

    Args:
        graph (Dict[Any, Any]): Dicionario que representa o grafo, onde as chaves sao vertices e os valores sao listas de vizinhos.
        vertices_order (List[Any], optional): Lista que representa a ordem em que os vertices devem ser coloridos. Defaults to None.

    Returns:
        Dict[Any, int]: Dicionario que representa a coloracao, onde as chaves sao os vertices do grafo dado e os valores sao as cores dos vertices.
    """
    
    # Inicializacao
    vertices = list(graph.keys())
    lenght = len(vertices)
    vertices_to_indices = {v: i for i, v in enumerate(vertices)}

    # Usar ordem original caso nao seja passado uma ordem
    if vertices_order == None:
        vertices_order = vertices

    colors = np.full(len(vertices), -1) # -1 = sem cor
    avaliable_colors = [True] * lenght

    for v in vertices_order:
        v_idx = vertices_to_indices[v]

        # Marca cores dos vertices adjacentes como indisponiveis
        for adj in graph[v]:
            adj_idx = vertices_to_indices[adj]
            if colors[adj_idx] != -1:
                avaliable_colors[colors[adj_idx]] = False

        # Atribui a primeira cor disponivel
        for color in range(lenght):
            if avaliable_colors[color]:
                colors[v_idx] = color
                break

        # Reseta o array de cores disponiveis
        for adj in graph[v]:
            adj_idx = vertices_to_indices[adj]
            if colors[adj_idx] != -1:
                avaliable_colors[colors[adj_idx]] = True

    return {v: colors[vertices_to_indices[v]] for v in vertices}