from village.debug import *

from village.tests import ApartmentBlockTester
from building import Building
from village.apartment_block import ApartmentBlock
from village import *

from mcpi.vec3 import Vec3

def debug_apart_block():
	global mc
	ps = mc.player.getTilePos()

	#build_pos = Vec3(14,0,-1)
	build_pos = Vec3(0,0,0)
	apartments = ApartmentBlock(Building.NORTH)
	apartments.build_to_left(mc, ps + build_pos)
	

def debug_farms():
	global mc
	ps = mc.player.getTilePos()

	build = LargeFarm(Building.NORTH)
	build.build_to_right(mc, ps + Vec3(2,0,-2))
	
	build = Farm(Building.NORTH)
	build.build_to_left(mc, ps + Vec3(-2,0,-2))
	

if __name__ == "__main__":
# TODO tests these builds with large farm & apartment block added.
	#run_builds()
	#clear_builds()
	
	# TODO retry apartment block build with input ptompt between sections 
	#		to allow each section to complete before sending next
	debug_apart_block()
	#test_current_buildings(mc)
