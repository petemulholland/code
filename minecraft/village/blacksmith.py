from building import Building, BuildingLayer, BuildingBlock, TABLE_TOP
from oriented_blocks import Stair, Furnace, Chest
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3


class Blacksmith(Building):
	"""description of class"""

	WALLS_CORNER_POS = {'South East' : Building.SE_CORNER_POS + Vec3(0,0,-1), 
						'South West' : Building.SE_CORNER_POS + Vec3(-9,0,-1),
						'North West' : Building.SE_CORNER_POS + Vec3(-9,0,-7),
						'North East' : Building.SE_CORNER_POS + Vec3(0,0,-7) }

	STAIR_SPAN = (WALLS_CORNER_POS['South West'] + Vec3(1,0,1), 
					WALLS_CORNER_POS['South West'] + Vec3(3,0,1))

	LAVAPIT_SPAN = (WALLS_CORNER_POS['North West'], 
					WALLS_CORNER_POS['North West'] + Vec3(3,0,2))
	LAVA_SPAN = (WALLS_CORNER_POS['North West'] + Vec3(1,0,1), 
					WALLS_CORNER_POS['North West'] + Vec3(2,0,1))
	FURNACE_POS = WALLS_CORNER_POS['North West'] + Vec3(3,0,3)

	CORNER_POSTS = (WALLS_CORNER_POS['South East'],
					WALLS_CORNER_POS['North East'],
					WALLS_CORNER_POS['South East'] + Vec3(-3,0,0))
	FENCES_POS = (WALLS_CORNER_POS['South West'], 
					WALLS_CORNER_POS['South West'] + Vec3(4,0,0))
	
	WINDOWS_POS = ((WALLS_CORNER_POS['North East'] + Vec3(-2,0,0), 
					"North wall, east window"), 
					(WALLS_CORNER_POS['North East'] + Vec3(-4,0,0), 
					"North wall, west window"), 
					(WALLS_CORNER_POS['North East'] + Vec3(0,0,2), 
					"East wall, north window"), 
					(WALLS_CORNER_POS['North East'] + Vec3(0,0,4), 
					"East wall, south window"))

	WALL_SPANS = [(WALLS_CORNER_POS['North East'] + Vec3(-1,0,0), 
					WALLS_CORNER_POS['North East'] + Vec3(-5,0,0),
					"North wall"),
					(WALLS_CORNER_POS['North East'] + Vec3(0,0,1), 
					WALLS_CORNER_POS['North East'] + Vec3(0,0,5),
					"East wall"),
					(WALLS_CORNER_POS['South East'] + Vec3(-1,0,0), 
					WALLS_CORNER_POS['South East'] + Vec3(-2,0,0),
					"South wall"),
					(WALLS_CORNER_POS['South East'] + Vec3(-4,0,-3), 
					WALLS_CORNER_POS['South East'] + Vec3(-5,0,-3),
					"Central East wall"),
					(WALLS_CORNER_POS['South East'] + Vec3(-3,0,-1), 
					WALLS_CORNER_POS['South East'] + Vec3(-3,0,-2),
					"Door wall"),]
	
	DOOR_POS = WALLS_CORNER_POS['South East'] + Vec3(-3,0,-1)

	WIDTH = 10
	def __init__(self, *args, **kwargs):
		super(Blacksmith, self).__init__(width=Blacksmith.WIDTH, *args, **kwargs)

		#######################################################################
		# level 1
		layer_blocks = []
		layer_blocks.append(BuildingBlock(Blacksmith.WALLS_CORNER_POS['South East'], 
										block.COBBLESTONE, 
										Blacksmith.WALLS_CORNER_POS['North West'],
										description="Base"))
		layer_blocks.append(Stair(Blacksmith.STAIR_SPAN[0], 
								block.STAIRS_COBBLESTONE.withData(Stair.NORTH),
								Blacksmith.STAIR_SPAN[1],
								description="Steps"))

		self.layers.append(BuildingLayer(layer_blocks, 0))
		del layer_blocks[:] 

		#######################################################################
		# common blocks on several levels
		fences = []
		for pos in Blacksmith.FENCES_POS:
			fences.append(BuildingBlock(pos, block.FENCE, description="Post"))

		corners = []
		for pos in Blacksmith.CORNER_POSTS:
			corners.append(BuildingBlock(pos, block.WOOD, description="Corner block"))

		# walls, corners & fences are all included in layers that have walls.
		walls = []
		for span in Blacksmith.WALL_SPANS:
			walls.append(BuildingBlock(span[0], block.WOOD_PLANKS, span[1],
										description=span[2]))

		walls.extend(corners)
		walls.extend(fences)

		walls.append(BuildingBlock(Blacksmith.DOOR_POS, block.AIR, description="Clear door"))

		#######################################################################
		# level 2
		# fire pit & furnace
		layer_blocks.append(BuildingBlock(Blacksmith.LAVAPIT_SPAN[0], 
							  block.COBBLESTONE, Blacksmith.LAVAPIT_SPAN[1],
							  description="Lava pit"))
		layer_blocks.append(BuildingBlock(Blacksmith.LAVA_SPAN[0], 
							  block.LAVA_STATIONARY, Blacksmith.LAVA_SPAN[1],
							  description="Lava"))
		layer_blocks.append(BuildingBlock(Blacksmith.FURNACE_POS, 
							  block.COBBLESTONE,
							  description="Furnace base"))
		# walls
		layer_blocks.extend(walls)
		
		# seating area
		layer_blocks.append(BuildingBlock(Blacksmith.WALLS_CORNER_POS['North East'] + Vec3(-1,0,1), 
										block.WOOD_PLANKS, description="Seating area corner"))
		layer_blocks.append(Stair(Blacksmith.WALLS_CORNER_POS['North East'] + Vec3(-2,0,1), 
								block.STAIRS_WOOD.withData(Stair.NORTH), description="North seat"))
		layer_blocks.append(Stair(Blacksmith.WALLS_CORNER_POS['North East'] + Vec3(-1,0,2), 
								block.STAIRS_WOOD.withData(Stair.EAST), description="East seat"))
		layer_blocks.append(BuildingBlock(Blacksmith.WALLS_CORNER_POS['North East'] + Vec3(-2,0,2), 
									block.FENCE, description="Table base"))
		
		# anvil & chest
		layer_blocks.append(BuildingBlock(Blacksmith.WALLS_CORNER_POS['South West'] + Vec3(1,0,-2), 
										block.STONE_SLAB_DOUBLE, description="Anvil"))
		layer_blocks.append(Chest(Blacksmith.WALLS_CORNER_POS['North East'] + Vec3(-5,0,1), 
										block.CHEST.withData(Chest.WEST), description="Chest"))

		self.layers.append(BuildingLayer(layer_blocks, 1))
		del layer_blocks[:] 

		#######################################################################
		# level 3
		# lava pit & furnace area
		furnace = Furnace(Blacksmith.FURNACE_POS, block.FURNACE_INACTIVE.withData(Furnace.NORTH),
					description="Furnace")

		layer_blocks.append(BuildingBlock(Blacksmith.LAVAPIT_SPAN[0], 
							  block.COBBLESTONE, Blacksmith.LAVAPIT_SPAN[1],
							  description="Lava pit"))
		layer_blocks.append(BuildingBlock(Blacksmith.LAVA_SPAN[0] + Vec3(-1,0,0), 
							  block.AIR, Blacksmith.LAVA_SPAN[1] + Vec3(0,0,1),
								description="Clear area over lava"))
		# TODO: are IRON BARS available? - don't see in block list
		layer_blocks.append(BuildingBlock(Blacksmith.LAVAPIT_SPAN[0] + Vec3(0,0,1), 
							  block.DOOR_IRON, Blacksmith.LAVAPIT_SPAN[0] + Vec3(0,0,2),
							  description="Iron doors to west of lava pit"))
		layer_blocks.append(furnace)
		layer_blocks.extend(walls)

		# windows
		for pos, desc in Blacksmith.WINDOWS_POS:
			layer_blocks.append(BuildingBlock(pos, block.GLASS_PANE, description=desc))

		# TODO: table top, no carpet or pressure plates in mcpi, single stone slab?
		layer_blocks.append(BuildingBlock(Blacksmith.WALLS_CORNER_POS['North East'] + Vec3(-2,0,2), 
										TABLE_TOP, description="Table top"))

		self.layers.append(BuildingLayer(layer_blocks, 2))
		del layer_blocks[:]
		
		# remove door clear from walls:
		walls = walls[:len(walls) - 1]

		#######################################################################
		# level 4
		# lava pit & furnace area
		layer_blocks.append(BuildingBlock(Blacksmith.LAVAPIT_SPAN[0], 
							  block.COBBLESTONE, Blacksmith.LAVAPIT_SPAN[1],
							  description="Lava pit ceiling"))
		layer_blocks.append(furnace)
		layer_blocks.extend(walls)

		self.layers.append(BuildingLayer(layer_blocks, 3))
		del layer_blocks[:]

		#######################################################################
		# level 5 roof
		layer_blocks.append(BuildingBlock(Blacksmith.WALLS_CORNER_POS['South East'], 
										block.COBBLESTONE, 
										Blacksmith.WALLS_CORNER_POS['North West'],
										description="Roof"))
		layer_blocks.extend(corners)

		self.layers.append(BuildingLayer(layer_blocks, 4))
		del layer_blocks[:]

		#######################################################################
		# level 6 roof surround
		layer_blocks.append(BuildingBlock(Blacksmith.WALLS_CORNER_POS['South East'], 
										block.STONE_SLAB, 
										Blacksmith.WALLS_CORNER_POS['North West'],
										description="Roof half slabs"))
		# clear slabs inside border
		layer_blocks.append(BuildingBlock(Blacksmith.WALLS_CORNER_POS['South East'] + Vec3(-1,0,-1), 
							  block.AIR, Blacksmith.WALLS_CORNER_POS['North West'] + Vec3(1,0,1),
							  description="clear central roof slabs"))

		self.layers.append(BuildingLayer(layer_blocks, 5))
		del layer_blocks[:]

		self._set_orientation()
		
	def build(self, mc):
		super(Blacksmith, self).build(mc)


