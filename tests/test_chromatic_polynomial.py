import unittest
import numpy as np
from data.graphs import G_Crow, G_10_9_4, G_10_9_6, K2, K3, K4, K4_uncompleted, K5_uncompleted
from algorithms.chromatic_polynomial import chromatic_polynomial

class CompleteGraphs(unittest.TestCase):
    def test_K2(self):
        self.assertEqual(list(chromatic_polynomial(K2, len(K2))), [0, -1, 1])

    def test_K3(self):
        self.assertEqual(list(chromatic_polynomial(K3, len(K3))), [0, 2, -3, 1])

    def test_K4(self):
        self.assertEqual(list(chromatic_polynomial(K4, len(K4))), [0, -6, 11, -6, 1])

    def test_K4_uncompleted(self):
        self.assertEqual(list(chromatic_polynomial(K4_uncompleted, len(K4_uncompleted))), [0, -4, 8, -5, 1])

    def test_K5_uncompleted(self):
        self.assertEqual(list(chromatic_polynomial(K5_uncompleted, len(K5_uncompleted))), [0, 18, -39, 29, -9, 1])

    