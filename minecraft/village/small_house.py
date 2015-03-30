from building import Building, BuildingLayer, BuildingBlock
from oriented_blocks import Stair, Ladder, Torch
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

class SmallHouseV1(Building):
	
	WALLS_CORNER_POS = {'South East' : Building.SE_CORNER_POS,
						'South West' : Building.SE_CORNER_POS + Vec3(-4,0,0),
						'North West' : Building.SE_CORNER_POS + Vec3(-4,0,-4),
						'North East' : Building.SE_CORNER_POS + Vec3(0,0,-4)}

	WALL_SPANS = [(WALLS_CORNER_POS['South West'] + Vec3(0,0,-1), 
						WALLS_CORNER_POS['North West'] + Vec3(0,0,1), "West Wall"),
					(WALLS_CORNER_POS['North West'] + Vec3(1,0,0), 
						WALLS_CORNER_POS['North East'] + Vec3(-1,0,0), "North Wall"),
					(WALLS_CORNER_POS['North East'] + Vec3(0,0,1), 
						WALLS_CORNER_POS['South East'] + Vec3(0,0,-1), "East Wall"),
					(WALLS_CORNER_POS['South East'] + Vec3(-1,0,0), 
						WALLS_CORNER_POS['South West'] + Vec3(1,0,0), "South Wall")]

	DOOR_POS = WALLS_CORNER_POS['South East'] + Vec3(-2,0,0)
	STEP_POS = DOOR_POS + Vec3(0,0,1)
	TORCH_POS = DOOR_POS + Vec3(0,0,-1)
	LADDER_POS = DOOR_POS + Vec3(1,0,-3)

	WIN_POS = [WALLS_CORNER_POS['South East'] + Vec3(0,0,-2), 
				WALLS_CORNER_POS['South West'] + Vec3(0,0,-2), 
				WALLS_CORNER_POS['North East'] + Vec3(-2,0,0)]

	WIDTH = 5
	def __init__(self, *args, **kwargs):
		super(SmallHouseV1, self).__init__(width=SmallHouseV1.WIDTH, *args, **kwargs)

		#######################################################################
		# Level 1:
		layer_blocks = []
		layer_blocks.append(BuildingBlock(SmallHouseV1.WALLS_CORNER_POS['South West'], 
							  block.COBBLESTONE, SmallHouseV1.WALLS_CORNER_POS['North East'],
							  description="House base"))
		layer_blocks.append(Stair(SmallHouseV1.STEP_POS, 
								block.STAIRS_COBBLESTONE.withData(Stair.NORTH),
								description="Front step"))

		self.layers.append(BuildingLayer(layer_blocks, 0))
		del layer_blocks [:]

		#######################################################################
		# Common blocks:
		walls = []
		
		# cobblestone corners
		for key, pos in SmallHouseV1.WALLS_CORNER_POS.items():
			walls.append(BuildingBlock(pos, block.COBBLESTONE, description="Corner stone"))
		
		# wood plank walls 
		for pos1, pos2, desc in SmallHouseV1.WALL_SPANS:
			walls.append(BuildingBlock(pos1, block.WOOD_PLANKS, pos2, desc))

		# ladder
		ladder = Ladder(SmallHouseV1.LADDER_POS, block.LADDER.withData(Ladder.NORTH), description="Ladder")
		walls.append(ladder)

		#######################################################################
		# Level 2:
		# add walls as above & clear door	
		layer_blocks.extend(walls)
		
		layer_blocks.append(BuildingBlock(SmallHouseV1.DOOR_POS, block.AIR, description="Clear door"))
		self.layers.append(BuildingLayer(layer_blocks, 1))
		del layer_blocks [:]

		#######################################################################
		# Level 3:
		# add walls, clear door	& add windows
		layer_blocks.extend(walls)
			
		layer_blocks.append(BuildingBlock(SmallHouseV1.DOOR_POS, block.AIR, description="Clear door"))

		for pos in SmallHouseV1.WIN_POS:
			layer_blocks.append(BuildingBlock(pos, block.GLASS_PANE, description="Window"))

		self.layers.append(BuildingLayer(layer_blocks, 2))
		del layer_blocks [:]

		#######################################################################
		# Level 4:
		# add walls & torch over door	
		layer_blocks.extend(walls)
			
		layer_blocks.append(Torch(SmallHouseV1.TORCH_POS, block.TORCH.withData(Torch.NORTH), 
									description="Torch over door"))
		self.layers.append(BuildingLayer(layer_blocks, 3))
		del layer_blocks [:]

		#######################################################################
		# build the roof
		layer_blocks.append(BuildingBlock(SmallHouseV1.WALLS_CORNER_POS['South East'], 
							block.WOOD, SmallHouseV1.WALLS_CORNER_POS['North West'],
							description="Roof wood span"))
		layer_blocks.append(BuildingBlock(SmallHouseV1.WALLS_CORNER_POS['South East'] + Vec3(-1,0,-1), 
							block.WOOD_PLANKS, SmallHouseV1.WALLS_CORNER_POS['North West'] + Vec3(1,0,1),
							description="Roof wood plank span"))

		layer_blocks.append(BuildingBlock(SmallHouseV1.LADDER_POS, block.AIR, description="Clear ladder space"))
		
		layer_blocks.append(ladder)

		self.layers.append(BuildingLayer(layer_blocks, 4))
		del layer_blocks [:]

		#######################################################################
		# add the fences to the roof
		layer_blocks.append(BuildingBlock(SmallHouseV1.WALLS_CORNER_POS['South East'], 
							block.FENCE, SmallHouseV1.WALLS_CORNER_POS['North West'],
							description="Cover roof with fences"))
		layer_blocks.append(BuildingBlock(SmallHouseV1.WALLS_CORNER_POS['South East'] + Vec3(-1,0,-1), 
							block.AIR, SmallHouseV1.WALLS_CORNER_POS['North West'] + Vec3(1,0,1),
							description="Clear fences from inner roof"))

		self.layers.append(BuildingLayer(layer_blocks, 5))
		del layer_blocks [:]

		#######################################################################
		# add the door
		#self.layers.append(BuildingLayer([BuildingBlock(
		#						SmallHouseV2Base.DOOR_POS, block.DOOR_WOOD)], 2))

		self._set_orientation()
		
	def build(self, mc):
		super(SmallHouseV1, self).build(mc)


class SmallHouseV2Base(Building):
	WALLS_CORNER_POS = {'South East' : Building.SE_CORNER_POS,
						'South West' : Building.SE_CORNER_POS + Vec3(-3,0,0),
						'North West' : Building.SE_CORNER_POS + Vec3(-3,0,-4),
						'North East' : Building.SE_CORNER_POS + Vec3(0,0,-4) }

	WALL_SPANS = [(WALLS_CORNER_POS['South West'] + Vec3(0,0,-1), 
						WALLS_CORNER_POS['North West'] + Vec3(0,0,1), "West Wall"),
					(WALLS_CORNER_POS['North West'] + Vec3(1,0,0), 
						WALLS_CORNER_POS['North East'] + Vec3(-1,0,0), "North Wall"),
					(WALLS_CORNER_POS['North East'] + Vec3(0,0,1), 
						WALLS_CORNER_POS['South East'] + Vec3(0,0,-1), "East Wall"),
					(WALLS_CORNER_POS['South East'] + Vec3(-1,0,0), 
						WALLS_CORNER_POS['South West'] + Vec3(1,0,0), "South Wall")]

	DOOR_POS = WALLS_CORNER_POS['South East'] + Vec3(-2,0,0)
	STEP_POS = DOOR_POS + Vec3(0,0,1)
	TORCH_POS = DOOR_POS + Vec3(0,0,-1)

	WIN_POS = [WALLS_CORNER_POS['South East'] + Vec3(0,0,-2), 
				WALLS_CORNER_POS['South West'] + Vec3(0,0,-2)]


	WIDTH = 4
	def __init__(self, *args, **kwargs):
		super(SmallHouseV2Base, self).__init__(width=SmallHouseV2Base.WIDTH, *args, **kwargs)

		#######################################################################
		# Level 1:
		layer_blocks = []
		layer_blocks.append(BuildingBlock(SmallHouseV2Base.WALLS_CORNER_POS['South West'], 
							  block.COBBLESTONE, SmallHouseV2Base.WALLS_CORNER_POS['North East'],
							  description="House base"))
		layer_blocks.append(BuildingBlock(SmallHouseV2Base.WALLS_CORNER_POS['South East'] + Vec3(-1,0,-1), 
							  block.DIRT, SmallHouseV2Base.WALLS_CORNER_POS['North West'] + Vec3(1,0,1),
							  description="House inner base"))
		layer_blocks.append(Stair(SmallHouseV2Base.STEP_POS, 
								block.STAIRS_COBBLESTONE.withData(Stair.NORTH),
								description="Front step"))

		self.layers.append(BuildingLayer(layer_blocks, 0))
		del layer_blocks [:]

		#######################################################################
		# Common blocks:
		walls = []
		
		# wood corners
		for key, pos in SmallHouseV2Base.WALLS_CORNER_POS.items():
			walls.append(BuildingBlock(pos, block.WOOD, description="Corner wood"))
		
		# wood plank walls 
		for pos1, pos2, desc in SmallHouseV2Base.WALL_SPANS:
			walls.append(BuildingBlock(pos1, block.WOOD_PLANKS, pos2, desc))

		#######################################################################
		# Level 2:
		# add walls as above & clear door	
		layer_blocks.extend(walls)
		
		layer_blocks.append(BuildingBlock(SmallHouseV2Base.DOOR_POS, block.AIR, description="Clear door"))
		self.layers.append(BuildingLayer(layer_blocks, 1))
		del layer_blocks [:]

		#######################################################################
		# Level 3:
		# add walls, clear door	& add windows
		layer_blocks.extend(walls)
			
		layer_blocks.append(BuildingBlock(SmallHouseV2Base.DOOR_POS, block.AIR, description="Clear door"))

		for pos in SmallHouseV2Base.WIN_POS:
			layer_blocks.append(BuildingBlock(pos, block.GLASS_PANE, description="Window"))

		self.layers.append(BuildingLayer(layer_blocks, 2))
		del layer_blocks [:]

		#######################################################################
		# Level 4:
		# add walls & torch over door	
		layer_blocks.extend(walls)
			
		layer_blocks.append(Torch(SmallHouseV2Base.TORCH_POS, block.TORCH.withData(Torch.NORTH), 
									description="Torch over door"))
		self.layers.append(BuildingLayer(layer_blocks, 3))
		del layer_blocks [:]

		# derived classes specialize the roof


	def build(self, mc):
		super(SmallHouseV2Base, self).build(mc)

		
class SmallHouseV2(SmallHouseV2Base):
	def __init__(self, *args, **kwargs):
		super(SmallHouseV2, self).__init__(*args, **kwargs)
		
		#######################################################################
		# build the roof
		layer_blocks = []
		# create the wall spans as wood for first layer of roof
		for pos1, pos2, desc in SmallHouseV2Base.WALL_SPANS:
			layer_blocks.append(BuildingBlock(pos1, block.WOOD, pos2, desc + " roof"))

		self.layers.append(BuildingLayer(layer_blocks, 4))
		del layer_blocks [:]

		# create inner span as wood for second layer of roof
		layer_blocks.append(BuildingBlock(SmallHouseV2Base.WALLS_CORNER_POS['South East'] + Vec3(-1,0,-1), 
							  block.WOOD, SmallHouseV2Base.WALLS_CORNER_POS['North West'] + Vec3(1,0,1),
							  description="Roof inner"))

		self.layers.append(BuildingLayer(layer_blocks, 5))
		del layer_blocks [:]

		self._set_orientation()


class SmallHouseV3(SmallHouseV2Base):
	def __init__(self, *args, **kwargs):
		super(SmallHouseV3, self).__init__(*args, **kwargs)

		#######################################################################
		# build the roof
		layer_blocks = []

		# fill full building span with wood for roof
		layer_blocks.append(BuildingBlock(SmallHouseV2Base.WALLS_CORNER_POS['South East'], 
							  block.WOOD, SmallHouseV2Base.WALLS_CORNER_POS['North West'],
							  description="Roof"))

		# clear corners
		for key, pos in SmallHouseV2Base.WALLS_CORNER_POS.items():
			layer_blocks.append(BuildingBlock(pos, block.AIR, description="Clear roof corners"))

		self.layers.append(BuildingLayer(layer_blocks, 4))
		del layer_blocks [:]

		self._set_orientation()

