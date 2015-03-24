class Vec3:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	
	def __add__(self, other):
		return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
		
	def __radd__(self, other):
		return self + other
	
	def __iadd__(self, other):
		self.x += other.x
		self.y += other.y
		self.z += other.z
		return self

	def rotateLeft(self):
		self.x, self.z = self.z * -1, self.x
		
	def rotateRight(self):
		self.x, self.z = self.z, self.x * -1
	
	def clone(self):
		return Vec3(self.x, self.y, self.z)
		
	def __str__(self):
		return "({0},{1},{2})".format(self.x, self.y, self.z)

