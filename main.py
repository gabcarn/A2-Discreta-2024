from algorithms.brute_force import exhaustive_search as X
from algorithms.greedy_coloring import greedy_coloring as G
from data.graphs import G_Crow, G_10_9_4, G_10_9_6
import unittest

# print(X(G_10_9_6, 6, [])) # Numero cromatico = 4, coloracao encontrada: 5-coloracao
# print(X(G_10_9_6, 6, []))
# print(X(G_Crow, 5, []))

# print(G(G_10_9_4))
# print(G(G_10_9_6))
# print(G(G_Crow))

if __name__ == '__main__':
    unittest.main(verbosity=2)