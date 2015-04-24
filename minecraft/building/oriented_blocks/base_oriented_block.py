from building import BuildingBlock
import mcpi.block as block
from mcpi.block import Block

# NOTE: oriented block data appears to always indicate the direction the item is "facing"
class OrientedBlock(BuildingBlock):
	def __init__(self, north=None, south=None, east=None, west=None, *args, **kwargs):
		super(OrientedBlock, self).__init__(*args, **kwargs)
		self.NORTH = north
		self.SOUTH = south
		self.EAST = east
		self.WEST = west
		self.left_rotation = { self.EAST: self.NORTH, 
							   self.SOUTH : self.EAST,
							   self.WEST : self.SOUTH,
							   self.NORTH : self.WEST
							 }
		self.right_rotation = { self.EAST: self.SOUTH, 
							    self.SOUTH : self.WEST,
							    self.WEST : self.NORTH,
							    self.NORTH : self.EAST
							  }

	
	def rotateLeft(self):  
		super(OrientedBlock, self).rotateLeft()
		
		if self.block.data not in self.left_rotation:
			print "Invalid data on block: ({0})".format(str(self.block))
		else:
			self.block.data = self.left_rotation[self.block.data]
	
	def rotateRight(self, ct=1): 
		for i in range(ct):	
			super(OrientedBlock, self).rotateRight()
			if self.block.data not in self.right_rotation:
				print "Invalid data on block: ({0})".format(str(self.block))
			else:
				self.block.data = self.right_rotation[self.block.data]

