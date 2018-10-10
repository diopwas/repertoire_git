import unittest
from score_personne import *
class MyFirstTests(unittest.TestCase):
        def test_person2(self):
                self.assertEqual(score_person('Marie', 33), '50%')
