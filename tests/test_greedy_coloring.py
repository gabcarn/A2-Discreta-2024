import unittest

import sys
sys.path.append('../algorithms')
from greedy_coloring import greedy_coloring

sys.path.append('../utils')
from ordenations import random_ordering, largest_first_ordering, smallest_last_ordering

sys.path.append('../data')
from graphs import G_other, G_letters

class TestGreedyColoring(unittest.TestCase):
    def test_no_color_conflict(self):
        coloring = greedy_coloring(G_other)
        
        # Checa se grafos adjacentes possuem mesma cor
        for vertex, neighbors in G_other.items():
            for neighbor in neighbors:
                self.assertNotEqual(coloring[vertex], coloring[neighbor])

    def test_different_vertex_orderings(self):
        # Testa diferentes estratégias de ordenação
        random_coloring = greedy_coloring(G_other, random_ordering(G_other))
        largest_first_coloring = greedy_coloring(G_other, largest_first_ordering(G_other))
        smallest_last_coloring = greedy_coloring(G_other, smallest_last_ordering(G_other))
        
        # Checa se não há conflito de coloração
        for coloring in [random_coloring, largest_first_coloring, smallest_last_coloring]:
            for vertex, neighbors in G_other.items():
                for neighbor in neighbors:
                    self.assertNotEqual(coloring[vertex], coloring[neighbor])

    def test_single_vertex_graph(self):
        graph = {1: []}
        coloring = greedy_coloring(graph)
        self.assertEqual(coloring[1], 0)

    def test_diferent_types(self):
        # Testa o algoritmo com grafos com diferentes entradas (não números inteiros)
        coloring = greedy_coloring(G_letters)
        
        # Checa se não há conflitor de coloração
        for vertex, neighbors in G_letters.items():
            for neighbor in neighbors:
                self.assertNotEqual(coloring[vertex], coloring[neighbor])

if __name__ == '__main__':
    unittest.main()