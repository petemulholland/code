from base_oriented_block import OrientedBlock
from building.types import TORCH_REDSTONE_ACTIVE, TORCH_REDSTONE_INACTIVE
import mcpi.block as block
from mcpi.block import Block
#from mcpi.vec3 import Vec3

class Torch(OrientedBlock):
	''' Also applies to redstone torches
	1 	Facing east (attached to a block to its west)
	2 	Facing west (attached to a block to its east)
	3 	Facing south (attached to a block to its north)
	4 	Facing north (attached to a block to its south)
	5 	Facing up (attached to a block beneath it)
	'''

	EAST = 1
	WEST = 2
	SOUTH = 3
	NORTH = 4
	UP = 5
	
	# TODO: implement UP
	VALID_IDS = [block.TORCH.id,
				 TORCH_REDSTONE_ACTIVE.id,
				 TORCH_REDSTONE_INACTIVE.id, 
				 ]

	def __init__(self, *args, **kwargs):
		super(Torch, self).__init__(Torch.NORTH, Torch.SOUTH, 
									Torch.EAST, Torch.WEST, *args, **kwargs)

	def clone(self):
		new_pos2 = None

		assert self.block.id in Torch.VALID_IDS, "Invalid block id for Torch: {0}".format(self.block.id) 
		return Torch(self.pos.clone(),  Block(self.block.id).withData(self.block.data), 
					 self.description)

