from algorithms.brute_force import exhaustive_search as X
from algorithms.greedy_coloring import greedy_coloring as G
from algorithms.chromatic_polynomial import chromatic_polynomial as P
from data.graphs import G_Crow, G_10_9_4, G_10_9_6, K4_uncompleted, K5_uncompleted
import unittest

# print(X(G_10_9_6, 6, [])) # Numero cromatico = 4, coloracao encontrada: 5-coloracao
# print(X(G_10_9_6, 6, []))
# print(X(G_Crow, 5, []))

# print(G(G_10_9_4))
# print(G(G_10_9_6))
# print(G(G_Crow))

# print(P(G_10_9_4, len(G_10_9_4)))
# print(P(G_10_9_6, len(G_10_9_6)))
# print(P(K5_uncompleted, len(K5_uncompleted)))