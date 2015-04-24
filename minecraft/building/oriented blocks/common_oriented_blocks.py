from base_oriented_block import OrientedBlock
import mcpi.block as block
from mcpi.block import Block

# Ladder, chest & furnace share orientation values:
class CommonOriented(OrientedBlock):
	# changed these values from the "facing" direction so ladder is on side of block specified
	'''	0x1, 0x2, 0x4 	
		A three-bit field storing a value from 2 to 5:
			2: Ladder facing north
			3: Ladder facing south
			4: Ladder facing west
			5: Ladder facing east

		Invalid values default to 2.
		'''
	NORTH = 3 
	SOUTH = 2
	WEST = 4
	EAST = 5
	
	def __init__(self, block_type, *args, **kwargs):
		super(CommonOriented, self).__init__(CommonOriented.NORTH, CommonOriented.SOUTH, 
											CommonOriented.EAST, CommonOriented.WEST, 
											*args, **kwargs)
		self.block_type = block_type

	def clone(self):
		new_pos2 = None
		if self.pos2 is not None:
			new_pos2 = self.pos2.clone()
		
		assert self.block.id == self.block_type.id, "Invalid block id for {0}: {1}".format(type(self).__name__, self.block.id)
		
		return type(self)(self.pos.clone(), self.block.clone(), new_pos2, self.description)


class Ladder(CommonOriented):
	
	def __init__(self, *args, **kwargs):
		super(Ladder, self).__init__(block.LADDER, *args, **kwargs)


class Chest(CommonOriented):
	
	def __init__(self, *args, **kwargs):
		super(Chest, self).__init__(block.CHEST, *args, **kwargs)


class Furnace(CommonOriented):
	
	def __init__(self, *args, **kwargs):
		super(Furnace, self).__init__(block.FURNACE_INACTIVE, *args, **kwargs)

