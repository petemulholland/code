from building import BuildingBlock
import mcpi.block as block
from mcpi.vec3 import Vec3

class OrientedBlock(BuildingBlock):
	def __init__(self, **kwarg):
		super(OrientedBlock, self).__init__(**kwarg)
		self.EAST = None
		self.WEST = None
		self.NORTH = None
		self.SOUTH = None
		
	def rotateLeft(self):  
		super(OrientedBlock, self).rotateLeft()
		
		if self.data == self.EAST:	
			self.data = self.NORTH
		elif self.data == self.SOUTH:
			self.data == self.EAST
		elif self.data == self.WEST:
			self.data = self.SOUTH
		else:
			self.data = self.WEST
		
	
	def rotateRight(self, ct=1): 
		for i in range(ct):	
			self.pos.rotateRight()
			self.pos2.rotateRight()

			if self.data == self.EAST:	
				self.data = self.SOUTH
			elif self.data == self.SOUTH:
				self.data == self.WEST
			elif self.data == self.WEST:
				self.data = self.NORTH
			else:
				self.data = self.EAST

class Torch(OrientedBlock):

	def __init__(self, **kwarg):
		super(Torch, self).__init__(**kwarg)
		self.EAST = 1
		self.WEST = 2
		self.SOUTH = 3
		self.NORTH = 4
		
class Ladder(OrientedBlock):

	def __init__(self, **kwarg):
		super(Ladder, self).__init__(**kwarg)
		self.NORTH = 2
		self.SOUTH = 3
		self.WEST = 4
		self.EAST = 5

class Stair(OrientedBlock):

	def __init__(self, **kwarg):
		super(Stair, self).__init__(**kwarg)
		self.EAST = 0
		self.WEST = 1
		self.SOUTH = 2
		self.NORTH = 3

		