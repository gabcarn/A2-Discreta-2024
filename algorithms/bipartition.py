from typing import Dict, Any, Union, Tuple, List
from collections import deque

import sys
sys.path.append('../utils')
from cycle import build_odd_cycle, find_closest_ancestor

def bipartition(graph: Dict[Any, Any]) -> Union[Tuple[bool, Dict[Any, Any]], Tuple[bool, List]]:
    """Verificar se um grafo conexo e bipartido. Se for, retorna uma 2-coloracao. Caso
    contrario, retorna um ciclo impar.

    Args:
        graph (Dict[Any, Any]): Dicionario que representa o grafo, onde as chaves sao vertices e os valores sao listas de vizinhos.

    Returns:
        Union[Tuple[bool, Dict[Any, Any]], Tuple[bool, List]]: Tupla (True, coloration) se o grafo for bipartido, onde coloration e a 2-coloracao. Ou (False, odd_cycle) se o grafo nao for bipartido, onde odd_cycle e o ciclo impar.
    """  
    # Inicializacao
    coloration = {}  # Armazena as cores (1 ou 2) dos vertices
    parents = {}  # Armazena o "pai" de cada vertice
    queue = deque() # Fila para realizar BFS

    # Inicializa a BFS
    start = next(iter(graph))
    coloration[start] = 1 # Atribui a cor 1 ao vertice inicial
    queue.append(start)

    # Realiza a BFS para verificar biparticao
    while queue:
        v = queue.popleft() # Remove o vertice atual da fila
        for w in graph[v]:
            if w not in coloration: # Se w ainda nao foi visitado
                coloration[w] = 3 - coloration[v] # Atribui cor oposta a de v
                parents[w] = v # Define v como "pai" de w
                queue.append(w) # Adiciona w a fila
            elif coloration[w] == coloration[v]: # Se w ja foi visitado e tem mesma cor que v
    
    # Constroi o ciclo impar
                closest_ancestor = find_closest_ancestor(parents, v, w)
                odd_cycle = build_odd_cycle(parents, v, w, closest_ancestor)
                return False, odd_cycle # Nao possui biparticao, retorna ciclo impar
    return True, coloration # Possui biparticao