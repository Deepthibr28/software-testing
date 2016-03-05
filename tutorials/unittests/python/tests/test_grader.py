import unittest
from python.src import grader

class test_grader(unittest.TestCase):

	def test_calculator_returns_A(self):
		self.assertEqual('A', grader.calculator(98))
		
	def test_calculator_returns_B(self):
		self.assertEqual('B', grader.calculator(90))
		
	def test_calculator_returns_C(self):
		self.assertEqual('C', grader.calculator(80))
		
	def test_calculator_returns_D(self):
		self.assertEqual('D', grader.calculator(70))
		
	def test_calculator_returns_None(self):
		self.assertEqual('F', grader.calculator(50))
        #self.assertEqual(5, 5)
        #self.assertTrue(False)
