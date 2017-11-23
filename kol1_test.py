import unittest
from kol1 import MathUtil
from kol1 import Coordinates

#MarcelinaKochman


class MyTest(unittest.TestCase):

	def set_up_variables(self):
		self.test_angle = -180
		self.test_point_x = Coordinates(1,2)
		self.test_point_y = Coordinates(2,4)

	def test_normalize_degrees(self):
		returned_value = MathUtil.normalize_degrees(self.test_angle)
		self.assertEqual(returned_value, 180)
		
	def test_normalize_degrees(self):
		self.assertEqual(0, 0)
	
	
	
if __name__ == "__main__":
	unittest.main()