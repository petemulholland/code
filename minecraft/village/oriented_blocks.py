from building import BuildingBlock
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3
import time
import random


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
			print "Invalid data on block: (id:{0}, data:{1)}".format(str(self.block))
	
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
				print "Invalid data on block: (id:{0}, data:{1})".format(str(self.block))

class Torch(OrientedBlock):
	EAST = 1
	WEST = 2
	SOUTH = 3
	NORTH = 4
	
	def __init__(self, *args, **kwargs):
		super(Torch, self).__init__(Torch.NORTH, Torch.SOUTH, 
									Torch.EAST, Torch.WEST, *args, **kwargs)

	def clone(self):
		new_pos2 = None
		if self.pos2 is not None: # shouldn't be required?
			new_pos2 = self.pos2.clone()
		# TODO: is mcpi Block object clonable - i need clone here)
		assert self.block.id == block.TORCH.id, "Invalid block id for Torch: {0}".format(self.block.id) 
		return Torch(self.pos.clone(),  block.TORCH.withData(self.block.data), 
					new_pos2, self.description)

class Stair(OrientedBlock):
	EAST = 0
	WEST = 1
	SOUTH = 2
	NORTH = 3
	
	def __init__(self, *args, **kwargs):
		super(Stair, self).__init__(Stair.NORTH, Stair.SOUTH, 
									Stair.EAST, Stair.WEST, *args, **kwargs)
	
	def clone(self):
		new_pos2 = None
		if self.pos2 is not None:
			new_pos2 = self.pos2.clone()

		# TODO: seen brick stairs in inventory, find block id. any other stair types?
		assert (self.block.id == block.STAIRS_COBBLESTONE.id or 
				self.block.id == block.STAIRS_WOOD.id), "Invalid block id for Stair: {0}".format(self.block.id)
		
		return Stair(self.pos.clone(), self.block.clone(), new_pos2, self.description)

class Door(OrientedBlock):
	NORTH = 1
	WEST = 0
	SOUTH = 3
	EAST = 2

	HINGE_LEFT = 8
	HINGE_RIGHT = 9

	def __init__(self, hinge_side=None, *args, **kwargs):
		super(Door, self).__init__(Door.NORTH, Door.SOUTH,
									Door.EAST, Door.WEST, 
									*args, **kwargs)
		if hinge_side == None:
			hinge_side = random.choice([Door.HINGE_LEFT, Door.HINGE_RIGHT])

		self.hinge_side = hinge_side

	def clone(self):
		assert(self.hinge_side is not None), "Hinge side on door not set"
		new_pos2 = None
		if self.pos2 is not None:
			new_pos2 = self.pos2.clone()
		
		return Door(self.pos.clone(), self.block.clone(), new_pos2, self.description, self.hinge_side)

	def build_at(self, mc, pos):
		self._build(mc, Vec3(pos.x, pos.y + 1, pos.z),
						self.block.withData(self.hinge_side))
		self._build(mc, pos, self.block)
		
	def clear_at(self, mc, pos, fill=block.AIR):
		self._build(mc, Vec3(pos.x, pos.y + 1, pos.z), fill)
		self._build(mc, pos, fill)


# Ladder, chest & furnace share orientation values:
class CommonOriented(OrientedBlock):
	# changed these values from the "facing" direction so ladder is on side of block specified
	# TODO: check that furnace and chest face correct direction!
	NORTH = 3 
	SOUTH = 2
	WEST = 5
	EAST = 4
	
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


