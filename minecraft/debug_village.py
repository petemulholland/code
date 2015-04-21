from village.debug import *

from village.tests import ApartmentBlockTester
from village.building import Building
from village.apartment_block import ApartmentBlock
from mcpi.vec3 import Vec3

if __name__ == "__main__":
#	run_builds()
#	clear_builds()
	
	#ApartmentBlockTester.run_tests(mc)
	apartments = ApartmentBlock(Building.NORTH)
	apartments.build_to_left(mc, Vec3(0,0,0))

	#test_current_buildings(mc)
