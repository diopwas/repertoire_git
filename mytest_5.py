import unittest
from score_personne import *
class MyFirstTests(unittest.TestCase):
    def test_person4(self):
        self.assertEqual(score_person('Ely', 28), '75%')
