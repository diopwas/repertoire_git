import unittest
from score_personne import *
class MyFirstTests(unittest.TestCase):
        def test_person3(self):
                self.assertEqual(score_person('Marc', 60), '43%')
