from building import BuildingBlock
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

class OrientedBlock(BuildingBlock):
	def __init__(self, north=None, south=None, east=None, west=None, *args, **kwargs):
		super(OrientedBlock, self).__init__(*args, **kwargs)
		self.NORTH = north
		self.SOUTH = south
		self.EAST = east
		self.WEST = west
	
	def rotateLeft(self):  
		super(OrientedBlock, self).rotateLeft()
		
		if self.block.data == self.EAST:	
			self.block.data = self.NORTH
		elif self.block.data == self.SOUTH:
			self.block.data = self.EAST
		elif self.block.data == self.WEST:
			self.block.data = self.SOUTH
		elif self.block.data == self.NORTH:
			self.block.data = self.WEST
		else:
			print "Invalid data on block: (id:{0}, data:{1)}".format(
						self.block.id, self.block.data) # TODO: does mcpi Block implement __str__?
	
	def rotateRight(self, ct=1): 
		for i in range(ct):	
			super(OrientedBlock, self).rotateRight()
			if self.block.data == self.EAST:	
				self.block.data = self.SOUTH
			elif self.block.data == self.SOUTH:
				self.block.data = self.WEST
			elif self.block.data == self.WEST:
				self.block.data = self.NORTH
			elif self.block.data == self.NORTH:
				self.block.data = self.EAST
			else:
				print "Invalid data on block: (id:{0}, data:{1})".format(
							self.block.id, self.block.data) # TODO: does mcpi Block implement __str__?

class Torch(OrientedBlock):
	EAST = 1
	WEST = 2
	SOUTH = 3
	NORTH = 4
	
	def __init__(self, *args, **kwargs):
		super(Torch, self).__init__(Torch.NORTH, Torch.SOUTH, 
									Torch.EAST, Torch.WEST, *args, **kwargs)

	def clone(self):
		new_offset = self.offset.clone()
		new_pos = self.pos.clone()
		new_pos2 = None
		if self.pos2 is not None: # shouldn't be required?
			new_pos2 = self.pos2.clone()
		# TODO: is mcpi Block object clonable - i need clone here)
		assert self.block.id == block.TORCH.id, "Invalid block id for Torch: {0}".format(self.block.id) 
		return Torch(new_offset, new_pos, 
					 block.TORCH.withData(self.block.data), new_pos2)

class Ladder(OrientedBlock):
	NORTH = 2
	SOUTH = 3
	WEST = 4
	EAST = 5
	
	def __init__(self, *args, **kwargs):
		super(Ladder, self).__init__(Ladder.NORTH, Ladder.SOUTH, 
									 Ladder.EAST, Ladder.WEST, *args, **kwargs)

	# TODO: could make this span several blocks vertically, 
	# do I only use this as a block? layer code would screw with level
	# could add a blocks list to building, i.e. not layer specific
	def clone(self):
		new_offset = self.offset.clone()
		new_pos = self.pos.clone()
		new_pos2 = None
		if self.pos2 is not None:
			new_pos2 = self.pos2.clone()
		assert self.block.id == block.LADDER.id, "Invalid block id for Ladder: {0}".format(self.block.id)
		return Ladder(new_offset, new_pos, 
					 block.LADDER.withData(self.block.data), new_pos2)

class Stair(OrientedBlock):
	EAST = 0
	WEST = 1
	SOUTH = 2
	NORTH = 3
	
	def __init__(self, *args, **kwargs):
		super(Stair, self).__init__(Stair.NORTH, Stair.SOUTH, 
									Stair.EAST, Stair.WEST, *args, **kwargs)
	
	def clone(self):
		new_offset = self.offset.clone()
		new_pos = self.pos.clone()
		new_pos2 = None
		if self.pos2 is not None:
			new_pos2 = self.pos2.clone()

		# TODO: seen brick stairs in inventory, find block id. any other stair types?
		assert (self.block.id == block.STAIRS_COBBLESTONE.id or self.block.id == block.STAIRS_WOOD.id), "Invalid block id for Stair: {0}".format(self.block.id)
		
		return Stair(new_offset, new_pos, 
					 Block(self.block.id, self.block.data), new_pos2)

