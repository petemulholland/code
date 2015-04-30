from base_oriented_block import OrientedBlock
from building.types import TORCH_REDSTONE_ACTIVE, TORCH_REDSTONE_INACTIVE
import mcpi.block as block
from mcpi.block import Block

class Wood(OrientedBlock):
	'''Wood NOTE: Acacia & Dark oak were added in 1.7
		
		Block id:17
		
		DV 	Description
		0 	0000 Oak wood facing up/down
		1 	0001 Spruce wood facing up/down
		2 	0010 Birch wood facing up/down
		3 	0011 Jungle wood facing up/down
		4 	0100 Oak wood facing East/West
		5 	0101 Spruce wood facing East/West
		6 	0110 Birch wood facing East/West
		7 	0111 Jungle wood facing East/West
		8 	1000 Oak wood facing North/South
		9 	1001 Spruce wood facing North/South
		10 	1010 Birch wood facing North/South
		11 	1011 Jungle wood facing North/South
		12 	1100 Oak wood with only bark
		13 	1101 Spruce wood with only bark
		14 	1110 Birch wood with only bark
		15 	1111 Jungle wood with only bark'''

	OAK = 0
	SPRUCE = 1
	BIRCH = 2
	JUNGLE = 3

	TYPE_MASK = 3

	UP_DOWN = 0
	EAST_WEST = 4
	NORTH_SOUTH = 8
	ORIENTATION_MASK = NORTH_SOUTH + EAST_WEST

	VALID_IDS = [block.WOOD]

	def __init__(self, *args, **kwargs):
		super(Wood, self).__init__({'NORTH': Wood.NORTH_SOUTH, 
									'SOUTH': Wood.NORTH_SOUTH, 
									'EAST' : Wood.EAST_WEST,
									'WEST' : Wood.EAST_WEST},
								   *args, **kwargs)

	def clone(self):
		new_pos2 = None

		assert self.block.id in Wood.VALID_IDS, "Invalid block id for Torch: {0}".format(self.block.id) 
		return Wood(self.pos.clone(),  Block(self.block.id).withData(self.block.data), 
					 self.description)

	def rotateLeft(self):  
		super(OrientedBlock, self).rotateLeft()
		
		if self.block.data & ORIENTATION_MASK not in self.left_rotation:
			print "Invalid data on block: ({0})".format(str(self.block))
		else:
			self.block.data = self.left_rotation[self.block.data & ORIENTATION_MASK] + self.block.data & TYPE_MASK
	

	def rotateRight(self, ct=1): 
		for i in range(ct):	
			super(OrientedBlock, self).rotateRight()
			if self.block.data & ORIENTATION_MASK not in self.right_rotation:
				print "Invalid data on block: ({0})".format(str(self.block))
			else:
				self.block.data = self.right_rotation[self.block.data & ORIENTATION_MASK] + self.block.data & TYPE_MASK
