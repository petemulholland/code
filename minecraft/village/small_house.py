from building import Building, BuildingLayer, BuildingBlock
from oriented_blocks import Stair, Ladder, Torch
import mcpi.block as block
from mcpi.vec3 import Vec3

HOUSE_BASE_POS = (Vec3(-2,0,1), Vec3(2,0,5))
HOUSE_INNER_POS = (Vec3(-1,0,2), Vec3(1,0,4))
HOUSE_WEST_WALL = (Vec3(-2,0,2), Vec3(-1,0,4))

HOUSE_NORTH_WALL = (Vec3(-1,0,5), Vec3(1,0,5))
HOUSE_EAST_WALL = (Vec3(2,0,4), Vec3(2,0,2))
HOUSE_SOUTH_WALL = (Vec3(-1,0,1), Vec3(1,0,1))

HOUSE_DOOR_POS = Vec3(0,0,1)
HOUSE_STEP_POS = Vec3(0,0,0)
HOUSE_LADDER_POS = Vec3(1,0,4)
HOUSE_TORCH_POS = (0,0,2)

WINDOW_EAST_POS = Vec3(2,0,3)
WINDOW_NORTH_POS = Vec3(0,0,5)
WINDOW_WEST_POS = Vec3(-2,0,3)

ROOF_FENCE_WEST =  (Vec3(-2,0,1), Vec3(-2,0,5))
ROOF_FENCE_NORTH = (Vec3(-1,0,5), Vec3(2,0,5))
ROOF_FENCE_EAST =  (Vec3(2,0,4), Vec3(2,0,1))
ROOF_FENCE_SOUTH = (Vec3(2,0,1), Vec3(-1,0,1))

OAK_UPDOWN = 0

class SmallHouse(Building):
	def __init__(self, *args, **kwargs):
		super(SmallHouse, self).__init__(*args, **kwargs)

		# build the base layer
		offset = self.pos
		HOUSE_BASE_BLOCKS = []
		HOUSE_BASE_BLOCKS.append(BuildingBlock(offset, HOUSE_BASE_POS[0], block.COBBLESTONE, HOUSE_BASE_POS[1]))
		HOUSE_BASE_BLOCKS.append(Stair(offset, HOUSE_STEP_POS, block.STAIRS_COBBLESTONE, None, Stair.NORTH))

		self.layers.append(BuildingLayer(HOUSE_BASE_BLOCKS, 0))
		
		# build the walls
		LADDER = Ladder(offset, HOUSE_LADDER_POS, block.LADDER, None, Ladder.NORTH)

		HOUSE_WALL_BLOCKS = []
		HOUSE_WALL_BLOCKS.append(BuildingBlock(offset, HOUSE_BASE_POS[0], block.COBBLESTONE, HOUSE_BASE_POS[1]))
		HOUSE_WALL_BLOCKS.append(BuildingBlock(offset, HOUSE_INNER_POS[0], block.AIR, HOUSE_INNER_POS[1])) # fill inner with air
		HOUSE_WALL_BLOCKS.append(BuildingBlock(offset, HOUSE_WEST_WALL[0], block.WOOD_PLANKS, HOUSE_WEST_WALL[1]))
		HOUSE_WALL_BLOCKS.append(BuildingBlock(offset, HOUSE_NORTH_WALL[0], block.WOOD_PLANKS, HOUSE_NORTH_WALL[1]))
		HOUSE_WALL_BLOCKS.append(BuildingBlock(offset, HOUSE_EAST_WALL[0], block.WOOD_PLANKS, HOUSE_EAST_WALL[1]))
		HOUSE_WALL_BLOCKS.append(BuildingBlock(offset, HOUSE_SOUTH_WALL[0], block.WOOD_PLANKS, HOUSE_SOUTH_WALL[1]))
		HOUSE_WALL_BLOCKS.append(LADDER)

		walls = list(HOUSE_WALL_BLOCKS)
		walls.append(BuildingBlock(offset, HOUSE_DOOR_POS, block.AIR))
		self.layers.append(BuildingLayer(walls, 1))

		# add windows to second layer of walls
		walls.append(BuildingBlock(offset, WINDOW_WEST_POS, block.GLASS_PANE))
		walls.append(BuildingBlock(offset, WINDOW_NORTH_POS, block.GLASS_PANE))
		walls.append(BuildingBlock(offset, WINDOW_EAST_POS, block.GLASS_PANE))
		self.layers.append(BuildingLayer(walls, 2))

		# reset wall blocks to build without windws & door
		walls = list(HOUSE_WALL_BLOCKS)
		walls.append(Torch(offset, HOUSE_TORCH_POS, block.TORCH, None, Torch.NORTH))
		self.layers.append(BuildingLayer(HOUSE_WALL_BLOCKS, 3))
		
		# build the roof
		HOUSE_ROOF_BLOCKS = []
		HOUSE_ROOF_BLOCKS.append(BuildingBlock(offset, HOUSE_BASE_POS[0], block.WOOD, HOUSE_BASE_POS[1], OAK_UPDOWN))
		HOUSE_ROOF_BLOCKS.append(BuildingBlock(offset, HOUSE_INNER_POS[0], block.WOOD_PLANKS, HOUSE_INNER_POS[1]))
		HOUSE_ROOF_BLOCKS.append(BuildingBlock(offset, HOUSE_LADDER_POS, block.AIR))
		HOUSE_ROOF_BLOCKS.append(LADDER)

		self.layers.append(BuildingLayer(HOUSE_ROOF_BLOCKS, 4))
		
		# add the fences to the roof
		fences = []
		fences.append(BuildingBlock(offset, ROOF_FENCE_WEST[0], block.FENCE, ROOF_FENCE_WEST[1]))
		fences.append(BuildingBlock(offset, ROOF_FENCE_NORTH[0], block.FENCE, ROOF_FENCE_NORTH[1]))
		fences.append(BuildingBlock(offset, ROOF_FENCE_EAST[0], block.FENCE, ROOF_FENCE_EAST[1]))
		fences.append(BuildingBlock(offset, ROOF_FENCE_SOUTH[0], block.FENCE, ROOF_FENCE_SOUTH[1]))
		self.layers.append(BuildingLayer(fences, 5))

		self._set_orientation()
		
	def build(self, mc):
		super(SmallHouse, self).build(mc)
		
