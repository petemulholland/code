from building import BuildingBlock
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3
import time
import random

#TODO: beak these out into separate files in and oriented_blocks package
# other oriented blocks to be defined: ??
# http://minecraft.gamepedia.com/Data_values#Block_IDs
#	- redstone repeater
#	- piston (& sticky piston)
#	- button
#	- lever
#	- hopper
#	- sign
#	- painting?
#	- dispenser
#	- fence gate?
#	- bookshelf

# NOTE: oriented block data appears to always indicate the direction the item is "facing"
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
	''' The total data needed to accurately describe a single door tile is now contained in both door tiles, so both data values have to be inspected.
		Common to both door tiles, the top bit (0x8) is as follows:
			0: The bottom half of the door
			1: The top half of the door

		Top Sections
			The least-significant bit (0x1) is as follows, assuming you're facing the same direction the door faces while closed:
				0: Hinge is on the right (this is the default for single doors)
				1: Hinge is on the left (this will be used for the other half of a double-door combo)

			The other two bits (0x2 and 0x4) are always zero.
			The only valid values for a top section, therefore, are 8 (binary 1000) and 9 (binary 1001).

		Bottom Sections
			The second bit (0x4) determines the door's state:
				0: Closed
				1: Open

			The bottom two bits determine which direction the door faces (these directions given for which direction the door faces while closed)
				0: Facing west
				1: Facing north
				2: Facing east
				3: Facing south

		Starting at Minecraft ??
			The second bit for the top half of the door (0x2) determines whether the door is Powered or Unpowered.
				0: Door is Unpowered
				1: Door is Powered
			Which means the top section, now uses values 8, 9, 10, and 11. '''

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
	# TODO: Fix this and correct Church layout & Small House V1 (any other ladders used?)
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


