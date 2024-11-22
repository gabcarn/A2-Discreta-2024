import unittest

import sys
sys.path.append('../algorithms')
from bipartition import bipartition

sys.path.append('../data')
from graphs import G_bipartite, G_non_bipartite

class TestBipartition(unittest.TestCase):
    def test_bipartite_graph(self):
        is_bipartite, coloration = bipartition(G_bipartite)
        self.assertTrue(is_bipartite)
        # Verifica se as cores de vértices adjacentes são diferentes e se são 1 ou 2
        for vertex, neighbors in G_bipartite.items():
            for neighbor in neighbors:
                self.assertNotEqual(coloration[vertex], coloration[neighbor])
                self.assertIn(coloration[vertex], [1, 2])

    def test_non_bipartite_graph(self):
        is_bipartite, odd_cycle = bipartition(G_non_bipartite)
        self.assertFalse(is_bipartite)
        
        # Verifica se o ciclo tem comprimento ímpar
        self.assertTrue(len(odd_cycle) % 2 == 1)
        
        # Verifica se o ciclo está no grafo
        for i in range(len(odd_cycle)):
            next_vertex = odd_cycle[(i + 1) % len(odd_cycle)]
            self.assertIn(next_vertex, G_non_bipartite[odd_cycle[i]])

    def test_single_vertex_graph(self):
        G = {1: []}
        is_bipartite, coloration = bipartition(G)
        self.assertTrue(is_bipartite)