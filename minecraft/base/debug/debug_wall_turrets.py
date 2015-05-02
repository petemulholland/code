from base.enclosure.walls import CastleWallAndMoat, StraightWallTurret, CornerWallTurret
from debug_base import mc, pl
from building import Building
from mcpi.vec3 import Vec3

# TODO: add tests to create:
#		1. wall with moat (CastleWallAndMoat)
#			- in 4 directions making a square		
#			- need (8*2) + 16 = 32 & some space - 40
#		2. Corner turret on each corner
#		3. 1 straight wall turret on each wall, mirror 2 of them (east & south).

build_offset = Vec3(-1,0,-1)
global mc, ps
ps = mc.player.getTilePos()
ps += build_offset

def create_walls():
	wall = CastleWallAndMoat(40, Building.EAST)
	wall.build_to_left(mc, ps + Vec3(-1,0,0))

	wall = CastleWallAndMoat(40, Building.NORTH)
	wall.build_to_left(mc, ps + Vec3(0,0,-39))

	wall = CastleWallAndMoat(40, Building.WEST)
	wall.build_to_left(mc, ps + Vec3(-39,0,-39))

	wall = CastleWallAndMoat(40, Building.SOUTH)
	wall.build_to_left(mc, ps + Vec3(-39,0,0))

def create_corner_turrets():
	# north turrret on NE corner
	turret = CornerWallTurret(Building.NORTH)
	turret.build_to_left(mc, ps + Vec3(4,0,-36))
	# mirrored North turret on NW corner (give WEST with stairs in opposite direction)
	turret = CornerWallTurret(Building.NORTH)
	turret.mirror()
	turret.build_to_left(mc, ps + Vec3(-36,0,-36))
	# East turret on SE corner
	turret = CornerWallTurret(Building.EAST)
	turret.build_to_left(mc, ps + Vec3(4,0,4))
	# mirrored EAST on SW corner?
	turret = CornerWallTurret(Building.EAST)
	turret.mirror()
	turret.build_to_left(mc, ps + Vec3(-36,0,4))

def create_straight_turrets():
	pass

def debug_enclosure_walls():
	create_walls()
	create_corner_turrets()
	create_straight_turrets()
