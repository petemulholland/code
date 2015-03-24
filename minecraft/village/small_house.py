from building import Building, BuildingLayer, BuildingBlock
from oriented_blocks import Stair, Ladder, Torch
import mcpi.block as block
from mcpi.vec3 import Vec3

OAK_UPDOWN = 0

class SmallHouseV1(Building):
	BASE_POS = (Vec3(-2,0,1), Vec3(2,0,5))
	INNER_POS = (Vec3(-1,0,2), Vec3(1,0,4))

	WALL_WEST = (Vec3(-2,0,2), Vec3(-1,0,4))
	WALL_NORTH = (Vec3(-1,0,5), Vec3(1,0,5))
	WALL_EAST = (Vec3(2,0,4), Vec3(2,0,2))
	WALL_SOUTH = (Vec3(-1,0,1), Vec3(1,0,1))

	DOOR_POS = Vec3(0,0,1)
	STEP_POS = Vec3(0,0,0)
	LADDER_POS = Vec3(1,0,4)
	TORCH_POS = Vec3(0,0,2)

	WIN_EAST_POS = Vec3(2,0,3)
	WIN_NORTH_POS = Vec3(0,0,5)
	WIN_WEST_POS = Vec3(-2,0,3)

	FENCE_WEST =  (Vec3(-2,0,1), Vec3(-2,0,5))
	FENCE_NORTH = (Vec3(-1,0,5), Vec3(2,0,5))
	FENCE_EAST =  (Vec3(2,0,4), Vec3(2,0,1))
	FENCE_SOUTH = (Vec3(2,0,1), Vec3(-1,0,1))

	def __init__(self, *args, **kwargs):
		super(SmallHouseV1, self).__init__(*args, **kwargs)

		# build the base layer
		offset = self.build_pos
		BASE_BLOCKS = []
		BASE_BLOCKS.append(BuildingBlock(offset, SmallHouseV1.BASE_POS[0], 
							  block.COBBLESTONE, SmallHouseV1.BASE_POS[1]))
		BASE_BLOCKS.append(Stair(offset, SmallHouseV1.STEP_POS, 
								block.STAIRS_COBBLESTONE, 
								None, Stair.NORTH))

		self.layers.append(BuildingLayer(BASE_BLOCKS, 0))
		
		# build the walls
		LADDER = Ladder(offset, SmallHouseV1.LADDER_POS, block.LADDER, None, Ladder.NORTH)

		WALL_BLOCKS = []
		WALL_BLOCKS.append(BuildingBlock(offset, SmallHouseV1.BASE_POS[0], 
							block.COBBLESTONE, SmallHouseV1.BASE_POS[1]))
		WALL_BLOCKS.append(BuildingBlock(offset, SmallHouseV1.INNER_POS[0], 
							block.AIR, SmallHouseV1.INNER_POS[1])) # fill inner with air
		WALL_BLOCKS.append(BuildingBlock(offset, SmallHouseV1.WALL_WEST[0], 
							block.WOOD_PLANKS, SmallHouseV1.WALL_WEST[1]))
		WALL_BLOCKS.append(BuildingBlock(offset, SmallHouseV1.WALL_NORTH[0], 
							block.WOOD_PLANKS, SmallHouseV1.WALL_NORTH[1]))
		WALL_BLOCKS.append(BuildingBlock(offset, SmallHouseV1.WALL_EAST[0], 
							block.WOOD_PLANKS, SmallHouseV1.WALL_EAST[1]))
		WALL_BLOCKS.append(BuildingBlock(offset, SmallHouseV1.WALL_SOUTH[0], 
							block.WOOD_PLANKS, SmallHouseV1.WALL_SOUTH[1]))
		WALL_BLOCKS.append(LADDER)

		walls = list(WALL_BLOCKS)
		walls.append(BuildingBlock(offset, SmallHouseV1.DOOR_POS, block.AIR))
		self.layers.append(BuildingLayer(walls, 1))

		# add windows to second layer of walls
		walls.append(BuildingBlock(offset, SmallHouseV1.WIN_WEST_POS, block.GLASS_PANE))
		walls.append(BuildingBlock(offset, SmallHouseV1.WIN_NORTH_POS, block.GLASS_PANE))
		walls.append(BuildingBlock(offset, SmallHouseV1.WIN_EAST_POS, block.GLASS_PANE))
		self.layers.append(BuildingLayer(walls, 2))

		# reset wall blocks to build without windws & door
		walls = list(WALL_BLOCKS)
		walls.append(Torch(offset, SmallHouseV1.TORCH_POS, block.TORCH, None, Torch.NORTH))
		self.layers.append(BuildingLayer(WALL_BLOCKS, 3))
		
		# build the roof
		ROOF_BLOCKS = []
		ROOF_BLOCKS.append(BuildingBlock(offset, SmallHouseV1.BASE_POS[0], 
							block.WOOD, SmallHouseV1.BASE_POS[1], OAK_UPDOWN))
		ROOF_BLOCKS.append(BuildingBlock(offset, SmallHouseV1.INNER_POS[0], 
							block.WOOD_PLANKS, SmallHouseV1.INNER_POS[1]))
		ROOF_BLOCKS.append(BuildingBlock(offset, SmallHouseV1.LADDER_POS, block.AIR))
		ROOF_BLOCKS.append(LADDER)

		self.layers.append(BuildingLayer(ROOF_BLOCKS, 4))
		
		# add the fences to the roof
		fences = []
		fences.append(BuildingBlock(offset, SmallHouseV1.FENCE_WEST[0], 
						block.FENCE, SmallHouseV1.FENCE_WEST[1]))
		fences.append(BuildingBlock(offset, SmallHouseV1.FENCE_NORTH[0], 
						block.FENCE, SmallHouseV1.FENCE_NORTH[1]))
		fences.append(BuildingBlock(offset, SmallHouseV1.FENCE_EAST[0], 
						block.FENCE, SmallHouseV1.FENCE_EAST[1]))
		fences.append(BuildingBlock(offset, SmallHouseV1.FENCE_SOUTH[0], 
						block.FENCE, SmallHouseV1.FENCE_SOUTH[1]))
		self.layers.append(BuildingLayer(fences, 5))

		# add the door
		self.layers.append(BuildingLayer([BuildingBlock(offset, 
								SmallHouseV2Base.DOOR_POS, block.DOOR_WOOD)], 1))


		self._set_orientation()
		
	def build(self, mc):
		super(SmallHouseV1, self).build(mc)


class SmallHouseV2Base(Building):
	BASE_POS = (Vec3(-1,0,1), Vec3(2,0,5))
	INNER_POS = (Vec3(0,0,2), Vec3(1,0,4))

	WALL_WEST = (Vec3(-1,0,2), Vec3(-1,0,4))
	WALL_NORTH = (Vec3(0,0,5), Vec3(1,0,5))
	WALL_EAST = (Vec3(2,0,4), Vec3(2,0,2))
	WALL_SOUTH = (Vec3(0,0,1), Vec3(1,0,1))

	DOOR_POS = Vec3(0,0,1)
	STEP_POS = Vec3(0,0,0)
	TORCH_POS = Vec3(0,0,2)

	WIN_EAST_POS = Vec3(2,0,3)
	WIN_WEST_POS = Vec3(-2,0,3)

	def __init__(self, *args, **kwargs):
		super(SmallHouseV2Base, self).__init__(*args, **kwargs)

		offset = self.build_pos
		# build the base layer
		BASE_BLOCKS = []
		BASE_BLOCKS.append(BuildingBlock(offset, SmallHouseV2Base.BASE_POS[0], 
							  block.COBBLESTONE, SmallHouseV2Base.BASE_POS[1]))
		BASE_BLOCKS.append(BuildingBlock(offset, SmallHouseV2Base.INNER_POS[0], 
							  block.DIRT, SmallHouseV2Base.INNER_POS[1]))
		BASE_BLOCKS.append(Stair(offset, SmallHouseV2Base.STEP_POS, 
								block.STAIRS_COBBLESTONE, 
								None, Stair.NORTH))

		self.layers.append(BuildingLayer(BASE_BLOCKS, 0))

		# build the walls
		WALL_BLOCKS = []
		WALL_BLOCKS.append(BuildingBlock(offset, SmallHouseV2Base.BASE_POS[0], 
							block.WOOD, SmallHouseV2Base.BASE_POS[1], OAK_UPDOWN))
		WALL_BLOCKS.append(BuildingBlock(offset, SmallHouseV2Base.INNER_POS[0], 
							block.AIR, SmallHouseV2Base.INNER_POS[1])) # fill inner with air
		WALL_BLOCKS.append(BuildingBlock(offset, SmallHouseV2Base.WALL_WEST[0], 
							block.WOOD_PLANKS, SmallHouseV2Base.WALL_WEST[1]))
		WALL_BLOCKS.append(BuildingBlock(offset, SmallHouseV2Base.WALL_NORTH[0], 
							block.WOOD_PLANKS, SmallHouseV2Base.WALL_NORTH[1]))
		WALL_BLOCKS.append(BuildingBlock(offset, SmallHouseV2Base.WALL_EAST[0], 
							block.WOOD_PLANKS, SmallHouseV2Base.WALL_EAST[1]))
		WALL_BLOCKS.append(BuildingBlock(offset, SmallHouseV2Base.WALL_SOUTH[0], 
							block.WOOD_PLANKS, SmallHouseV2Base.WALL_SOUTH[1]))

		walls = list(WALL_BLOCKS)
		walls.append(BuildingBlock(offset, SmallHouseV2Base.DOOR_POS, block.AIR))
		self.layers.append(BuildingLayer(walls, 1))

		# add windows to second layer of walls
		walls.append(BuildingBlock(offset, SmallHouseV2Base.WIN_WEST_POS, block.GLASS_PANE))
		walls.append(BuildingBlock(offset, SmallHouseV2Base.WIN_EAST_POS, block.GLASS_PANE))
		self.layers.append(BuildingLayer(walls, 2))

		# reset wall blocks to build without windws & door
		walls = list(WALL_BLOCKS)
		walls.append(Torch(offset, SmallHouseV2Base.TORCH_POS, block.TORCH, None, Torch.NORTH))
		self.layers.append(BuildingLayer(WALL_BLOCKS, 3))

		# add the door
		self.layers.append(BuildingLayer([BuildingBlock(offset, 
								SmallHouseV2Base.DOOR_POS, block.DOOR_WOOD)], 1))

		# derived classes specialize the roof


	def build(self, mc):
		super(SmallHouseV2Base, self).build(mc)

		
class SmallHouseV2(SmallHouseV2Base):
	def __init__(self, *args, **kwargs):
		super(SmallHouseV2, self).__init__(*args, **kwargs)
		
		offset = self.build_pos
		# add roof layers
		roof = []
		roof.append(BuildingBlock(offset, SmallHouseV2Base.BASE_POS[0], 
							block.WOOD, SmallHouseV2Base.BASE_POS[1], OAK_UPDOWN))
		roof.append(BuildingBlock(offset, SmallHouseV2Base.INNER_POS[0], 
							block.AIR, SmallHouseV2Base.INNER_POS[1])) # fill inner with air
		roof.append(BuildingBlock(offset, Vec3(-1,0,1), block.AIR))
		roof.append(BuildingBlock(offset, Vec3(-1,0,5), block.AIR))
		roof.append(BuildingBlock(offset, Vec3(2,0,5), block.AIR))
		roof.append(BuildingBlock(offset, Vec3(2,0,1), block.AIR))
		self.layers.append(BuildingLayer(roof, 3))

		roof = []
		roof.append(BuildingBlock(offset, SmallHouseV2Base.INNER_POS[0], 
							block.WOOD, SmallHouseV2Base.INNER_POS[1], OAK_UPDOWN))
		self.layers.append(BuildingLayer(roof, 4))

		self._set_orientation()


class SmallHouseV3(SmallHouseV2Base):
	def __init__(self, *args, **kwargs):
		super(SmallHouseV3, self).__init__(*args, **kwargs)

		offset = self.build_pos
		# add roof layer
		roof = []
		roof.append(BuildingBlock(offset, SmallHouseV2Base.BASE_POS[0], 
							block.WOOD, SmallHouseV2Base.BASE_POS[1], OAK_UPDOWN))
		roof.append(BuildingBlock(offset, Vec3(-1,0,1), block.AIR))
		roof.append(BuildingBlock(offset, Vec3(-1,0,5), block.AIR))
		roof.append(BuildingBlock(offset, Vec3(2,0,5), block.AIR))
		roof.append(BuildingBlock(offset, Vec3(2,0,1), block.AIR))
		self.layers.append(BuildingLayer(roof, 3))

		self._set_orientation()


