from building import Building, BuildingLayer, BuildingBlock
from oriented_block import Stair, Ladder, Torch
import mcpi.block as block
from mcpi.vec3 import Vec3

HOUSE_BASE = (Vec3(-2,0,2), Vec3(2,0,6))
HOUSE_INNER = (Vec3(-1,0,3), Vec3(1,0,5))
HOUSE_WEST_WALL = (Vec3(-2,0,3), Vec3(-1,0,5))
HOUSE_NORTH_WALL = (Vec3(-1,0,6), Vec3(1,0,6))
HOUSE_EAST_WALL = (Vec3(2,0,5), Vec3(2,0,3))
HOUSE_SOUTH_WALL = (Vec3(-1,0,2), Vec3(1,0,2))
HOUSE_DOOR = Vec3(0,0,2)

OAK_UPDOWN = 0

HOUSE_BASE = []
HOUSE_BASE.append(BuildingBlock(HOUSE_BASE[0], block.COBBLESTONE, HOUSE_BASE[1]))
HOUSE_BASE.append(Stair(Vec3(0,0,1), block.COBBLESTONE_STAIR, Vec3(0,0,0), Stair.NORTH)

LADDER = Ladder(Vec3(1,0,5), block.LADDER, Vec3(0,0,0), Ladder.NORTH)

HOUSE_WALL = []
HOUSE_BASE.append(BuildingBlock(HOUSE_BASE[0], block.COBBLESTONE, HOUSE_BASE[1]))
HOUSE_BASE.append(BuildingBlock(HOUSE_INNER[0], block.AIR, HOUSE_INNER[1])) # fill inner with air
HOUSE_BASE.append(BuildingBlock(HOUSE_WEST_WALL[0], block.WOOD_PLANKS, HOUSE_WEST_WALL[1]))
HOUSE_BASE.append(BuildingBlock(HOUSE_NORTH_WALL[0], block.WOOD_PLANKS, HOUSE_NORTH_WALL[1]))
HOUSE_BASE.append(BuildingBlock(HOUSE_EAST_WALL[0], block.WOOD_PLANKS, HOUSE_EAST_WALL[1]))
HOUSE_BASE.append(BuildingBlock(HOUSE_SOUTH_WALL[0], block.WOOD_PLANKS, HOUSE_SOUTH_WALL[1]))
HOUSE_BASE.append(LADDER)

HOUSE_ROOF = []
HOUSE_ROOF.append(BuildingBlock(HOUSE_BASE[0], block.WOOD, HOUSE_BASE[1], OAK_UPDOWN))
HOUSE_ROOF.append(BuildingBlock(HOUSE_INNER[0], block.WOOD_PLANKS, HOUSE_INNER[1]))
HOUSE_ROOF.append(BuildingBlock(Vec3(1,0,5), block.AIR))
HOUSE_ROOF.append(LADDER)


class SmallHouse(Building):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self.layers.append(BuildingLayer(HOUSE_BASE, 0)
		
		walls = list(HOUSE_WALL)
		walls.append(BuildingBlock(HOUSE_DOOR, block.AIR)
		self.layers.append(BuildingLayer(walls, 1)

		walls.append(BuildingBlock(Vec3(-2,0,4), block.GLASS_PANE)
		walls.append(BuildingBlock(Vec3(0,0,6), block.GLASS_PANE)
		walls.append(BuildingBlock(Vec3(2,0,4), block.GLASS_PANE)
		self.layers.append(BuildingLayer(walls, 2)

		walls = list(HOUSE_WALL)
		walls.append(Torch(vec3(0,0,3), block.TORCH, Vec3(0,0,0), Torch.NORTH)
		self.layers.append(BuildingLayer(HOUSE_WALL, 3)
		
		self.layers.append(BuildingLayer(HOUSE_ROOF, 4)
		
		fences = []
		fences.append(BuildingBlock(Vec3(-2,0,2), block.FENCE, Vec3(-2,0,6))
		fences.append(BuildingBlock(Vec3(-1,0,6), block.FENCE, Vec3(2,0,6))
		fences.append(BuildingBlock(Vec3(2,0,5), block.FENCE, Vec3(2,0,2))
		fences.append(BuildingBlock(Vec3(2,0,2), block.FENCE, Vec3(-1,0,2))
		self.layers.append(BuildingLayer(fences, 5)

	def build(self, mc):
		super().build(mc)
		
