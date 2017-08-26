import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

from building import Building, BuildingEx, BuildingBlock, SubBuilding, Torch, Stair, Door
from building.types import STAIRS_STONE_BRICK
from base.enclosure.walls.constants import *

################################################################
# class CastleWallAndMoat
################################################################
class CastleWallAndMoat(BuildingEx):
	''' Straight wall with moat 
		ssssss 5
		wwwwww 4
		wwwwww 3
		wwwwww 2
		ssssss 1
		ssssss 0
		...210
	''' 
	def __init__(self, wall_length, *args, **kwargs):
		super(CastleWallAndMoat, self).__init__(width=wall_length, *args, **kwargs)
		self.length = wall_length
		self.height = WALL_HEIGHT - 1
		self.foundation_depth = WALL_DEPTH
		self.base_level = WALL_DEPTH - 1
		self.x2 = -1 * (self.length - 1)

	def _create_wall(self):
		builds = []
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(0,self.foundation_depth,0),
									block.STONE_BRICK,
									Building.SE_CORNER_POS + Vec3(self.x2,self.height, -1),
									description="Wall"))

		# overhang & fences on top
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(0,self.height,-2),
									block.STONE_BRICK,
									Building.SE_CORNER_POS + Vec3(self.x2,self.height, -2),
									description="Wall overhang"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(0,self.height,-3),
									block.FENCE,
									Building.SE_CORNER_POS + Vec3(self.x2,self.height+1, -3),
									description="Wall fences"))
		self._add_section("Wall - stone brick wall", builds)

	def _create_moat(self):
		builds = []
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(0,self.base_level,-2),
									block.DIRT,
									Building.SE_CORNER_POS + Vec3(self.x2,self.base_level, -5),
									description="Wall moat base"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(0,self.foundation_depth,-5),
									block.STONE_BRICK,
									Building.SE_CORNER_POS + Vec3(self.x2,-1,-5),
									description="moat outer wall"))

		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(0,self.foundation_depth,-2),
									block.WATER,
									Building.SE_CORNER_POS + Vec3(self.x2,-2,-4),
									description="moat water"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(0,-1,-2),
									block.AIR,
									Building.SE_CORNER_POS + Vec3(self.x2,-1,-4),
									description="clear blocks over water"))
		self._add_section("Wall - moat", builds)

	def _create_structure(self):
		super(CastleWallAndMoat, self)._create_structure()
		self._create_wall()
		self._create_moat()

