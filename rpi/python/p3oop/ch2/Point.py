import math

class Point:
	'Point in 2 dimentional coords'
	def __init__(self, x=0, y=0):
		''' Initialize the position of a new Point
		The x and y corrds can be specified
		If not specified, point defaults to the origin'''
		self.move(x, y)
	
	def move(self, x, y):
		'''Move the point to a new location'''
		self.x = x
		self.y = y
	
	def reset(self):
		'''Reset the point back to origin'''
		self.move(0, 0)
	
	def calculate_distance(self, other_point):
		'''Calculate the distance from this point to a second
		point passed as a parameter'''
		return math.sqrt((self.x - other_point.x) ** 2 + 
						 (self.y - other_point.y) ** 2)




