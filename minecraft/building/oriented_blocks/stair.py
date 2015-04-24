from base_oriented_block import OrientedBlock
from building.types import STAIRS_BIRCH, STAIRS_BRICK, STAIRS_JUNGLE, STAIRS_NETHER_BRICK, STAIRS_QUARTZ, STAIRS_SANDSTONE, STAIRS_SPRUCE, STAIRS_STONE_BRICK
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3
import time
import random

class Stair(OrientedBlock):
	''' 0x1 
		0x2 A two-bit field containing a value from 0 to 3 specifying the direction of the stairs' full-block side:
			0: East
			1: West
			2: South
			3: North

		0x4 	Set if stairs are upside-down'''

	EAST = 0
	WEST = 1
	SOUTH = 2
	NORTH = 3
	
	ORIENTATION_MASK = 3

	# need to override roatate methods to account for upside down mask
	UPSIDE_DOWN = 4 # this is a bit field so should be added to the orientation values above

	# http://minecraft.gamepedia.com/Data_values#Block_IDs
	VALID_IDS = [block.STAIRS_WOOD.id,
				 block.STAIRS_COBBLESTONE.id,
				 STAIRS_BRICK.id,
				 STAIRS_STONE_BRICK.id,
				 STAIRS_NETHER_BRICK.id,
				 STAIRS_SANDSTONE.id,
				 STAIRS_SPRUCE.id,
				 STAIRS_BIRCH.id,
				 STAIRS_JUNGLE.id,
				 STAIRS_QUARTZ.id,
				 ]
	
	def __init__(self, *args, **kwargs):
		super(Stair, self).__init__(Stair.NORTH, Stair.SOUTH, 
									Stair.EAST, Stair.WEST, *args, **kwargs)
	def invert(self):
		# ^ does a bitwise XOR
		self.block.data = self.block.data ^ Stair.UPSIDE_DOWN

	def clone(self):
		new_pos2 = None
		if self.pos2 is not None:
			new_pos2 = self.pos2.clone()

		assert (self.block.id in Stair.VALID_IDS), "Invalid block id for Stair: {0}".format(self.block.id)
		
		return Stair(self.pos.clone(), self.block.clone(), new_pos2, self.description)

	def rotateLeft(self):  
		# this appears to work as required, doesn't call OrientedBlock.rotate, just calls BuildingBlock.rotate to rotate posns
		super(OrientedBlock, self).rotateLeft() 
		
		if self.block.data & Stair.ORIENTATION_MASK not in self.left_rotation:
			print "Invalid data on block: ({0})".format(str(self.block))
		else:
			self.block.data = self.left_rotation[self.block.data & Stair.ORIENTATION_MASK] + self.block.data & Stair.UPSIDE_DOWN
	
	def rotateRight(self, ct=1): 
		for i in range(ct):	
			# this appears to work as required, doesn't call OrientedBlock.rotate, just calls BuildingBlock.rotate to rotate posns
			super(OrientedBlock, self).rotateRight()
			if self.block.data  & Stair.ORIENTATION_MASK not in self.right_rotation:
				print "Invalid data on block: ({0})".format(str(self.block))
			else:
				self.block.data = self.right_rotation[self.block.data & Stair.ORIENTATION_MASK] + self.block.data & Stair.UPSIDE_DOWN

