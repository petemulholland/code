from village.tests import *
from village.building import SLEEP_SECS
from village.building import Building
from village.utils import setup_test_area
from village.oriented_blocks import *

import mcpi.minecraft as minecraft

from mcpi import block
from mcpi.vec3 import Vec3
import time

from village.debug.debug_utils import mc, pl, cm

def debug_crops():
	global mc
	ps = mc.player.getTilePos()

	for z in range(-1,-10, -1):
		mc.setBlock(Vec3(ps.x, ps.y, ps.z + z), block.FARMLAND.withData(-(z) - 1))
		mc.setBlock(Vec3(ps.x, ps.y + 1, ps.z + z), Block(59,-(z) - 1))
	


if __name__ == "__main__":
	debug_crops()
