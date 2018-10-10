import unittest
from score_personne import *  # j'importe le module contenant ma fonction
class MyFirstTests(unittest.TestCase):
    def test_person1(self):
        self.assertEqual(score_person('Joseph', 15), '66%')

        # je viens de faire un 3e commit
