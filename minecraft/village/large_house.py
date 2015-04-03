from building import Building, BuildingLayer, BuildingBlock
from oriented_blocks import Torch, Stair
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

class LargeHouse(Building):
	"""description of class"""
	WALLS_CORNER_POS = {'South East' : Building.SE_CORNER_POS + Vec3(0,0,-1),
						'South West' : Building.SE_CORNER_POS + Vec3(-8,0,-1),
						'North West' : Building.SE_CORNER_POS + Vec3(-8,0,-11),
						'North East' : Building.SE_CORNER_POS + Vec3(-2,0,-11),
						'East mid west' : Building.SE_CORNER_POS + Vec3(-2,0,-6),
						'East mid east' : Building.SE_CORNER_POS + Vec3(0,0,-6) }
	
	FLOOR_SPANS = ((WALLS_CORNER_POS['South West'] + Vec3(1,0,-1), 
					WALLS_CORNER_POS['North East'] + Vec3(-1,0,1)), 
					(WALLS_CORNER_POS['East mid west'] + Vec3(0,0,1), 
					WALLS_CORNER_POS['South East'] + Vec3(-1,0,-1)))
	
	# make these all run south to north, so they can be adjusted in a loop
	WINDOW_SPANS = ((WALLS_CORNER_POS['South West'] + Vec3(0,0,-1), 
						WALLS_CORNER_POS['South West'] + Vec3(0,0,-4), 
						"South west window"), 
					(WALLS_CORNER_POS['South West'] + Vec3(0,0,-6), 
						WALLS_CORNER_POS['South West'] + Vec3(0,0,-9),
						"North west window"),
					(WALLS_CORNER_POS['East mid west'] + Vec3(0,0,-1), 
						WALLS_CORNER_POS['East mid west'] + Vec3(0,0,-4),
						"North east window"), 
					(WALLS_CORNER_POS['South East'] + Vec3(0,0,-1), 
						WALLS_CORNER_POS['South East'] + Vec3(0,0,-4),
						"South east window"))
	
	SOUTH_WIN_SPAN = (WALLS_CORNER_POS['South East'] + Vec3(-4,0,0), 
						WALLS_CORNER_POS['South East'] + Vec3(-6,0,0),
						"South wall window")
	
	NORTH_WIN_SPAN = (WALLS_CORNER_POS['North East'] + Vec3(-2,0,0), 
						WALLS_CORNER_POS['North East'] + Vec3(-4,0,0),
						"North gable window")

	DOOR_POS = WALLS_CORNER_POS['South East'] + Vec3(-2,0,0)


	WIDTH = 9
	def __init__(self, *args, **kwargs):
		super(LargeHouse, self).__init__(width=LargeHouse.WIDTH, *args, **kwargs)

		layer_blocks = []
		#######################################################################
		# common blocks
		walls = []
		walls.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['South West'], 
									block.COBBLESTONE, 
									LargeHouse.WALLS_CORNER_POS['North West'],
									description="West wall"))
		walls.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['North West'], 
									block.COBBLESTONE, 
									LargeHouse.WALLS_CORNER_POS['North East'],
									description="North wall"))
		walls.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['North East'], 
									block.COBBLESTONE, 
									LargeHouse.WALLS_CORNER_POS['East mid west'],
									description="East wall, north section"))
		walls.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['East mid west'], 
									block.COBBLESTONE, 
									LargeHouse.WALLS_CORNER_POS['East mid east'],
									description="East wall, extension"))
		walls.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['East mid east'], 
									block.COBBLESTONE, 
									LargeHouse.WALLS_CORNER_POS['South East'],
									description="East wall, south section"))
		walls.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['South East'], 
									block.COBBLESTONE, 
									LargeHouse.WALLS_CORNER_POS['South West'],
									description="South wall"))

		#######################################################################
		# level 1
		layer_blocks.extend(walls)

		for floor_span in LargeHouse.FLOOR_SPANS:
			layer_blocks.append(BuildingBlock(floor_span[0], 
											block.WOOD_PLANKS, floor_span[1],
											description="Floor"))


		layer_blocks.append(Stair(LargeHouse.DOOR_POS + Vec3(0,0,1), 
								block.STAIRS_COBBLESTONE.withData(Stair.NORTH),
								description="Front Stair"))

		self.add_layer(BuildingLayer(layer_blocks, 0))
		del layer_blocks[:]

		#######################################################################
		# level 2
		layer_blocks.extend(walls)
		# Clear door space
		layer_blocks.append(BuildingBlock(LargeHouse.DOOR_POS, 
										block.AIR, description="Clear door"))

		self.add_layer(BuildingLayer(layer_blocks, 1))
		del layer_blocks[:]

		#######################################################################
		# level 3
		# west wall
		windows = []
		for pos1, pos2, desc in LargeHouse.WINDOW_SPANS:
			windows.append(BuildingBlock(pos1, block.WOOD, pos2, description=desc + " frame"))
			windows.append(BuildingBlock(pos1 + Vec3(0,0,-1), block.GLASS_PANE, 
										pos2 + Vec3(0,0,1), description=desc))

		windows.append(BuildingBlock(LargeHouse.SOUTH_WIN_SPAN[0], block.WOOD, 
									LargeHouse.SOUTH_WIN_SPAN[1], 
									description=LargeHouse.SOUTH_WIN_SPAN[2] + " frame"))
		windows.append(BuildingBlock(LargeHouse.SOUTH_WIN_SPAN[0] + Vec3(-1,0,0), block.GLASS_PANE, 
									LargeHouse.SOUTH_WIN_SPAN[1] + Vec3(1,0,0), 
									description=LargeHouse.SOUTH_WIN_SPAN[2]))

		# north wall is cobblestone,
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['North East'],
										block.COBBLESTONE, 
										LargeHouse.WALLS_CORNER_POS['North West'],
										description="North wall"))

		# outer corners are cobblestone
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['South West'],
										block.COBBLESTONE, 
										description="South West corner"))
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['South East'],
										block.COBBLESTONE, 
										description="South East corner"))
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['East mid east'],
										block.COBBLESTONE, 
										description="East extension corner"))
		# place wood plank blocks
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['East mid west'],
										block.WOOD_PLANKS, 
										LargeHouse.WALLS_CORNER_POS['East mid west'] + Vec3(1,0,0),
										description="East extension, planks"))
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['South West'] + Vec3(0,0,-5),
										block.WOOD_PLANKS, 
										description="West wall, planks"))

		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['South West'] + Vec3(1,0,0),
										block.WOOD_PLANKS, 
										description="South wall, planks"))
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['South East'] + Vec3(-1,0,0),
										block.WOOD_PLANKS, 
										LargeHouse.WALLS_CORNER_POS['South East'] + Vec3(-3,0,0),
										description="South wall, door frame"))

		# clear door
		layer_blocks.append(BuildingBlock(LargeHouse.DOOR_POS, 
										block.AIR, description="Clear door"))

		# add windows
		layer_blocks.extend(windows)

		self.add_layer(BuildingLayer(layer_blocks, 2))
		del layer_blocks[:]

		#######################################################################
		# level 4
		# walls
		# West, North & North east cobblestone walls
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['South West'], 
										block.COBBLESTONE, LargeHouse.WALLS_CORNER_POS['North West'],
										description="West wall"))
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['North West'], 
										block.COBBLESTONE, LargeHouse.WALLS_CORNER_POS['North East'],
										description="North wall"))
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['North East'], 
										block.COBBLESTONE, 
										LargeHouse.WALLS_CORNER_POS['East mid west'] + Vec3(0,0,-1),
										description="East wall, north section"))
		# wooden east extension wall
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['East mid west'], 
										block.WOOD_PLANKS, 
										LargeHouse.WALLS_CORNER_POS['East mid east'] + Vec3(-1,0,0),
										description="East wall, extension"))
		# south east cobblestone wall
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['East mid east'], 
										block.COBBLESTONE, LargeHouse.WALLS_CORNER_POS['South East'],
										description="East wall, south section"))
		# wooden south wall (cobblestone corners)
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['South West'] + Vec3(1,0,0), 
										block.WOOD_PLANKS, LargeHouse.WALLS_CORNER_POS['South East'] + Vec3(-1,0,0),
										description="South wall"))

		# roof eaves
		# south roof eaves
		layer_blocks.append(Stair(LargeHouse.WALLS_CORNER_POS['South West'] + Vec3(0,0,1), 
								block.STAIRS_WOOD.withData(Stair.NORTH), 
								LargeHouse.WALLS_CORNER_POS['South East'] + Vec3(0,0,1),
								description="South roof eaves"))
		# 
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['East mid west'] + Vec3(1,0,-1), 
								block.WOOD_PLANKS, description="East roof eaves corner"))

		layer_blocks.append(Stair(LargeHouse.WALLS_CORNER_POS['North East'] + Vec3(1,0,0), 
								block.STAIRS_WOOD.withData(Stair.WEST), 
								LargeHouse.WALLS_CORNER_POS['North East'] + Vec3(1,0,3),
								description="East roof eaves, west facing"))
		layer_blocks.append(Stair(LargeHouse.WALLS_CORNER_POS['East mid east'] + Vec3(0,0,-1), 
								block.STAIRS_WOOD.withData(Stair.SOUTH), 
								description="East roof eaves, north facing"))

		layer_blocks.append(Torch(LargeHouse.DOOR_POS + Vec3(0,0,-1), block.TORCH.withData(Torch.NORTH)))

		self.add_layer(BuildingLayer(layer_blocks, 3))
		del layer_blocks[:]

		#######################################################################
		# level 5
		# west roof & gable
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['South West'] + Vec3(1,0,-1), 
										block.WOOD_PLANKS, 
										LargeHouse.WALLS_CORNER_POS['North West'] + Vec3(1,0,0), 
										description="West roof rafters"))
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['South West'] + Vec3(0,0,-1), 
										block.WOOD_PLANKS, 
										LargeHouse.WALLS_CORNER_POS['South West'] + Vec3(0,0,-4), 
										description="West roof gable"))
		layer_blocks.append(Stair(LargeHouse.WALLS_CORNER_POS['South West'] + Vec3(0,0,-5), 
								block.STAIRS_WOOD.withData(Stair.EAST), 
								LargeHouse.WALLS_CORNER_POS['North West'], 
								description="West roof"))

		# north gable window
		layer_blocks.append(BuildingBlock(LargeHouse.NORTH_WIN_SPAN[0], block.WOOD, 
										LargeHouse.NORTH_WIN_SPAN[1], 
										description=LargeHouse.NORTH_WIN_SPAN[2] + " frame"))
		layer_blocks.append(BuildingBlock(LargeHouse.NORTH_WIN_SPAN[0] + Vec3(-1,0,0), block.GLASS_PANE, 
										LargeHouse.NORTH_WIN_SPAN[1] + Vec3(1,0,0), 
										description=LargeHouse.NORTH_WIN_SPAN[2]))

		# east rafters & gable
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['North East'] + Vec3(-1,0,0), 
										block.WOOD_PLANKS, 
										LargeHouse.WALLS_CORNER_POS['East mid west'] + Vec3(-1,0,1), 
										description="East roof rafters"))
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['East mid west'] + Vec3(-1,0,1), 
										block.WOOD_PLANKS, 
										LargeHouse.WALLS_CORNER_POS['East mid east'] + Vec3(0,0,1), 
										description="East roof extension rafters"))
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['East mid west'], 
										block.WOOD_PLANKS, 
										description="East roof extension corner rafter"))
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['East mid east'] + Vec3(0,0,1), 
										block.WOOD_PLANKS, 
										LargeHouse.WALLS_CORNER_POS['South East'] + Vec3(0,0,-1), 
										description="East gable"))
		# east roof
		layer_blocks.append(Stair(LargeHouse.WALLS_CORNER_POS['North East'], 
								block.STAIRS_WOOD.withData(Stair.WEST), 
								LargeHouse.WALLS_CORNER_POS['East mid west'] + Vec3(0,0,-1), 
								description="East roof"))
		layer_blocks.append(Stair(LargeHouse.WALLS_CORNER_POS['East mid west'] + Vec3(1,0,0), 
								block.STAIRS_WOOD.withData(Stair.SOUTH), 
								LargeHouse.WALLS_CORNER_POS['East mid east'], 
								description="East roof extension"))

		# south roof
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['South West'] + Vec3(0,0,-1), 
										block.WOOD_PLANKS, 
										LargeHouse.WALLS_CORNER_POS['South East'] + Vec3(0,0,-1), 
										description="South roof rafters"))
		layer_blocks.append(Stair(LargeHouse.WALLS_CORNER_POS['South West'], 
								block.STAIRS_WOOD.withData(Stair.NORTH), 
								LargeHouse.WALLS_CORNER_POS['South East'], 
								description="South roof"))


		self.add_layer(BuildingLayer(layer_blocks, 4))
		del layer_blocks[:]

		#######################################################################
		# level 6
		# rafters
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['South West'] + Vec3(0,0,-2), 
										block.WOOD_PLANKS, 
										LargeHouse.WALLS_CORNER_POS['South East'] + Vec3(0,0,-3), 
										description="West to east roof rafters & gables"))
		
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['South West'] + Vec3(2,0,-4), 
										block.WOOD_PLANKS, 
										LargeHouse.WALLS_CORNER_POS['North West'] + Vec3(2,0,0), 
										description="West rafters"))
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['South West'] + Vec3(4,0,-4), 
										block.WOOD_PLANKS, 
										LargeHouse.WALLS_CORNER_POS['North West'] + Vec3(4,0,0), 
										description="East rafters"))
		
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['South West'] + Vec3(1,0,-4), 
										block.WOOD_PLANKS,  
										description="West roof rafter corner"))
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['South West'] + Vec3(5,0,-4), 
										block.WOOD_PLANKS,  
										description="East roof rafter corner"))
		
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['North West'] + Vec3(3,0,0), 
										block.WOOD_PLANKS, 
										description="North gable"))

		# roof
		layer_blocks.append(Stair(LargeHouse.WALLS_CORNER_POS['South West'] + Vec3(0,0,-4), 
								block.STAIRS_WOOD.withData(Stair.SOUTH), 
								description="West roof north facing"))
		layer_blocks.append(Stair(LargeHouse.WALLS_CORNER_POS['South West'] + Vec3(1,0,-5), 
								block.STAIRS_WOOD.withData(Stair.EAST), 
								LargeHouse.WALLS_CORNER_POS['North West'] + Vec3(1,0,0), 
								description="West roof"))
		
		layer_blocks.append(Stair(LargeHouse.WALLS_CORNER_POS['North East'] + Vec3(-1,0,0), 
								block.STAIRS_WOOD.withData(Stair.WEST), 
								LargeHouse.WALLS_CORNER_POS['North East'] + Vec3(-1,0,5), 
								description="East roof"))
		layer_blocks.append(Stair(LargeHouse.WALLS_CORNER_POS['East mid east'] + Vec3(0,0,1), 
								block.STAIRS_WOOD.withData(Stair.SOUTH), 
								LargeHouse.WALLS_CORNER_POS['East mid east'] + Vec3(-2,0,1), 
								description="east roof north facing"))
		
		layer_blocks.append(Stair(LargeHouse.WALLS_CORNER_POS['South West'] + Vec3(0,0,-1), 
								block.STAIRS_WOOD.withData(Stair.NORTH), 
								LargeHouse.WALLS_CORNER_POS['South East'] + Vec3(0,0,-1),
							    description="South roof"))

		self.add_layer(BuildingLayer(layer_blocks, 5))
		del layer_blocks[:]

		#######################################################################
		# level 7
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['South West'] + Vec3(2,0,-3), 
										block.WOOD_PLANKS, 
										LargeHouse.WALLS_CORNER_POS['South West'] + Vec3(4,0,-3), 
										description="East - west rafters"))
		layer_blocks.append(BuildingBlock(LargeHouse.WALLS_CORNER_POS['North West'] + Vec3(3,0,0), 
										block.WOOD_PLANKS, 
										LargeHouse.WALLS_CORNER_POS['North West'] + Vec3(3,0,6), 
										description="North - south rafters"))

		layer_blocks.append(Stair(LargeHouse.WALLS_CORNER_POS['South West'] + Vec3(0,0,-3), 
								block.STAIRS_WOOD.withData(Stair.SOUTH), 
								LargeHouse.WALLS_CORNER_POS['South West'] + Vec3(1,0,-3), 
								description="West roof north facing"))
		layer_blocks.append(Stair(LargeHouse.WALLS_CORNER_POS['North West'] + Vec3(2,0,0), 
								block.STAIRS_WOOD.withData(Stair.EAST), 
								LargeHouse.WALLS_CORNER_POS['North West'] + Vec3(2,0,6), 
								description="West roof"))

		layer_blocks.append(Stair(LargeHouse.WALLS_CORNER_POS['North West'] + Vec3(4,0,0), 
								block.STAIRS_WOOD.withData(Stair.WEST), 
								LargeHouse.WALLS_CORNER_POS['North West'] + Vec3(4,0,6), 
								description="East roof"))
		layer_blocks.append(Stair(LargeHouse.WALLS_CORNER_POS['South East'] + Vec3(0,0,-3), 
								block.STAIRS_WOOD.withData(Stair.SOUTH), 
								LargeHouse.WALLS_CORNER_POS['South East'] + Vec3(-3,0,-3), 
								description="east roof north facing"))

		layer_blocks.append(Stair(LargeHouse.WALLS_CORNER_POS['South West'] + Vec3(0,0,-2), 
								block.STAIRS_WOOD.withData(Stair.NORTH), 
								LargeHouse.WALLS_CORNER_POS['South East'] + Vec3(0,0,-2), 
								description="South roof"))

		self.add_layer(BuildingLayer(layer_blocks, 6))
		del layer_blocks[:]


		#######################################################################
		self._set_orientation()
		
	def build(self, mc):
		super(LargeHouse, self).build(mc)

