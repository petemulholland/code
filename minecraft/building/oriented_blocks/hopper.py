from base_oriented_block import OrientedBlock
from building.types import HOPPER
import mcpi.block as block
from mcpi.block import Block
#from mcpi.vec3 import Vec3

class Hopper(OrientedBlock):
	''' Hopper
	0x1, 0x2, 0x4:
	A three-bit field storing a value from 0 to 5:

		0: Output facing down
		1: (unused)
		2: Output facing north
		3: Output facing south
		4: Output facing west
		5: Output facing east
	0x8 	Set if activated/disabled.
	'''

	DOWN = 0
	NORTH = 2
	SOUTH = 3
	WEST = 4
	EAST = 5
	

	def __init__(self, *args, **kwargs):
		super(Hopper, self).__init__(Hopper.NORTH, Hopper.SOUTH, 
									Hopper.EAST, Hopper.WEST, *args, **kwargs)

	def clone(self):
		new_pos2 = None

		assert self.block.id == HOPPER.id, "Invalid block id for Hopper: {0}".format(self.block.id) 
		return Hopper(self.pos.clone(),  Block(self.block.id).withData(self.block.data), 
					  self.description)

