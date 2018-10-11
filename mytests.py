import unittest
import score_personne 
class MyFirstTests(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')
#############################################################

    def test_person1(self):
        self.assertEqual(score_person(name, age), '66%')

    def test_person2(self):
        self.assertEqual(score_person(name, age), '50%')

    def test_person3(self):
        self.assertEqual(score_person(name, age), '43%')

    def test_person4(self):
        self.assertEqual(score_person(name, age), '75%')
