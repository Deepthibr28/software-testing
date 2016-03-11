import unittest
from python.src import age_group_finder

class test_age_finder(unittest.TestCase):

	def test_baby_age(self):
		self.assertEqual('Baby', age_group_finder.find(2))
	def test_toddler_age(self):
		self.assertEqual('Toddler', age_group_finder.find(5))
	def test_children_age(self):
		self.assertEqual('Children', age_group_finder.find(10))
	def test_teen_age(self):
		self.assertEqual('Teen', age_group_finder.find(17))
		self.assertEqual('Teen and Young adult', age_group_finder.find(18))
	def test_youngadult_age(self):
		self.assertEqual('Young adult', age_group_finder.find(22))
	def test_adult_age(self):
		self.assertEqual('Adult', age_group_finder.find(27))
	def test_old_age(self):
		self.assertEqual('Old', age_group_finder.find(80))

	