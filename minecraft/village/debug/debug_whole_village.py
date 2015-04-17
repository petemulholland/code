import time

from village import *
from village.utils import setup_test_area
from village.debug.debug_utils import mc, pl, cm

import mcpi.minecraft as minecraft
from mcpi.vec3 import Vec3

#LampPost, Vec3(0,0,0)
buildings = []
lampposts = []
streets = []

BUILD_BUILDINGS = True
BUILD_LAMPS = True
BUILD_STREETS = True

def setup_build_coords():
	global buildings, lampposts, streets

	x = 3
	z = -3
	buildings.append((Well, Vec3(x,0,z)))
	x += Well.WIDTH
	
	lampposts.append((LampPost, Vec3(x,0,z+1)))
	
	x += 3
	buildings.append((SmallHouseV1, Vec3(x,0,z)))
	x += SmallHouseV1.WIDTH
	
	lampposts.append((LampPost, Vec3(x,0,z+1)))
	
	x += 3
	buildings.append((SmallHouseV2, Vec3(x,0,z)))
	x += SmallHouseV2.WIDTH
	
	lampposts.append((LampPost, Vec3(x,0,z+1)))
	
	x += 3
	buildings.append((SmallHouseV3, Vec3(x,0,z)))
	x += SmallHouseV3.WIDTH
	
	lampposts.append((LampPost, Vec3(x,0,z+1)))

	x = 3
	z += -6 - 3
	buildings.append((Farm, Vec3(x,0,z)))
	x += Farm.WIDTH 
	
	lampposts.append((LampPost, Vec3(x,0,z+1)))
	
	x += 3
	buildings.append((Library, Vec3(x,0,z)))
	x += Library.WIDTH
	
	lampposts.append((LampPost, Vec3(x,0,z+1)))
	
	x += 3
	buildings.append((LargeHouse, Vec3(x,0,z)))
	x += LargeHouse.WIDTH
	
	lampposts.append((LampPost, Vec3(x,0,z+1)))


	x = 3
	z += -9 - 3
	buildings.append((Church, Vec3(x,0,z)))
	x += Church.WIDTH
	
	lampposts.append((LampPost, Vec3(x,0,z+1)))
	
	x += 3
	buildings.append((Butcher, Vec3(x,0,z)))
	x += Butcher.WIDTH
	z += -3
	
	lampposts.append((LampPost, Vec3(x,0,z+1)))
	
	x += 3
	buildings.append((Blacksmith, Vec3(x,0,z)))
	x += Blacksmith.WIDTH
	
	lampposts.append((LampPost, Vec3(x,0,z+1)))

	STREET_LEVEL = 0
	x = 0
	y = STREET_LEVEL
	z = 0
	# build street running in front of houses
	for i in range(13):
		streets.append((Street, Vec3(i * 3,y,z)))
	z = -9
	# build street running in front of second row of buildings
	for i in range(13):
		streets.append((Street, Vec3(i * 3,y,z)))
	# build street running in front of third row of buildings
	z += -12
	for i in range(8):
		streets.append((Street, Vec3(i * 3,y,z)))
	# adjust street for offset of blacksmith
	z += -3
	for i in range(7, 13):
		streets.append((Street, Vec3(i * 3,y,z)))

	# build street running north on west side of buildings
	x = 0
	for  i in range(13):
		streets.append((Street, Vec3(x,y,i*-3)))

def orient_pos(pos, orientation):
	ret = pos.clone()
	if orientation == Building.EAST:
		ret.rotateRight()
	elif orientation == Building.SOUTH:
		ret.rotateRight()
		ret.rotateRight()
	elif orientation == Building.WEST:
		ret.rotateLeft()

	return ret

def build_building(mc, build_type, pos, start_pos, orientation, offset, build_right=True):
	_pos = pos
	if not build_right:
		_pos = Vec3(_pos.x * -1, _pos.y, _pos.z)

	build_pos = orient_pos(offset + _pos, orientation) + start_pos
	build = build_type(orientation)

	if build_right:
		build.build_to_right(mc, build_pos)
	else:
		build.build_to_left(mc, build_pos)


def build_village(mc, start_pos, orientation, offset, build_right=True):
	global buildings, lampposts, street

	_offset = offset.clone()
	if not build_right:
		_offset = Vec3(_offset.x * -1, _offset.y, _offset.z)
	
	if BUILD_STREETS:
		for build_type, pos in streets:
			build_building(mc, build_type, pos, start_pos, orientation, _offset, build_right)

	if BUILD_LAMPS:
		for build_type, pos in lampposts:
			build_building(mc, build_type, pos, start_pos, orientation, _offset, build_right)

	if BUILD_BUILDINGS:
		for build_type, pos in buildings:
			build_building(mc, build_type, pos, start_pos, orientation, _offset, build_right)


def run_builds(build_right=True):
	global mc, pl
	
	setup_build_coords()
	offset = Vec3(3,0,-3)
	pos = pl.getTilePos()
	build_village(mc, pos, Building.NORTH, offset, build_right)
	build_village(mc, pos, Building.EAST, offset, build_right)
	build_village(mc, pos, Building.SOUTH, offset, build_right)
	build_village(mc, pos, Building.WEST, offset, build_right)

def clear_village(mc, start_pos, orientation, offset, build_right=True):
	global buildings

	_offset = offset.clone()
	if not build_right:
		_offset = Vec3(_offset.x * -1, _offset.y, _offset.z)
	
	for build_type, pos in buildings:
		_pos = pos
		if not build_right:
			_pos = Vec3(_pos.x * -1, _pos.y, _pos.z)

		build_pos= orient_pos(_offset + _pos, orientation) + start_pos
		build = build_type(orientation)

		if build_right:
			build.clear_to_right(mc, build_pos)
		else:
			build.clear_to_left(mc, build_pos)

def clear_builds(build_right=True):
	global mc, pl
	
	setup_build_coords()
	offset = Vec3(3,0,-3)
	pos = pl.getTilePos()
	clear_village(mc, pos, Building.NORTH, offset, build_right)
	clear_village(mc, pos, Building.EAST, offset, build_right)
	clear_village(mc, pos, Building.SOUTH, offset, build_right)
	clear_village(mc, pos, Building.WEST, offset, build_right)

if __name__ == "__main__":
	run_builds()
	clear_builds()

	#run_builds(False)
	#clear_builds(False)
	# clear space before running build left
	#run_builds(False)