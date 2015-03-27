from building import Building, BuildingLayer, BuildingBlock
from oriented_blocks import Torch, Stair, Ladder
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

class Church(Building):
	"""description of class"""
	
	BASE_SPAN  = (Vec3(-1,0,-1), Vec3(1,0,-9)) 
	
	WALL_S_SPAN = (Vec3(-1,0,-1), Vec3(1,0,-1))
	WALL_TN_SPAN = (Vec3(-1,0,-5), Vec3(1,0,-5)) # Tower Wall north section
	WALL_N_SPAN = (Vec3(-1,0,-9), Vec3(1,0,-9))
	
	WALL_SW_SPAN = (Vec3(-2,0,-2), Vec3(-2,0,-4)) # SW wall sections
	WALL_NW_SPAN = (Vec3(-2,0,-6), Vec3(-2,0,-8))
	WALL_W_SPAN = (Vec3(-2,0,-2), Vec3(-2,0,-8))
	WALL_SE_SPAN = (Vec3(2,0,-2), Vec3(2,0,-4))
	WALL_NE_SPAN = (Vec3(2,0,-6), Vec3(2,0,-8))
	WALL_E_SPAN = (Vec3(2,0,-2), Vec3(2,0,-8))
	

	WALL_MID_POS = (Vec3(-2,0,-5), Vec3(2,0,-5))
	
	DOOR_POS = Vec3(0,0,-1)
	LADDER_POS = Vec3(-1,0,-4)
	
	WINS_S_POS = (Vec3(-2,0,-3), Vec3(2,0,-3)) # south window positions
	WINS_N_POS = (Vec3(-2,0,-7), Vec3(0,0,-9), Vec3(2,0,-7)) # north window positions
	
	ROOF_SPAN = (Vec3(-1,0,-6), Vec3(1,0,-8))
	TOWER_FLOOR_SPAN = (Vec3(-1,0,-2), Vec3(1,0,-4))
	TOWER_WIN_POS = (Vec3(-2,0,-3), Vec3(2,0,-3), Vec3(0,0,-1), Vec3(0,0,-5))

	

	def __init__(self, *args, **kwargs):
		super(Church, self).__init__(*args, **kwargs)

		offset = self.build_pos

		ladder = Ladder(offset, Church.LADDER_POS, block.LADDER.withData(Ladder.WEST), description="Ladder")


		layer_blocks = []
		# level 1
		layer_blocks.append(BuildingBlock(offset, Church.BASE_SPAN[0], 
										block.COBBLESTONE, Church.BASE_SPAN[1],
										description="Base"))
		layer_blocks.append(BuildingBlock(offset, Church.WALL_NW_SPAN[0], 
										block.COBBLESTONE, Church.WALL_NW_SPAN[1],
										description="NW Wall"))
		layer_blocks.append(BuildingBlock(offset, Church.WALL_NE_SPAN[0], 
										block.COBBLESTONE, Church.WALL_NE_SPAN[1],
										description="NE Wall"))
		layer_blocks.append(Stair(offset, Vec3(0,0,0), 
								block.STAIRS_COBBLESTONE.withData(Stair.NORTH),
								description="Front Stair"))

		self.layers.append(BuildingLayer(layer_blocks, 0))
		del layer_blocks[:]

		# common blocks
		walls = []
		walls.append(BuildingBlock(offset, Church.WALL_W_SPAN[0], 
									block.COBBLESTONE, Church.WALL_W_SPAN[1]))
		walls.append(BuildingBlock(offset, Church.WALL_N_SPAN[0], 
									block.COBBLESTONE, Church.WALL_N_SPAN[1]))
		walls.append(BuildingBlock(offset, Church.WALL_E_SPAN[0], 
									block.COBBLESTONE, Church.WALL_E_SPAN[1]))
		walls.append(BuildingBlock(offset, Church.WALL_S_SPAN[0], 
									block.COBBLESTONE, Church.WALL_S_SPAN[1]))
		walls.append(ladder)

		# level 2
		layer_blocks.extend(walls)
		layer_blocks.append(BuildingBlock(offset, Church.DOOR_POS,  block.AIR))


		layer_blocks.append(BuildingBlock(offset, Vec3(-1,0,-7), 
										block.COBBLESTONE, Vec3(1,0,-8)))
		layer_blocks.append(Stair(offset, Vec3(-1,0,-6), 
								block.STAIRS_COBBLESTONE.withData(Stair.NORTH)))
		layer_blocks.append(Stair(offset, Vec3(0,0,-7), 
								block.STAIRS_COBBLESTONE.withData(Stair.NORTH)))
		layer_blocks.append(Stair(offset, Vec3(1,0,-6), 
								block.STAIRS_COBBLESTONE.withData(Stair.NORTH)))

		self.layers.append(BuildingLayer(layer_blocks, 1))
		del layer_blocks[:]

		# level 3
		layer_blocks.extend(walls)
		layer_blocks.append(BuildingBlock(offset, Church.DOOR_POS,  block.AIR))

		layer_blocks.append(Stair(offset, Vec3(-1,0,-8), 
								block.STAIRS_COBBLESTONE.withData(Stair.WEST)))
		layer_blocks.append(Stair(offset, Vec3(1,0,-8), 
								block.STAIRS_COBBLESTONE.withData(Stair.EAST)))

		for pos in Church.WINS_S_POS:
			layer_blocks.append(BuildingBlock(offset, pos, block.GLASS_PANE))
		
		self.layers.append(BuildingLayer(layer_blocks, 2))
		del layer_blocks[:]
		
		# level 4
		layer_blocks.extend(walls)
		for pos in Church.WINS_S_POS:
			layer_blocks.append(BuildingBlock(offset, pos, block.GLASS_PANE))
		for pos in Church.WINS_N_POS:
			layer_blocks.append(BuildingBlock(offset, pos, block.GLASS_PANE))

		self.layers.append(BuildingLayer(layer_blocks, 3))
		del layer_blocks[:]
		
		# level 5
		# insert the tower floor before the ladder in the walls list here
		walls.insert(4, BuildingBlock(offset, Church.TOWER_FLOOR_SPAN[0], 
										block.COBBLESTONE, Church.TOWER_FLOOR_SPAN[1]))
		layer_blocks.extend(walls)
		layer_blocks.append(BuildingBlock(offset, Church.WALL_TN_SPAN[0], 
										block.COBBLESTONE, Church.WALL_TN_SPAN[1]))
		layer_blocks.append(BuildingBlock(offset, Church.DOOR_POS,  block.COBBLESTONE))
		layer_blocks.append(BuildingBlock(offset, Vec3(-2,0,-1),  block.COBBLESTONE))
		layer_blocks.append(BuildingBlock(offset, Vec3(2,0,-1),  block.COBBLESTONE))

		layer_blocks.append(Torch(offset, Vec3(1,0,-7), block.TORCH.withData(Torch.WEST)))
		layer_blocks.append(Torch(offset, Vec3(0,0,-6), block.TORCH.withData(Torch.NORTH)))
		layer_blocks.append(Torch(offset, Vec3(-1,0,-7), block.TORCH.withData(Torch.EAST)))
		layer_blocks.append(Torch(offset, Vec3(0,0,-8), block.TORCH.withData(Torch.SOUTH)))

		self.layers.append(BuildingLayer(layer_blocks, 4))
		del layer_blocks[:]
		
		# reset walls for tower
		del walls[:]
		walls.append(BuildingBlock(offset, Church.WALL_SW_SPAN[0], 
									block.COBBLESTONE, Church.WALL_SW_SPAN[1]))
		walls.append(BuildingBlock(offset, Church.WALL_TN_SPAN[0], 
									block.COBBLESTONE, Church.WALL_TN_SPAN[1]))
		walls.append(BuildingBlock(offset, Church.WALL_SE_SPAN[0], 
									block.COBBLESTONE, Church.WALL_SE_SPAN[1]))
		walls.append(BuildingBlock(offset, Church.WALL_S_SPAN[0], 
									block.COBBLESTONE, Church.WALL_S_SPAN[1]))
		walls.append(ladder)

		# level 6
		layer_blocks.extend(walls)
		layer_blocks.append(BuildingBlock(offset, Church.ROOF_SPAN[0], 
										block.COBBLESTONE, Church.ROOF_SPAN[1]))

		self.layers.append(BuildingLayer(layer_blocks, 5))
		del layer_blocks[:]
		
		# levels 7 & 8 are same
		layer_blocks.extend(walls)
		for pos in Church.TOWER_WIN_POS:
			layer_blocks.append(BuildingBlock(offset, pos, block.GLASS_PANE))

		self.layers.append(BuildingLayer(layer_blocks, 6))
		self.layers.append(BuildingLayer(layer_blocks, 7))
		del layer_blocks[:]
		
		# level 9
		# nothing to add here just tower walls
		self.layers.append(BuildingLayer(walls, 8))
		
		# level 10
		# insert floor into walls here before ladder
		walls.insert(4, BuildingBlock(offset, Church.TOWER_FLOOR_SPAN[0], 
										block.COBBLESTONE, Church.TOWER_FLOOR_SPAN[1]))
		self.layers.append(BuildingLayer(walls, 9))
		
		# level 11
		# remove floor from walls
		walls = walls[:4]
		self.layers.append(BuildingLayer(walls, 10))
		
		# level 12
		for pos in Church.TOWER_WIN_POS:
			layer_blocks.append(BuildingBlock(offset, pos, block.COBBLESTONE))

		self.layers.append(BuildingLayer(layer_blocks, 11))
		del layer_blocks[:]

		self._set_orientation()
		
	def build(self, mc):
		super(Church, self).build(mc)

