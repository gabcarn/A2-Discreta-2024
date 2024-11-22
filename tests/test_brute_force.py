import unittest
import numpy as np
from algorithms.brute_force import exhaustive_search
from data.graphs import G_Crow, G_10_9_4, G_10_9_6

class IncompleteColoring(unittest.TestCase):
    def test_q_greather_than_chromatic(self):
        self.assertEqual(exhaustive_search(G_10_9_4, 4, []), [0, 1, 2, 3, 0, 1, 0, 1, 0, 1])
        
    def test_q_equal_chromatic(self):
        self.assertEqual(exhaustive_search(G_10_9_6, 6, [0, 1, 2, 3, 4]), [0, 1, 2, 3, 4, 5, 0, 1, 0, 1])
     
    def test_q_less_than_chromatic(self):
        self.assertEqual(exhaustive_search(G_Crow, 3, [0, 2, 1]), [])
    
    def test_q_greather_than_vertices(self):
         self.assertEqual(exhaustive_search(G_10_9_4, 11, [0, 2, 7, 7, 3]), [])

class CompleteColoring(unittest.TestCase):
    def test_complete_coloring_invalid(self):
         self.assertEqual(exhaustive_search(G_10_9_6, 6, [0, 1, 2, 3, 4, 5, 0, 0, 1, 1]), [])

    def test_complete_coloring_valid(self):
        self.assertEqual(exhaustive_search(G_Crow, 6, [0, 1, 2, 3, 4, 5]), [0, 1, 2, 3, 4, 5])