import copy

import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

from building import Building, BuildingEx, BuildingBlock, SubBuilding, Torch, Stair, Door
from building.types import STAIRS_STONE_BRICK
from base.enclosure.walls.constants import *


################################################################
# class WallTurretMoat
################################################################
class WallTurretMoat(BuildingEx):
	''' class to create 1 quater section of moat around a turret 
		default orientation is north east
		Building.NORTH => north east
		Building.WEST => north west
		Building.SOUTH => south west
		Building.EAST => south east

		7 XX      
		6 wwXX    
		5 wwwwX   
		4 wwwwwX  
		3   wwwwX 
		2    wwwX 
		1     wwwX
		0     wwwX
		  76543210
		'''
	WIDTH = 8
	def __init__(self, *args, **kwargs):
		super(WallTurretMoat, self).__init__(width=WallTurretMoat.WIDTH, *args, **kwargs)
		self.base_level = WALL_DEPTH - 1
		self.moat_bottom = WALL_DEPTH
		self.nw_opened = False
		self.se_opened = False

	def clone(self):
		new_moat = super(WallTurretMoat, self).clone()
		new_moat.se_opened = copy.copy(self.se_opened)
		new_moat.nw_opened = copy.copy(self.nw_opened)
		return new_moat

	def _create_base(self):
		builds = []
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(0,self.base_level,0),
									block.DIRT,
									Building.SE_CORNER_POS + Vec3(-7,self.base_level,-7),
									description="turret moat base"))
		self._add_section("Wall turret moat - base", builds)
		 
	def _create_walls(self):
		builds = []
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(0,self.base_level+1,0),
									block.STONE_BRICK,
									Building.SE_CORNER_POS + Vec3(0,-1,-1),
									description="moat wall"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-1,self.base_level+1,-2),
									block.STONE_BRICK,
									Building.SE_CORNER_POS + Vec3(-1,-1,-3),
									description="moat wall"))

		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-2,self.base_level+1,-4),
									block.STONE_BRICK,
									Building.SE_CORNER_POS + Vec3(-2,-1,-4),
									description="moat wall"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-3,self.base_level+1,-5),
									block.STONE_BRICK,
									Building.SE_CORNER_POS + Vec3(-3,-1,-5),
									description="moat wall"))

		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-4,self.base_level+1,-6),
									block.STONE_BRICK,
									Building.SE_CORNER_POS + Vec3(-5,-1,-6),
									description="moat wall"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-6,self.base_level+1,-7),
									block.STONE_BRICK,
									Building.SE_CORNER_POS + Vec3(-7,-1,-7),
									description="moat wall"))

		self._add_section("Wall turret moat - walls", builds)

	def _create_water(self):
		builds = []
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-1,self.moat_bottom,0),
									block.AIR,
									Building.SE_CORNER_POS + Vec3(-3,-1,-1),
									description="moat - clear space down"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-2,self.moat_bottom,-2),
									block.AIR,
									Building.SE_CORNER_POS + Vec3(-4,-1,-3),
									description="moat - clear space down"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-3,self.moat_bottom,-4),
									block.AIR,
									Building.SE_CORNER_POS + Vec3(-3,-1,-4),
									description="moat - clear space down"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-4,self.moat_bottom,-3),
									block.AIR,
									Building.SE_CORNER_POS + Vec3(-5,-1,-5),
									description="moat - clear space down"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-6,self.moat_bottom,-4),
									block.AIR,
									Building.SE_CORNER_POS + Vec3(-7,-1,-6),
									description="moat - clear space down"))

		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-1,self.moat_bottom,0),
									block.WATER,
									Building.SE_CORNER_POS + Vec3(-3,WATER_HEIGHT,-1),
									description="moat water"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-2,self.moat_bottom,-2),
									block.WATER,
									Building.SE_CORNER_POS + Vec3(-4,WATER_HEIGHT,-3),
									description="moat water"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-3,self.moat_bottom,-4),
									block.WATER,
									Building.SE_CORNER_POS + Vec3(-3,WATER_HEIGHT,-4),
									description="moat water"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-4,self.moat_bottom,-3),
									block.WATER,
									Building.SE_CORNER_POS + Vec3(-5,WATER_HEIGHT,-5),
									description="moat water"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-6,self.moat_bottom,-4),
									block.WATER,
									Building.SE_CORNER_POS + Vec3(-7,WATER_HEIGHT,-6),
									description="moat water"))
		self._add_section("Wall turret moat - water", builds)

	def open_se_wall(self):
		self.se_opened = True

	def _clear_se_wall(self):
		#TODO: leaving blocks agains twall intact
		builds = []
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(0,WALL_DEPTH,0),
									block.WATER,
									Building.SE_CORNER_POS + Vec3(0,WATER_HEIGHT,-1),
									description="clear turret moat end- water"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(0,WATER_HEIGHT+1,0),
									block.AIR,
									Building.SE_CORNER_POS + Vec3(0,-1,-1),
									description="clear turret moat end- air bove water"))

		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-1,WALL_DEPTH,-2),
									block.WATER,
									Building.SE_CORNER_POS + Vec3(-1,WATER_HEIGHT,-2),
									description="clear turret moat end- water"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-1,WATER_HEIGHT+1,-2),
									block.AIR,
									Building.SE_CORNER_POS + Vec3(-1,-1,-2),
									description="clear turret moat end- air bove water"))

		self._add_section("Wall turret moat - clear SE opening", builds)

	def open_nw_wall(self):
		self.nw_opened = True

	def _clear_nw_wall(self):
		builds = []
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-6,WALL_DEPTH,-7),
									block.WATER,
									Building.SE_CORNER_POS + Vec3(-7,WATER_HEIGHT,-7),
									description="clear turret moat end- water"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-6,WATER_HEIGHT+1,-7),
									block.AIR,
									Building.SE_CORNER_POS + Vec3(-7,-1,-7),
									description="clear turret moat end- air bove water"))

		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-5,WALL_DEPTH,-6),
									block.WATER,
									Building.SE_CORNER_POS + Vec3(-5,WATER_HEIGHT,-6),
									description="clear turret moat end- water"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-5,WATER_HEIGHT+1,-6),
									block.AIR,
									Building.SE_CORNER_POS + Vec3(-5,-1,-6),
									description="clear turret moat end- air bove water"))
		self._add_section("Wall turret moat - clear NW opening", builds)

	def _create_structure(self):
		super(WallTurretMoat, self)._create_structure()
		self._create_base()
		self._create_walls()
		self._create_water()

		if self.se_opened:
			self._clear_se_wall()
		if self.nw_opened:
			self._clear_nw_wall()

