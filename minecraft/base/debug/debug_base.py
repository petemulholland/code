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


def debug_dining_hall():
	global mc
	ps = mc.player.getTilePos()

	build = DiningHall(Building.NORTH)
	build.build_to_left(mc, ps + Vec3(-1,0,-1))
	
if __name__ == "__main__":
	debug_dining_hall()