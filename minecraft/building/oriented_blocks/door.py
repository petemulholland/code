from base_oriented_block import OrientedBlock
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3
import random

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



