from building import Building, BuildingLayer, BuildingBlock
from oriented_blocks import Torch, Stair, Furnace, Chest
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3


class Blacksmith(Building):
	"""description of class"""

	BASE_SPAN = (Vec3(-2,0,-2), Vec3(7,0,-8))
	STAIR_SPAN = (Vec3(-1,0,-1), Vec3(1,0,-1))

	LAVAPIT_SPAN = (Vec3(-2,0,-6), Vec3(1,0,-8))
	LAVA_SPAN = (Vec3(-1,0,-7), Vec3(0,0,-7))
	FURNACE_POS = Vec3(-1,0,-5)

	CORNER_POSTS = (Vec3(4,0,-2),Vec3(7,0,-2),Vec3(7,0,-8))
	FENCES_POS = (Vec3(-2,0,-2), Vec3(-2,0,2))
	WINDOWS_POS = (Vec3(3,0,-8), Vec3(5,0,-8), Vec3(7,0,-6), Vec3(7,0,-4))

	WALL_SPANS = [(Vec3(2,0,-8), Vec3(6,0,-8)),
					(Vec3(7,0,-3), Vec3(7,0,-7)),
					(Vec3(5,0,-2), Vec3(6,0,-2)),
					(Vec3(2,0,-5), Vec3(3,0,-5))]
	
	DOOR_JAM_POS = Vec3(4,0,-4)
	DOOR_POS = Vec3(4,0,-3)

	def __init__(self, *args, **kwargs):
		super(Blacksmith, self).__init__(*args, **kwargs)

		offset = self.build_pos
		# build the base layer
		BASE_BLOCKS = []
		BASE_BLOCKS.append(BuildingBlock(offset, Blacksmith.BASE_SPAN[0], 
							  block.COBBLESTONE, Blacksmith.BASE_SPAN[1]))
		BASE_BLOCKS.append(Stair(offset, Blacksmith.STAIR_SPAN[0], 
								block.STAIRS_COBBLESTONE.withData(Stair.NORTH),
								Blacksmith.STAIR_SPAN[1]))

		self.layers.append(BuildingLayer(BASE_BLOCKS, 0))

		# common blcoks on several levels
		fences = []
		for pos in Blacksmith.FENCES_POS:
			fences.append(BuildingBlock(offset, pos, block.FENCE))

		corners = []
		for pos in Blacksmith.CORNER_POSTS:
			corners.append(BuildingBlock(offset, pos, block.WOOD))

		# walls, corners & fences are all included in layers that have walls.
		walls = []
		for span in Blacksmith.WALL_SPANS:
			walls.append(BuildingBlock(offset, span[0], block.WOOD_PLANKS, span[1]))

		walls.append(BuildingBlock(offset, Blacksmith.DOOR_JAM_POS, block.WOOD_PLANKS))

		for corner in corners:
			walls.append(corner)
		for fence in fences:
			walls.append(fence)

		# level 1
		# trying to avoid building up lots of lists here, but when i del [:] this will the object in it be deleted?
		layer_blocks = [] 
		# fire pit & furnace
		layer_blocks.append(BuildingBlock(offset, Blacksmith.LAVAPIT_SPAN[0], 
							  block.COBBLESTONE, Blacksmith.LAVAPIT_SPAN[1]))
		layer_blocks.append(BuildingBlock(offset, Blacksmith.LAVA_SPAN[0], 
							  block.LAVA_STATIONARY, Blacksmith.LAVA_SPAN[1]))
		layer_blocks.append(BuildingBlock(offset, Blacksmith.FURNACE_POS, 
							  block.COBBLESTONE))
		# walls
		layer_blocks.extend(walls)
		
		# seating area
		layer_blocks.append(BuildingBlock(offset, Vec3(6,0,-7), block.WOOD_PLANKS))
		layer_blocks.append(Stair(offset, Vec3(5,0,-7), block.STAIRS_WOOD.withData(Stair.NORTH)))
		layer_blocks.append(Stair(offset, Vec3(6,0,-6), block.STAIRS_WOOD.withData(Stair.EAST)))
		layer_blocks.append(BuildingBlock(offset, Vec3(5,0,-6), block.FENCE))
		
		# anvil & chest
		layer_blocks.append(BuildingBlock(offset, Vec3(-1,0,-4), block.STONE_SLAB_DOUBLE))
		layer_blocks.append(Chest(offset, Vec3(-1,0,-4), block.CHEST.withData(Chest.WEST)))

		self.layers.append(BuildingLayer(layer_blocks, 1))
		del layer_blocks[:] # TODO will this del the items in walls?

		# level 2
		# lava pit & furnace area
		furnace = Furnace(offset, Blacksmith.FURNACE_POS, block.FURNACE_INACTIVE.withData(Furnace.NORTH))

		layer_blocks.append(BuildingBlock(offset, Blacksmith.LAVAPIT_SPAN[0], 
							  block.COBBLESTONE, Blacksmith.LAVAPIT_SPAN[1]))
		layer_blocks.append(BuildingBlock(offset, Blacksmith.LAVA_SPAN[0] + Vec3(-1,01), 
							  block.AIR, Blacksmith.LAVA_SPAN[1]))
		# TODO: are IRON BARS available? - don't see in block list
		layer_blocks.append(BuildingBlock(offset, Blacksmith.LAVAPIT_SPAN[0], 
							  block.DOOR_IRON, Blacksmith.LAVAPIT_SPAN[0] + Vec3(0,0,-1)))
		layer_blocks.append(furnace)
		layer_blocks.extend(walls)

		# windows
		for pos in Blacksmith.WINDOWS_POS:
			layer_blocks.append(BuildingBlock(offset, pos, block.GLASS_PANE))

		# TODO: table top, no carpet or pressure plates in mcpi, single stone slab?
		layer_blocks.append(BuildingBlock(offset, Vec3(5,0,-6), block.STONE_SLAB))

		self.layers.append(BuildingLayer(layer_blocks, 2))
		del layer_blocks[:]

		# level 3
		# lava pit & furnace area
		layer_blocks.append(BuildingBlock(offset, Blacksmith.LAVAPIT_SPAN[0], 
							  block.COBBLESTONE, Blacksmith.LAVAPIT_SPAN[1]))
		layer_blocks.append(furnace)
		layer_blocks.extend(walls)
		# add wall block over door
		layer_blocks.append(BuildingBlock(offset, Blacksmith.DOOR_POS, block.WOOD_PLANKS))

		self.layers.append(BuildingLayer(layer_blocks, 3))
		del layer_blocks[:]

		# level 4 roof
		layer_blocks.append(BuildingBlock(offset, Blacksmith.BASE_SPAN[0], 
							  block.COBBLESTONE, Blacksmith.BASE_SPAN[1]))
		layer_blocks.extend(corners)

		self.layers.append(BuildingLayer(layer_blocks, 4))
		del layer_blocks[:]

		# level 5 roof surround
		layer_blocks.append(BuildingBlock(offset, Blacksmith.BASE_SPAN[0], 
							  block.STONE_SLAB, Blacksmith.BASE_SPAN[1]))
		# clear slabs inside border
		layer_blocks.append(BuildingBlock(offset, Blacksmith.BASE_SPAN[0] + Vec3(1,0,-1), 
							  block.AIR, Blacksmith.BASE_SPAN[1] + Vec3(-1,0,1)))

		self.layers.append(BuildingLayer(layer_blocks, 5))
		del layer_blocks[:]

		self._set_orientation()
		
	def build(self, mc):
		super(Blacksmith, self).build(mc)


