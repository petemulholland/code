from building import Building, BuildingLayer, BuildingBlock
from oriented_blocks import Torch, Stair, Ladder
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

class Butcher(Building):
	"""description of class"""
	
	PEN_CORNERS_POS = { 'South West' : Vec3(-2,0,-8),
						'North West' : Vec3(-2,0,-12),
						'North East' : Vec3(4,0,-12),
						'South East' : Vec3(4,0,-8) }

	WALLS_CORNER_POS = {'South West' : Vec3(-4,0,-2),
						'North West' : Vec3(-4,0,-7),
						'North East' : Vec3(4,0,-7),
						'South East' : Vec3(4,0,-2) }

	WINDOW_SPANS = {'West' : (Vec3(-4,0,-4), Vec3(-4,0,-5)),
					'North' : (Vec3(-2,0,-7), Vec3(-1,0,-7)),
					'East' : (Vec3(4,0,-5), Vec3(4,0,-4)),
					'South' : (Vec3(-2,0,1), Vec3(-2,0,1)), }

	SOUTH_DOOR_POS = Vec3(-2,0,-2)
	NORTH_DOOR_POS = Vec3(2,0,-7)

	FLOOR_SPANS = ((Vec3(-3,0,-3), Vec3(0,0,-6), block.WOOD_PLANKS),
					(Vec3(1,0,-6), Vec3(3,0,-6), block.WOOD_PLANKS),
					(Vec3(1,0,-3), Vec3(3,0,-5), block.STONE_SLAB_DOUBLE))


	def __init__(self, *args, **kwargs):
		super(Butcher, self).__init__(*args, **kwargs)

		offset = self.build_pos

		layer_blocks = []
		# level 1
		# Pen
		layer_blocks.append(BuildingBlock(offset, Butcher.PEN_CORNERS_POS['South West'], 
										block.DIRT, Butcher.PEN_CORNERS_POS['North East'],
										description="Pen base"))
		walls = []								
		# Walls 
		walls.append(BuildingBlock(offset, Butcher.WALLS_CORNER_POS['South West'], 
										block.COBBLESTONE, Butcher.WALLS_CORNER_POS['North West'],
										description="West wall base"))
		walls.append(BuildingBlock(offset, Butcher.WALLS_CORNER_POS['North West'], 
										block.COBBLESTONE, Butcher.WALLS_CORNER_POS['North East'],
										description="North wall base"))
		walls.append(BuildingBlock(offset, Butcher.WALLS_CORNER_POS['North East'], 
										block.COBBLESTONE, Butcher.WALLS_CORNER_POS['South East'],
										description="East wall base"))
		walls.append(BuildingBlock(offset, Butcher.WALLS_CORNER_POS['South East'], 
										block.COBBLESTONE, Butcher.WALLS_CORNER_POS['South West'],
										description="South wall base"))
		layer_blocks.extend(walls)

		# floor
		for pos1, pos2, block_type in Butcher.FLOOR_SPANS:
			layer_blocks.append(BuildingBlock(offset, pos1, block_type, pos2,
											description="floor"))

		# door steps
		layer_blocks.append(Stair(offset, Butcher.SOUTH_DOOR_POS + Vec3(0,0,1), 
								block.STAIRS_COBBLESTONE.withData(Stair.NORTH), 
								description="Front door step"))
		layer_blocks.append(BuildingBlock(offset, Butcher.NORTH_DOOR_POS + Vec3(0,0,-1), 
										block.COBBLESTONE, 
										description="Pen door step"))

		self.layers.append(BuildingLayer(layer_blocks, 0))
		del layer_blocks[:]

		# level 2
		# Pen fences
		layer_blocks.append(BuildingBlock(offset, Butcher.PEN_CORNERS_POS['South West'], 
										block.FENCE, Butcher.PEN_CORNERS_POS['North West'],
										description="West pen fence"))
		layer_blocks.append(BuildingBlock(offset, Butcher.PEN_CORNERS_POS['North West'], 
										block.FENCE, Butcher.PEN_CORNERS_POS['North East'],
										description="North pen fence"))
		layer_blocks.append(BuildingBlock(offset, Butcher.PEN_CORNERS_POS['North East'], 
										block.FENCE, Butcher.PEN_CORNERS_POS['South East'],
										description="East pen fence"))
		# Walls 
		layer_blocks.extend(walls)
		layer_blocks.append(BuildingBlock(offset, Butcher.SOUTH_DOOR_POS, 
										block.AIR, description="Clear front door"))
		layer_blocks.append(BuildingBlock(offset, Butcher.NORTH_DOOR_POS, 
										block.AIR, description="Clear pen door"))

		# table
		layer_blocks.append(BuildingBlock(offset, Vec3(-3,0,-6), 
										block.WOOD_PLANKS, 
										description="Table area corner"))
		layer_blocks.append(BuildingBlock(offset, Vec3(-2,0,-5), 
										block.FENCE, description="Table base"))
		layer_blocks.append(Stair(offset, Vec3(-3,0,-5), 
								block.STAIRS_WOOD.withData(Stair.WEST), 
								description="West seat"))
		layer_blocks.append(Stair(offset, Vec3(-2,0,-6), 
								block.STAIRS_WOOD.withData(Stair.NORTH), 
								description="North seat"))

		# counter
		layer_blocks.append(BuildingBlock(offset, Vec3(2,0,-3), 
										block.STONE_SLAB_DOUBLE, Vec3(2,0,-4),
										description="Counter"))


		self.layers.append(BuildingLayer(layer_blocks, 1))
		del layer_blocks[:]

		# level 3
		# corners
		for key, pos in Butcher.WALLS_CORNER_POS.items():
			layer_blocks.append(BuildingBlock(offset, pos, 
										block.COBBLESTONE, description=key + " corner"))
		# north and south walls
		layer_blocks.append(BuildingBlock(offset, Butcher.WALLS_CORNER_POS['North West'] + Vec3(1,0,0), 
										block.WOOD_PLANKS, Butcher.WALLS_CORNER_POS['North East'] + Vec3(-1,0,0),
										description="North wall"))
		layer_blocks.append(BuildingBlock(offset, Butcher.WALLS_CORNER_POS['South West'] + Vec3(1,0,0), 
										block.WOOD_PLANKS, Butcher.WALLS_CORNER_POS['South East'] + Vec3(-1,0,0),
										description="South wall"))

		# east and west walls
		layer_blocks.append(BuildingBlock(offset, Butcher.WALLS_CORNER_POS['South West'] + Vec3(0,0,-1), 
										block.WOOD, Butcher.WALLS_CORNER_POS['North West'] + Vec3(0,0,1),
										description="West wall"))
		layer_blocks.append(BuildingBlock(offset, Butcher.WALLS_CORNER_POS['North East'] + Vec3(0,0,-1), 
										block.WOOD, Butcher.WALLS_CORNER_POS['South East'] + Vec3(0,0,1),
										description="East wall"))

		# windows
		for key, span in Butcher.WINDOW_SPANS.items():
			# clear the space first:
			layer_blocks.append(BuildingBlock(offset, span[0], 
											block.AIR, span[1],
											description="Clearing " + key + " window"))
			layer_blocks.append(BuildingBlock(offset, span[0], 
											block.GLASS_PANE, span[1],
											description=key + " window"))

		layer_blocks.append(BuildingBlock(offset, Butcher.SOUTH_DOOR_POS, 
										block.AIR, description="Clear front door"))
		layer_blocks.append(BuildingBlock(offset, Butcher.NORTH_DOOR_POS, 
										block.AIR, description="Clear pen door"))

		# TODO: table top

		self.layers.append(BuildingLayer(layer_blocks, 2))
		del layer_blocks[:]

		# level 4
		# east & west stone walls
		layer_blocks.append(BuildingBlock(offset, Butcher.WALLS_CORNER_POS['South West'], 
										block.COBBLESTONE, Butcher.WALLS_CORNER_POS['North West'],
										description="West wall"))
		layer_blocks.append(BuildingBlock(offset, Butcher.WALLS_CORNER_POS['North East'], 
										block.COBBLESTONE, Butcher.WALLS_CORNER_POS['South East'],
										description="East wall"))
		# north and south wood walls
		layer_blocks.append(BuildingBlock(offset, Butcher.WALLS_CORNER_POS['North West'] + Vec3(1,0,0), 
										block.WOOD_PLANKS, Butcher.WALLS_CORNER_POS['North East'] + Vec3(-1,0,0),
										description="North wall"))
		layer_blocks.append(BuildingBlock(offset, Butcher.WALLS_CORNER_POS['South East'] + Vec3(1,0,0), 
										block.WOOD_PLANKS, Butcher.WALLS_CORNER_POS['South West'] + Vec3(-1,0,0),
										description="South wall"))

		# north and south roof eaves
		layer_blocks.append(Stair(offset, Butcher.WALLS_CORNER_POS['North West'] + Vec3(0,0,-1), 
										block.STAIRS_WOOD.withData(Stair.SOUTH), 
										Butcher.WALLS_CORNER_POS['North East'] + Vec3(0,0,-1),
										description="North roof eaves"))
		layer_blocks.append(Stair(offset, Butcher.WALLS_CORNER_POS['South East'] + Vec3(0,0,1), 
										block.STAIRS_WOOD.withData(Stair.NORTH), 
										Butcher.WALLS_CORNER_POS['South West'] + Vec3(0,0,1),
										description="South roof eaves"))
		# torches over doors
		layer_blocks.append(Torch(offset, Butcher.SOUTH_DOOR_POS + Vec3(0,0,-1), 
										block.TORCH.withData(Torch.NORTH), 
										description="Torch over front door"))
		layer_blocks.append(Torch(offset, Butcher.NORTH_DOOR_POS + Vec3(0,0,1), 
										block.TORCH.withData(Torch.SOUTH), 
										description="Torch over pen door"))

		self.layers.append(BuildingLayer(layer_blocks, 3))
		del layer_blocks[:]

		# level 5

		# east & west gables
		layer_blocks.append(BuildingBlock(offset, Butcher.WALLS_CORNER_POS['South West'] + Vec3(0,0,-1), 
										block.WOOD_PLANKS, Butcher.WALLS_CORNER_POS['North West'] + Vec3(0,0,1),
										description="West gable"))
		layer_blocks.append(BuildingBlock(offset, Butcher.WALLS_CORNER_POS['North East'] + Vec3(0,0,1), 
										block.WOOD_PLANKS, Butcher.WALLS_CORNER_POS['South East'] + Vec3(0,0,-1),
										description="East gable"))
		# north and south rafters
		layer_blocks.append(BuildingBlock(offset, Butcher.WALLS_CORNER_POS['North West'] + Vec3(0,0,1), 
										block.WOOD_PLANKS, Butcher.WALLS_CORNER_POS['North East'] + Vec3(0,0,1),
										description="North rafters"))
		layer_blocks.append(BuildingBlock(offset, Butcher.WALLS_CORNER_POS['South East'] + Vec3(0,0,-1), 
										block.WOOD_PLANKS, Butcher.WALLS_CORNER_POS['South West'] + Vec3(0,0,-1),
										description="South rafters"))

		# north and south roof 
		layer_blocks.append(Stair(offset, Butcher.WALLS_CORNER_POS['North West'], 
										block.STAIRS_WOOD.withData(Stair.SOUTH), 
										Butcher.WALLS_CORNER_POS['North East'],
										description="North roof"))
		layer_blocks.append(Stair(offset, Butcher.WALLS_CORNER_POS['South East'], 
										block.STAIRS_WOOD.withData(Stair.NORTH), 
										Butcher.WALLS_CORNER_POS['South West'],
										description="South roof"))


		self.layers.append(BuildingLayer(layer_blocks, 4))
		del layer_blocks[:]

		# level 6
		# rafters
		layer_blocks.append(BuildingBlock(offset, Butcher.WALLS_CORNER_POS['South West'] + Vec3(0,0,-2), 
										block.WOOD_PLANKS, Butcher.WALLS_CORNER_POS['North East'] + Vec3(0,0,2),
										description="Rafters"))

		# north and south roof 
		layer_blocks.append(Stair(offset, Butcher.WALLS_CORNER_POS['North West'] + Vec3(0,0,1), 
										block.STAIRS_WOOD.withData(Stair.SOUTH), 
										Butcher.WALLS_CORNER_POS['North East'] + Vec3(0,0,1),
										description="North roof"))
		layer_blocks.append(Stair(offset, Butcher.WALLS_CORNER_POS['South East'] + Vec3(0,0,-1), 
										block.STAIRS_WOOD.withData(Stair.NORTH), 
										Butcher.WALLS_CORNER_POS['South West'] + Vec3(0,0,-1),
										description="South roof"))

		self.layers.append(BuildingLayer(layer_blocks, 5))
		del layer_blocks[:]

		# level 7
		# north and south roof 
		layer_blocks.append(Stair(offset, Butcher.WALLS_CORNER_POS['North West'] + Vec3(0,0,2), 
										block.STAIRS_WOOD.withData(Stair.SOUTH), 
										Butcher.WALLS_CORNER_POS['North East'] + Vec3(0,0,2),
										description="North roof"))
		layer_blocks.append(Stair(offset, Butcher.WALLS_CORNER_POS['South East'] + Vec3(0,0,-2), 
										block.STAIRS_WOOD.withData(Stair.NORTH), 
										Butcher.WALLS_CORNER_POS['South West'] + Vec3(0,0,-2),
										description="South roof"))

		self.layers.append(BuildingLayer(layer_blocks, 6))
		del layer_blocks[:]


		self._set_orientation()
		
	def build(self, mc):
		super(Butcher, self).build(mc)

