import time

import mcpi.minecraft as minecraft
from mcpi import block
from mcpi.vec3 import Vec3

from base.rooms.dining_hall import DiningHall
from building import Building
from mcpi.vec3 import Vec3

mc = minecraft.Minecraft.create()
pl = mc.player
cm = mc.camera

#build_pos = Vec3(0,0,-1)
build_pos = Vec3(0,0,0)

def debug_dining_hall():
	global mc
	ps = mc.player.getTilePos()

	build = DiningHall(Building.NORTH)
	build.build_to_left(mc, ps + Vec3(-1,0,-1))
	
def debug_building(type):
	global mc, build_pos
	ps = mc.player.getTilePos()
	ps += build_pos

	build = type(Building.NORTH)
	build.build_to_left(mc, ps + Vec3(build._width / 2,0,-2))

if __name__ == "__main__":
	debug_dining_hall()