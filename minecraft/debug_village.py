from village.debug import *

from village.tests import ApartmentBlockTester
from village.building import Building
from village.apartment_block import ApartmentBlock
from mcpi.vec3 import Vec3

def debug_apart_block():
	global mc
	ps = mc.player.getTilePos()

	apartments = ApartmentBlock(Building.NORTH)
	apartments.build_to_left(mc, ps + Vec3(14,0,-1))
	

if __name__ == "__main__":
# TODO tests these builds with large farm & apartment block added.
	#run_builds()
	#clear_builds()
	
	debug_apart_block()
	#test_current_buildings(mc)
