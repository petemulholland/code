from building import BuildingBlock
import mcpi.block as block
from mcpi.vec3 import Vec3

class OrientedBlock(BuildingBlock):
	def __init__(self, *args, **kwargs):
		super(OrientedBlock, self).__init__(*args, **kwargs)
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
	EAST = 1
	WEST = 2
	SOUTH = 3
	NORTH = 4

	def __init__(self, *args, **kwargs):
		super(Torch, self).__init__(*args, **kwargs)
		self.EAST = Torch.EAST
		self.WEST = Torch.WEST
		self.SOUTH = Torch.SOUTH
		self.NORTH = Torch.NORTH
		
class Ladder(OrientedBlock):
	NORTH = 2
	SOUTH = 3
	WEST = 4
	EAST = 5

	def __init__(self, *args, **kwargs):
		super(Ladder, self).__init__(*args, **kwargs)
		self.NORTH = Ladder.NORTH
		self.SOUTH = Ladder.SOUTH
		self.WEST = Ladder.WEST
		self.EAST = Ladder.EAST

class Stair(OrientedBlock):
	EAST = 0
	WEST = 1
	SOUTH = 2
	NORTH = 3

	def __init__(self, *args, **kwargs):
		super(Stair, self).__init__(*args, **kwargs)
		self.EAST = Stair.EAST
		self.WEST = Stair.WEST
		self.SOUTH = Stair.SOUTH
		self.NORTH = Stair.NORTH

		