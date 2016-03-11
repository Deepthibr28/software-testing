import unittest
from python.src import largest_num_finder

class test_largest_num_finder(unittest.TestCase):

	def test_a_largest(self):
		self.assertEqual(5, largest_num_finder.find(5,2,3))
		self.assertEqual(5, largest_num_finder.find(5,3,2))
	def test_b_largest(self):
		self.assertEqual(5, largest_num_finder.find(2,5,3))
		self.assertEqual(5, largest_num_finder.find(3,5,2))
	def test_c_largest(self):
		self.assertEqual(5, largest_num_finder.find(2,3,5))
		self.assertEqual(5, largest_num_finder.find(3,2,5))
	def test_none_largest(self):
		self.assertEqual(5, largest_num_finder.find(5,5,5))
		self.assertEqual(5, largest_num_finder.find(5,3,3))