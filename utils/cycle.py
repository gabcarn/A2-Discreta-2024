from typing import Dict, Any, Union, Tuple, List
from collections import deque

def build_odd_cycle(parents: Dict[Any, Any], v: Any, w: Any,
                    closest_ancestor: Any) -> List[Any]:
    """Constroi o ciclo impar baseado no ancestral comum mais proximo.

    Args:
        parents (Dict[Any, Any]): Dicionario onde as chaves sao vertices e os valores sao
                                os vertices "pais".
        v (Any): Um vertice que participa do ciclo.
        w (Any): O outro vertice que participa do ciclo.
        closest_ancestor (Any): Ancestral mais proximo dos vertices v e w.

    Returns:
        List[Any]: Lista dos vertices de um ciclo impar baseado no ancestral comum mais
        proximo dos vertices v e w.
    """
    v_path = []
    # Encontra a linha de ancestralidade de v ate closest_ancestor
    while v != closest_ancestor:
        v_path.append(v)
        v = parents[v]
    w_path = []
    # Encontra a linha de ancestralidade de w ate closest_ancestor
    while w != closest_ancestor:
        w_path.append(w)
        w = parents[w]
    # Retorna o ciclo impar: de v ate u, seguido de u ate w
    return v_path + [closest_ancestor] + w_path[::-1]

def find_closest_ancestor(parents: Dict[Any, Any], v: Any, w: Any) -> Any:
    """Encontra o ancestral comum mais proximo de v e w na arvore parents.

    Args:
        parents (Dict[Any, Any]): Dicionario onde as chaves sao vertices e os valores sao
                                os vertices "pais".
        v (Any): Um vertice cujo ancestral esta sendo procurado.
        w (Any): O outro vertice cujo ancestral esta sendo procurado.

    Returns:
        Any: Ancestral comum mais proximo de v e w na arvore parents.
    """
    v_ancestors = set()
    # Encontra todos os ancestrais de v
    while v in parents:
        v_ancestors.add(v)
        v = parents[v]
    # Encontra o ancestral comum mais proximo de v e w
    while w not in v_ancestors:
        w = parents[w]
    return w