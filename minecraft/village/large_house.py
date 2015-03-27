from building import Building, BuildingLayer, BuildingBlock
from oriented_blocks import Torch, Stair
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

class LargeHouse(Building):
	"""description of class"""
	
	WEST_WALL_SPAN = (Vec3(-4,0,-2), Vec3(-4,0,-12))
	NORTH_WALL_SPAN = (Vec3(-4,0,-12), Vec3(2,0,-12))
	EAST_WALL_N_SPAN = (Vec3(2,0,-12), Vec3(2,0,-7))
	EAST_WALL_E_SPAN = (Vec3(2,0,-7), Vec3(4,0,-7))
	EAST_WALL_S_SPAN = (Vec3(4,0,-7), Vec3(4,0,-2))
	SOUTH_WALL_SPAN = (Vec3(-4,0,-2), Vec3(4,0,-2))

	FLOOR_SPANs = ((Vec3(-3,0,-3), Vec3(1,0,-11)), (Vec3(2,0,-3), Vec3(3,0,-6)))
	STEP_POS = Vec3(2,0,-1)
	DOOR_POS = Vec3(2,0,-2)



	def __init__(self, *args, **kwargs):
		super(LargeHouse, self).__init__(*args, **kwargs)

		offset = self.build_pos

		layer_blocks = []
		walls = []
		# level 1
		walls.append(BuildingBlock(offset, LargeHouse.WEST_WALL_SPAN[0], 
									block.COBBLESTONE, LargeHouse.WEST_WALL_SPAN[1],
									description="West wall"))
		walls.append(BuildingBlock(offset, LargeHouse.NORTH_WALL_SPAN[0], 
									block.COBBLESTONE, LargeHouse.NORTH_WALL_SPAN[1],
									description="North wall"))
		walls.append(BuildingBlock(offset, LargeHouse.EAST_WALL_N_SPAN[0], 
									block.COBBLESTONE, LargeHouse.EAST_WALL_N_SPAN[1],
									description="East wall, north section"))
		walls.append(BuildingBlock(offset, LargeHouse.EAST_WALL_E_SPAN[0], 
									block.COBBLESTONE, LargeHouse.EAST_WALL_E_SPAN[1],
									description="East wall, extension"))
		walls.append(BuildingBlock(offset, LargeHouse.EAST_WALL_S_SPAN[0], 
									block.COBBLESTONE, LargeHouse.EAST_WALL_S_SPAN[1],
									description="East wall, south section"))
		walls.append(BuildingBlock(offset, LargeHouse.SOUTH_WALL_SPAN[0], 
									block.COBBLESTONE, LargeHouse.SOUTH_WALL_SPAN[1],
									description="South wall"))

		layer_blocks.extend(walls)

		for floor_span in FLOOR_SPANS:
			layer_blocks.append(BuildingBlock(offset, LargeHouse.floor_span[0], 
											block.WOOD_PLANKS, LargeHouse.floor_span[1],
											description="Floor"))


		layer_blocks.append(Stair(offset, LargeHouse.STEP_POS, 
								block.STAIRS_COBBLESTONE.withData(Stair.NORTH),
								description="Front Stair"))

		self.layers.append(BuildingLayer(layer_blocks, 0))
		del layer_blocks[:]

		# level 2
		layer_blocks.extend(walls)
		# Clear door space
		layer_blocks.append(BuildingBlock(offset, LargeHouse.DOOR_POS, 
										block.AIR, description="Floor"))

		self.layers.append(BuildingLayer(layer_blocks, 1))
		del layer_blocks[:]

		# level 3
		# west wall
		layer_blocks.append(BuildingBlock(offset, Vec3(-4,0,-2),
										block.COBBLESTONE, description="West wall, south corner"))
		layer_blocks.append(BuildingBlock(offset, Vec3(-4,0,-3),
										block.WOOD, description="West wall, window frame"))
		layer_blocks.append(BuildingBlock(offset, Vec3(-4,0,-6),
										block.WOOD, description="West wall, window frame"))
		layer_blocks.append(BuildingBlock(offset, Vec3(-4,0,-7),
										block.WOOD_PLANKS, description="West wall, wall section"))
		layer_blocks.append(BuildingBlock(offset, Vec3(-4,0,-8),
										block.WOOD, description="West wall, window frame"))
		layer_blocks.append(BuildingBlock(offset, Vec3(-4,0,-11),
										block.WOOD, description="West wall, window frame"))
		# insert the windows after frames have been built
		layer_blocks.append(BuildingBlock(offset, Vec3(-4,0,-4),
										block.GLASS_PANE, Vec3(-4,0,-5),
										description="West wall, south window"))
		layer_blocks.append(BuildingBlock(offset, Vec3(-4,0,-9),
										block.GLASS_PANE, Vec3(-4,0,-10),
										description="West wall, north window"))
		# north wall
		layer_blocks.append(BuildingBlock(offset, LargeHouse.NORTH_WALL_SPAN[0], 
									block.COBBLESTONE, LargeHouse.NORTH_WALL_SPAN[1],
									description="North wall"))
		
		# east wall
		layer_blocks.append(BuildingBlock(offset, Vec3(4,0,-2),
										block.COBBLESTONE, description="East wall, south corner"))
		layer_blocks.append(BuildingBlock(offset, Vec3(4,0,-3),
										block.WOOD, description="East wall, window frame"))
		layer_blocks.append(BuildingBlock(offset, Vec3(4,0,-6),
										block.WOOD, description="East wall, window frame"))
		layer_blocks.append(BuildingBlock(offset, Vec3(4,0,-7),
										block.WOOD_PLANKS, description="East wall, corner"))
		layer_blocks.append(BuildingBlock(offset, Vec3(3,0,-7),
										block.WOOD_PLANKS, Vec3(2,0,-7),
										description="East wall, wall section"))
		layer_blocks.append(BuildingBlock(offset, Vec3(2,0,-8),
										block.WOOD, description="East wall, window frame"))
		layer_blocks.append(BuildingBlock(offset, Vec3(2,0,-11),
										block.WOOD, description="East wall, window frame"))
		# insert the windows after frames have been built
		layer_blocks.append(BuildingBlock(offset, Vec3(2,0,-9),
										block.GLASS_PANE, Vec3(-4,0,-10),
										description="East wall, north window"))
		layer_blocks.append(BuildingBlock(offset, Vec3(4,0,-4),
										block.GLASS_PANE, Vec3(-4,0,-5),
										description="East wall, south window"))
		# south wall
		layer_blocks.append(BuildingBlock(offset, Vec3(3,0,-2),
										block.WOOD_PLANKS, description="South wall, door frame"))
		layer_blocks.append(BuildingBlock(offset, Vec3(1,0,-2),
										block.WOOD_PLANKS, description="South wall, door frame"))
		layer_blocks.append(BuildingBlock(offset, Vec3(0,0,-2),
										block.WOOD, description="South wall, window frame"))
		layer_blocks.append(BuildingBlock(offset, Vec3(-2,0,-2),
										block.WOOD, description="South wall, window frame"))
		layer_blocks.append(BuildingBlock(offset, Vec3(-3,0,-2),
										block.WOOD, description="South wall, wall section"))
		# insert the windows after frames have been built
		layer_blocks.append(BuildingBlock(offset, Vec3(-1,0,-2),
										block.GLASS_PANE, description="South wall, window"))

		self.layers.append(BuildingLayer(layer_blocks, 2))
		del layer_blocks[:]

		# level 4
		# walls
		layer_blocks.append(BuildingBlock(offset, LargeHouse.WEST_WALL_SPAN[0], 
										block.COBBLESTONE, LargeHouse.WEST_WALL_SPAN[1],
										description="West wall"))
		layer_blocks.append(BuildingBlock(offset, LargeHouse.NORTH_WALL_SPAN[0], 
										block.COBBLESTONE, LargeHouse.NORTH_WALL_SPAN[1],
										description="North wall"))
		layer_blocks.append(BuildingBlock(offset, LargeHouse.EAST_WALL_N_SPAN[0], 
										block.COBBLESTONE, LargeHouse.EAST_WALL_N_SPAN[1],
										description="East wall, north section"))
		layer_blocks.append(BuildingBlock(offset, LargeHouse.EAST_WALL_E_SPAN[0], 
										block.WOOD_PLANKS, LargeHouse.EAST_WALL_E_SPAN[1] + Vec3(-1,0,0),
										description="East wall, extension"))
		layer_blocks.append(BuildingBlock(offset, LargeHouse.EAST_WALL_S_SPAN[0], 
										block.COBBLESTONE, LargeHouse.EAST_WALL_S_SPAN[1],
										description="East wall, south section"))
		
		layer_blocks.append(BuildingBlock(offset, LargeHouse.SOUTH_WALL_SPAN[0] + Vec3(1,0,0), 
										block.WOOD_PLANKS, LargeHouse.SOUTH_WALL_SPAN[1] + Vec3(-1,0,0),
										description="South wall"))

		# roof eaves
		layer_blocks.append(Stair(offset, LargeHouse.SOUTH_WALL_SPAN[0] + Vec3(0,0,1), 
								block.STAIRS_WOOD.withData(Stair.NORTH), 
								LargeHouse.SOUTH_WALL_SPAN[1] + Vec3(0,0,1),
								description="South roof eaves"))

		layer_blocks.append(Stair(offset, LargeHouse.EAST_WALL_N_SPAN[0] + Vec3(1,0,0), 
								block.STAIRS_WOOD.withData(Stair.WEST), 
								LargeHouse.EAST_WALL_N_SPAN[1] + Vec3(1,0,0),
								description="East roof eaves, west facing"))
		layer_blocks.append(BuildingBlock(offset, Vec3(3,0,-8), 
										block.WOOD_PLANKS, description="East roof eaves corner"))
		layer_blocks.append(Stair(offset, Vec3(4,0,-8), 
								block.STAIRS_WOOD.withData(Stair.SOUTH), 
								description="East roof eaves, north facing"))
		layer_blocks.append(Torch(offset, LargeHouse.DOOR_POS + Vec3(0,0,-1), block.TORCH.withData(Torch.NORTH)))

		self.layers.append(BuildingLayer(layer_blocks, 3))
		del layer_blocks[:]

		# level 5
		# west roof & gable
		layer_blocks.append(BuildingBlock(offset, Vec3(-3,0,-3), 
										block.WOOD_PLANKS, Vec3(-3,0,-12), 
										description="West roof rafters"))
		layer_blocks.append(BuildingBlock(offset, Vec3(-4,0,-3), 
										block.WOOD_PLANKS, Vec3(-4,0,-6), 
										description="West roof gable"))
		layer_blocks.append(Stair(offset, Vec3(-4,0,-7), 
								block.STAIRS_WOOD.withData(Stair.EAST), Vec3(-4,0,-12), 
								description="West roof"))

		# north gable window
		layer_blocks.append(BuildingBlock(offset, Vec3(-2,0,-12),
										block.WOOD, description="North wall, gable window frame"))
		layer_blocks.append(BuildingBlock(offset, Vec3(-4,0,-12),
										block.WOOD, description="North wall, gable window frame"))
		# insert the windows after frames have been built
		layer_blocks.append(BuildingBlock(offset, Vec3(-3,0,-12),
										block.GLASS_PANE, description="North wall, gable window"))

		# east roof & gable
		layer_blocks.append(BuildingBlock(offset, Vec3(1,0,-12), 
										block.WOOD_PLANKS, Vec3(1,0,-6), 
										description="East roof rafters"))
		layer_blocks.append(BuildingBlock(offset, Vec3(1,0,-6), 
										block.WOOD_PLANKS, Vec3(4,0,-6), 
										description="East roof extension rafters"))
		layer_blocks.append(BuildingBlock(offset, Vec3(2,0,-7), 
										block.WOOD_PLANKS, 
										description="East roof extension corner rafter"))
		layer_blocks.append(BuildingBlock(offset, Vec3(4,0,-6), 
										block.WOOD_PLANKS, Vec3(4,0,-3), 
										description="East roof gable"))
		layer_blocks.append(Stair(offset, Vec3(2,0,-12), 
								block.STAIRS_WOOD.withData(Stair.WEST), Vec3(2,0,-8), 
								description="East roof"))
		layer_blocks.append(Stair(offset, Vec3(3,0,-7), 
								block.STAIRS_WOOD.withData(Stair.SOUTH), Vec3(4,0,-7), 
								description="East roof extension"))

		# south roof
		layer_blocks.append(BuildingBlock(offset, Vec3(-4,0,-3), 
										block.WOOD_PLANKS, Vec3(4,0,-3), 
										description="South roof rafters"))
		layer_blocks.append(Stair(offset, Vec3(-4,0,-2), 
								block.STAIRS_WOOD.withData(Stair.NORTH), Vec3(4,0,-2), 
								description="South roof"))


		self.layers.append(BuildingLayer(layer_blocks, 4))
		del layer_blocks[:]

		# level 6
		# rafters
		layer_blocks.append(BuildingBlock(offset, Vec3(-4,0,-4), 
										block.WOOD_PLANKS, Vec3(4,0,-5), 
										description="West to east roof rafters & gables"))
		layer_blocks.append(BuildingBlock(offset, Vec3(-2,0,-6), 
										block.WOOD_PLANKS, Vec3(-2,0,-11), 
										description="West rafters"))
		layer_blocks.append(BuildingBlock(offset, Vec3(0,0,-11), 
										block.WOOD_PLANKS, Vec3(0,0,-6), 
										description="East rafters"))
		layer_blocks.append(BuildingBlock(offset, Vec3(-3,0,-6), 
										block.WOOD_PLANKS,  
										description="West roof rafter corner"))
		layer_blocks.append(BuildingBlock(offset, Vec3(1,0,-6), 
										block.WOOD_PLANKS,  
										description="East roof rafter corner"))
		layer_blocks.append(BuildingBlock(offset, Vec3(-2,0,-12), 
										block.WOOD_PLANKS, Vec3(0,0,-12), 
										description="North gable"))

		# roof
		layer_blocks.append(Stair(offset, Vec3(-4,0,-6), 
								block.STAIRS_WOOD.withData(Stair.SOUTH), 
								description="West roof north facing"))
		layer_blocks.append(Stair(offset, Vec3(-3,0,-7), 
								block.STAIRS_WOOD.withData(Stair.EAST), 
								Vec3(-3,0,-12), description="West roof"))
		layer_blocks.append(Stair(offset, Vec3(1,0,-12), 
								block.STAIRS_WOOD.withData(Stair.WEST), 
								Vec3(1,0,-7), description="East roof"))
		layer_blocks.append(Stair(offset, Vec3(2,0,-6), 
								block.STAIRS_WOOD.withData(Stair.SOUTH), 
								Vec3(4,0,-6), description="east roof north facing"))
		layer_blocks.append(Stair(offset, Vec3(-4,0,-3), 
								block.STAIRS_WOOD.withData(Stair.NORTH), 
								Vec3(4,0,-3), description="South roof"))

		self.layers.append(BuildingLayer(layer_blocks, 5))
		del layer_blocks[:]

		# level 7
		layer_blocks.append(BuildingBlock(offset, Vec3(-2,0,-5), 
										block.WOOD_PLANKS, Vec3(0,0,-5), 
										description="East - west rafters"))
		layer_blocks.append(BuildingBlock(offset, Vec3(-1,0,-6), 
										block.WOOD_PLANKS, Vec3(-1,0,-12), 
										description="North - south rafters"))

		layer_blocks.append(Stair(offset, Vec3(-4,0,-5), 
								block.STAIRS_WOOD.withData(Stair.SOUTH), 
								Vec3(-3,0,-5), description="West roof north facing"))
		layer_blocks.append(Stair(offset, Vec3(-2,0,-6), 
								block.STAIRS_WOOD.withData(Stair.EAST), 
								Vec3(-2,0,-12), description="West roof"))
		layer_blocks.append(Stair(offset, Vec3(0,0,-12), 
								block.STAIRS_WOOD.withData(Stair.WEST), 
								Vec3(0,0,-6), description="East roof"))
		layer_blocks.append(Stair(offset, Vec3(1,0,-5), 
								block.STAIRS_WOOD.withData(Stair.SOUTH), 
								Vec3(4,0,-5), description="east roof north facing"))
		layer_blocks.append(Stair(offset, Vec3(-4,0,-4), 
								block.STAIRS_WOOD.withData(Stair.NORTH), 
								Vec3(4,0,-5), description="South roof"))

		self.layers.append(BuildingLayer(layer_blocks, 6))
		del layer_blocks[:]


		self._set_orientation()
		
	def build(self, mc):
		super(LargeHouse, self).build(mc)

