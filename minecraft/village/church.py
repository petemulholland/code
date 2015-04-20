from building import Building, BuildingLayer, BuildingBlock
from oriented_blocks import Torch, Stair, Ladder, Door
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

class Church(Building):
	"""description of class"""
	# todo rework this based on the 4 corners & east & west mid points.

	BASE_SPAN  = (Building.SE_CORNER_POS + Vec3(-3,0,-1), 
					Building.SE_CORNER_POS + Vec3(-1,0,-9)) 
	
	WALL_S_SPAN = (Building.SE_CORNER_POS + Vec3(-3,0,-1), 
					Building.SE_CORNER_POS + Vec3(-1,0,-1))
	WALL_TN_SPAN = (Building.SE_CORNER_POS + Vec3(-3,0,-5), 
					Building.SE_CORNER_POS + Vec3(-1,0,-5)) # Tower Wall north section
	WALL_N_SPAN = (Building.SE_CORNER_POS + Vec3(-3,0,-9), 
					Building.SE_CORNER_POS + Vec3(-1,0,-9))
	
	WALL_SW_SPAN = (Building.SE_CORNER_POS + Vec3(-4,0,-2), 
					Building.SE_CORNER_POS + Vec3(-4,0,-4)) # SW wall sections
	WALL_NW_SPAN = (Building.SE_CORNER_POS + Vec3(-4,0,-6), 
					Building.SE_CORNER_POS + Vec3(-4,0,-8))
	WALL_W_SPAN = (Building.SE_CORNER_POS + Vec3(-4,0,-2), 
					Building.SE_CORNER_POS + Vec3(-4,0,-8))
	WALL_SE_SPAN = (Building.SE_CORNER_POS + Vec3(0,0,-2), 
					Building.SE_CORNER_POS + Vec3(0,0,-4))
	WALL_NE_SPAN = (Building.SE_CORNER_POS + Vec3(0,0,-6), 
					Building.SE_CORNER_POS + Vec3(0,0,-8))
	WALL_E_SPAN = (Building.SE_CORNER_POS + Vec3(0,0,-2), 
					Building.SE_CORNER_POS + Vec3(0,0,-8))
	

	WALL_MID_POS = (Building.SE_CORNER_POS + Vec3(-4,0,-5), 
					Building.SE_CORNER_POS + Vec3(0,0,-5))
	
	DOOR_POS = Building.SE_CORNER_POS + Vec3(-2,0,-1)
	LADDER_POS = Building.SE_CORNER_POS + Vec3(-3,0,-4)
	
	WINS_S_POS = (Building.SE_CORNER_POS + Vec3(-4,0,-3), 
					Building.SE_CORNER_POS + Vec3(0,0,-3)) # south window positions
	WINS_N_POS = (Building.SE_CORNER_POS + Vec3(-4,0,-7), 
					Building.SE_CORNER_POS + Vec3(-2,0,-9), 
					Building.SE_CORNER_POS + Vec3(0,0,-7)) # north window positions
	
	ROOF_SPAN = (Building.SE_CORNER_POS + Vec3(-3,0,-6), 
					Building.SE_CORNER_POS + Vec3(-1,0,-8))
	TOWER_FLOOR_SPAN = (Building.SE_CORNER_POS + Vec3(-3,0,-2), 
						Building.SE_CORNER_POS + Vec3(-1,0,-4))
	TOWER_WIN_POS = (Building.SE_CORNER_POS + Vec3(-4,0,-3), 
					Building.SE_CORNER_POS + Vec3(0,0,-3), 
					Building.SE_CORNER_POS + Vec3(-2,0,-1), 
					Building.SE_CORNER_POS + Vec3(-2,0,-5))

	

	WIDTH = 5
	def __init__(self, *args, **kwargs):
		super(Church, self).__init__(width=Church.WIDTH, *args, **kwargs)

		ladder = Ladder(Church.LADDER_POS, block.LADDER.withData(Ladder.WEST)
														, description="Ladder on west side of block")


		layer_blocks = []
		#######################################################################
		# level 1
		layer_blocks.append(BuildingBlock(Church.BASE_SPAN[0], 
										block.COBBLESTONE, Church.BASE_SPAN[1],
										description="Base"))
		layer_blocks.append(BuildingBlock(Church.WALL_NW_SPAN[0], 
										block.COBBLESTONE, Church.WALL_NW_SPAN[1],
										description="West Wall base"))
		layer_blocks.append(BuildingBlock(Church.WALL_NE_SPAN[0], 
										block.COBBLESTONE, Church.WALL_NE_SPAN[1],
										description="East Wall base"))
		layer_blocks.append(Stair(Church.DOOR_POS + Vec3(0,0,1), 
								block.STAIRS_COBBLESTONE.withData(Stair.NORTH),
								description="Front Stair"))

		self.add_layer(BuildingLayer(layer_blocks, 0))
		del layer_blocks[:]

		#######################################################################
		# common blocks
		walls = []
		walls.append(BuildingBlock(Church.WALL_W_SPAN[0], 
									block.COBBLESTONE, Church.WALL_W_SPAN[1],
									description="Full west wall"))
		walls.append(BuildingBlock(Church.WALL_N_SPAN[0], 
									block.COBBLESTONE, Church.WALL_N_SPAN[1],
									description="North wall"))
		walls.append(BuildingBlock(Church.WALL_E_SPAN[0], 
									block.COBBLESTONE, Church.WALL_E_SPAN[1],
									description="Full East wall"))
		walls.append(BuildingBlock(Church.WALL_S_SPAN[0], 
									block.COBBLESTONE, Church.WALL_S_SPAN[1],
									description="South wall"))
		walls.append(ladder)

		#######################################################################
		# level 2
		layer_blocks.extend(walls)
		layer_blocks.append(BuildingBlock(Church.DOOR_POS,  block.AIR,
									description="Clearing Door"))


		layer_blocks.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-3,0,-7), 
										block.COBBLESTONE, 
										Building.SE_CORNER_POS + Vec3(-1,0,-8),
										description="Altar base"))
		layer_blocks.append(Stair(Building.SE_CORNER_POS + Vec3(-3,0,-6), 
								block.STAIRS_COBBLESTONE.withData(Stair.NORTH),
								description="West Stair, facing north"))
		layer_blocks.append(Stair(Building.SE_CORNER_POS + Vec3(-2,0,-7), 
								block.STAIRS_COBBLESTONE.withData(Stair.NORTH),
									description="Center Stair, facing north"))
		layer_blocks.append(Stair(Building.SE_CORNER_POS + Vec3(-1,0,-6), 
								block.STAIRS_COBBLESTONE.withData(Stair.NORTH),
									description="East Stair, facing north"))

		self.add_layer(BuildingLayer(layer_blocks, 1))
		del layer_blocks[:]

		#######################################################################
		# level 3
		layer_blocks.extend(walls)
		layer_blocks.append(BuildingBlock(Church.DOOR_POS,  block.AIR,
									description="Clearing Door"))

		layer_blocks.append(Stair(Building.SE_CORNER_POS + Vec3(-3,0,-8), 
								block.STAIRS_COBBLESTONE.withData(Stair.WEST),
									description="West stair, facing west"))
		layer_blocks.append(Stair(Building.SE_CORNER_POS + Vec3(-1,0,-8), 
								block.STAIRS_COBBLESTONE.withData(Stair.EAST),
									description="East stair, facing east"))

		for pos in Church.WINS_S_POS:
			layer_blocks.append(BuildingBlock(pos, block.GLASS_PANE,
									description="Glass pane, south"))
		
		self.add_layer(BuildingLayer(layer_blocks, 2))
		del layer_blocks[:]
		
		#######################################################################
		# level 4
		layer_blocks.extend(walls)
		for pos in Church.WINS_S_POS:
			layer_blocks.append(BuildingBlock(pos, block.GLASS_PANE,
									description="Glass pane, south"))
		for pos in Church.WINS_N_POS:
			layer_blocks.append(BuildingBlock(pos, block.GLASS_PANE,
									description="Glass pane, north"))

		self.add_layer(BuildingLayer(layer_blocks, 3))
		del layer_blocks[:]
		
		#######################################################################
		# level 5
		# insert the tower floor before the ladder in the walls list here
		walls.insert(4, BuildingBlock(Church.TOWER_FLOOR_SPAN[0], 
										block.COBBLESTONE, Church.TOWER_FLOOR_SPAN[1],
										description="Tower floor"))
		layer_blocks.extend(walls)
		layer_blocks.append(BuildingBlock(Church.WALL_TN_SPAN[0], 
										block.COBBLESTONE, Church.WALL_TN_SPAN[1],
									description="Tower north wall"))
		layer_blocks.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-4,0,-1),  
									block.COBBLESTONE,
									description="Filling south west corner"))
		layer_blocks.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(0,0,-1),  
									block.COBBLESTONE,
									description="Filling south east corner"))

		layer_blocks.append(Torch(Building.SE_CORNER_POS + Vec3(-1,0,-7), 
								block.TORCH.withData(Torch.WEST),
								description="East wall torch facing west"))
		layer_blocks.append(Torch(Building.SE_CORNER_POS + Vec3(-2,0,-6), 
								block.TORCH.withData(Torch.NORTH),
								description="South wall torch facing north"))
		layer_blocks.append(Torch(Building.SE_CORNER_POS + Vec3(-3,0,-7), 
								block.TORCH.withData(Torch.EAST),
								description="West wall torch facing east"))
		layer_blocks.append(Torch(Building.SE_CORNER_POS + Vec3(-2,0,-8), 
								block.TORCH.withData(Torch.SOUTH),
								description="North wall torch facing south"))

		self.add_layer(BuildingLayer(layer_blocks, 4))
		del layer_blocks[:]
		
		# reset walls for tower
		del walls[:]
		walls.append(BuildingBlock(Church.WALL_SW_SPAN[0], 
									block.COBBLESTONE, Church.WALL_SW_SPAN[1],
									description="Tower west wall"))
		walls.append(BuildingBlock(Church.WALL_TN_SPAN[0], 
									block.COBBLESTONE, Church.WALL_TN_SPAN[1],
									description="Tower north wall"))
		walls.append(BuildingBlock(Church.WALL_SE_SPAN[0], 
									block.COBBLESTONE, Church.WALL_SE_SPAN[1],
									description="Tower east wall"))
		walls.append(BuildingBlock(Church.WALL_S_SPAN[0], 
									block.COBBLESTONE, Church.WALL_S_SPAN[1],
									description="Tower south wall"))
		walls.append(ladder)

		# level 6
		layer_blocks.extend(walls)
		layer_blocks.append(BuildingBlock(Church.ROOF_SPAN[0], 
										block.COBBLESTONE, Church.ROOF_SPAN[1],
										description="Northern roof span"))

		self.add_layer(BuildingLayer(layer_blocks, 5))
		del layer_blocks[:]
		
		# levels 7 & 8 are same
		layer_blocks.extend(walls)
		for pos in Church.TOWER_WIN_POS:
			layer_blocks.append(BuildingBlock(pos, block.GLASS_PANE,
									description="Tower window"))

		self.add_layer(BuildingLayer(layer_blocks, 6))
		self.add_layer(BuildingLayer(layer_blocks, 7))
		del layer_blocks[:]
		
		# level 9
		# nothing to add here just tower walls
		self.add_layer(BuildingLayer(walls, 8))
		
		# level 10
		# insert floor into walls here before ladder
		# fill corners of tower at this level
		walls.insert(4, BuildingBlock(Church.TOWER_FLOOR_SPAN[0], 
										block.COBBLESTONE, Church.TOWER_FLOOR_SPAN[1],
										description="Tower floor"))

		self.add_layer(BuildingLayer(walls, 9))
		
		# level 11
		# remove floor & ladder at his level.
		walls = walls[:4]
		self.add_layer(BuildingLayer(walls, 10))
		
		# level 12
		for pos in Church.TOWER_WIN_POS:
			layer_blocks.append(BuildingBlock(pos, block.COBBLESTONE,
											description="Tower crenellation"))

		self.add_layer(BuildingLayer(layer_blocks, 11))
		del layer_blocks[:]


		# add the door
		self.add_block(Door(None, 
							Vec3(Church.DOOR_POS.x, 1, Church.DOOR_POS.z), 
							block.DOOR_WOOD.withData(Door.SOUTH)))

		self._set_orientation()
		
