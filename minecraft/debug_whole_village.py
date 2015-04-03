from village import *
from village.utils import setup_test_area
import mcpi.minecraft as minecraft
from mcpi.vec3 import Vec3

mc = minecraft.Minecraft.create()
pl = mc.player
cm = mc.camera

#LampPost, Vec3(0,0,0)
buildings = []

def setup_build_coords():
	global buildings

	x = 3
	z = -3
	buildings.append((Well, Vec3(x,0,z)))
	x += Well.WIDTH
	buildings.append((LampPost, Vec3(x,0,z)))
	x += 3
	buildings.append((SmallHouseV1, Vec3(x,0,z)))
	x += SmallHouseV1.WIDTH
	buildings.append((LampPost, Vec3(x,0,z)))
	x += 3
	buildings.append((SmallHouseV2, Vec3(x,0,z)))
	x += SmallHouseV2.WIDTH
	buildings.append((LampPost, Vec3(x,0,z)))
	x += 3
	buildings.append((SmallHouseV3, Vec3(x,0,z)))
	x += SmallHouseV3.WIDTH
	buildings.append((LampPost, Vec3(x,0,z)))

	x = 3
	z += -6 - 3
	buildings.append((Farm, Vec3(x,0,z)))
	x += Farm.WIDTH 
	buildings.append((LampPost, Vec3(x,0,z)))
	x += 3
	buildings.append((Library, Vec3(x,0,z)))
	x += Library.WIDTH
	buildings.append((LampPost, Vec3(x,0,z)))
	x += 3
	buildings.append((LargeHouse, Vec3(x,0,z)))
	x += LargeHouse.WIDTH
	buildings.append((LampPost, Vec3(x,0,z)))
	x += 3

	x = 3
	z += -9 - 3
	buildings.append((Church, Vec3(x,0,z)))
	x += Church.WIDTH
	buildings.append((LampPost, Vec3(x,0,z)))
	x += 3
	buildings.append((Butcher, Vec3(x,0,z)))
	x += Butcher.WIDTH
	z += -3
	buildings.append((LampPost, Vec3(x,0,z)))
	x += 3
	buildings.append((Blacksmith, Vec3(x,0,z)))
	x += Blacksmith.WIDTH
	buildings.append((LampPost, Vec3(x,0,z)))


	x = 0
	y = -1
	z = 0
	# build street running in front of houses
	for i in range(13):
		buildings.append((Street, Vec3(i * 3,y,z)))
	z = -9
	# build street running in front of second row of buildings
	for i in range(13):
		buildings.append((Street, Vec3(i * 3,y,z)))
	# build street running in front of third row of buildings
	z += -12
	for i in range(8):
		buildings.append((Street, Vec3(i * 3,y,z)))
	# adjust street for offset of blacksmith
	z += -3
	for i in range(7, 13):
		buildings.append((Street, Vec3(i * 3,y,z)))

	# build street running north on west side of buildings
	x = 0
	for  i in range(13):
		buildings.append((Street, Vec3(x,y,i*3)))

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

def build_village(mc, orientation, offset, build_right=True):
	global buildings

	_offset = offset.clone()
	if not build_right:
		_offset = Vec3(_offset.x * -1, _offset.y, _offset.z)
	
	for build_type, pos in buildings:
		_pos = pos
		if not build_right:
			_pos = Vec3(_pos.x * -1, _pos.y, _pos.z)

		build_pos= orient_pos(_offset + _pos, orientation) + pl.getTilePos()
		build = build_type(orientation)

		if build_right:
			build.build_to_right(mc, build_pos)
		else:
			build.build_to_left(mc, build_pos)

def run_builds(build_right=True):
	global mc
	
	setup_build_coords()
	offset = Vec3(3,0,-3)
	build_village(mc, Building.NORTH, offset, build_right)
	build_village(mc, Building.EAST, offset, build_right)
	build_village(mc, Building.SOUTH, offset, build_right)
	build_village(mc, Building.WEST, offset, build_right)

if __name__ == "__main__":
	run_builds()
	# clear space before running build left
	#run_builds(False)