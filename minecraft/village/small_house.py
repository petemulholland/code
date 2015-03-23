from building import Building, BuildingLayer, BuildingBlock
from oriented_blocks import Stair, Ladder, Torch
import mcpi.block as block
from mcpi.vec3 import Vec3

HOUSE_BASE = (Vec3(-2,0,1), Vec3(2,0,5))
HOUSE_INNER = (Vec3(-1,0,2), Vec3(1,0,4))
HOUSE_WEST_WALL = (Vec3(-2,0,2), Vec3(-1,0,4))
HOUSE_NORTH_WALL = (Vec3(-1,0,5), Vec3(1,0,5))
HOUSE_EAST_WALL = (Vec3(2,0,4), Vec3(2,0,2))
HOUSE_SOUTH_WALL = (Vec3(-1,0,1), Vec3(1,0,1))
HOUSE_DOOR = Vec3(0,0,1)
HOUSE_STEP = Vec3(0,0,0)
HOUSE_LADDER = Vec3(1,0,4)
WINDOW_EAST = Vec3(2,0,3)
WINDOW_NORTH = Vec3(0,0,5)
WINDOW_WEST = Vec3(-2,0,3)
ROOF_FENCE_WEST =  (Vec3(-2,0,1), Vec3(-2,0,5))
ROOF_FENCE_NORTH = (Vec3(-1,0,5), Vec3(2,0,5))
ROOF_FENCE_EAST =  (Vec3(2,0,4), Vec3(2,0,1))
ROOF_FENCE_SOUTH = (Vec3(2,0,1), Vec3(-1,0,1))
TORCH_POS = (0,0,2)
OAK_UPDOWN = 0

class SmallHouse(Building):
	def __init__(self, **kwargs):
		super(SmallHouse, self).__init__(**kwargs)

		offset = self.pos
		HOUSE_BASE = []
		HOUSE_BASE.append(BuildingBlock(offset, HOUSE_BASE[0], block.COBBLESTONE, HOUSE_BASE[1]))
		HOUSE_BASE.append(Stair(offset, HOUSE_STEP, block.COBBLESTONE_STAIR, None, Stair.NORTH))

		LADDER = Ladder(offset, HOUSE_LADDER, block.LADDER, None, Ladder.NORTH)

		HOUSE_WALL = []
		HOUSE_WALL.append(BuildingBlock(offset, HOUSE_BASE[0], block.COBBLESTONE, HOUSE_BASE[1]))
		HOUSE_WALL.append(BuildingBlock(offset, HOUSE_INNER[0], block.AIR, HOUSE_INNER[1])) # fill inner with air
		HOUSE_WALL.append(BuildingBlock(offset, HOUSE_WEST_WALL[0], block.WOOD_PLANKS, HOUSE_WEST_WALL[1]))
		HOUSE_WALL.append(BuildingBlock(offset, HOUSE_NORTH_WALL[0], block.WOOD_PLANKS, HOUSE_NORTH_WALL[1]))
		HOUSE_WALL.append(BuildingBlock(offset, HOUSE_EAST_WALL[0], block.WOOD_PLANKS, HOUSE_EAST_WALL[1]))
		HOUSE_WALL.append(BuildingBlock(offset, HOUSE_SOUTH_WALL[0], block.WOOD_PLANKS, HOUSE_SOUTH_WALL[1]))
		HOUSE_WALL.append(LADDER)

		HOUSE_ROOF = []
		HOUSE_ROOF.append(BuildingBlock(offset, HOUSE_BASE[0], block.WOOD, HOUSE_BASE[1], OAK_UPDOWN))
		HOUSE_ROOF.append(BuildingBlock(offset, HOUSE_INNER[0], block.WOOD_PLANKS, HOUSE_INNER[1]))
		HOUSE_ROOF.append(BuildingBlock(offset, HOUSE_LADDER, block.AIR))
		HOUSE_ROOF.append(LADDER)

		self.layers.append(BuildingLayer(HOUSE_BASE, 0))
		
		walls = list(HOUSE_WALL)
		walls.append(BuildingBlock(offset, HOUSE_DOOR, block.AIR))
		self.layers.append(BuildingLayer(walls, 1))

		walls.append(BuildingBlock(offset, WINDOW_WEST, block.GLASS_PANE))
		walls.append(BuildingBlock(offset, WINDOW_NORTH, block.GLASS_PANE))
		walls.append(BuildingBlock(offset, WINDOW_EAST, block.GLASS_PANE))
		self.layers.append(BuildingLayer(walls, 2))

		walls = list(HOUSE_WALL)
		walls.append(Torch(offset, TORCH_POS, block.TORCH, None, Torch.NORTH))
		self.layers.append(BuildingLayer(HOUSE_WALL, 3))
		
		self.layers.append(BuildingLayer(HOUSE_ROOF, 4))
		
		fences = []
		fences.append(BuildingBlock(offset, ROOF_FENCE_WEST[0], block.FENCE, ROOF_FENCE_WEST[1]))
		fences.append(BuildingBlock(offset, ROOF_FENCE_NORTH[0], block.FENCE, ROOF_FENCE_NORTH[1]))
		fences.append(BuildingBlock(offset, ROOF_FENCE_EAST[0], block.FENCE, ROOF_FENCE_EAST[1]))
		fences.append(BuildingBlock(offset, ROOF_FENCE_SOUTH[0], block.FENCE, ROOF_FENCE_SOUTH[1]))
		self.layers.append(BuildingLayer(fences, 5))

		self._set_direction()
		
	def build(self, mc):
		super(SmallHouse, self).build(mc)
		
