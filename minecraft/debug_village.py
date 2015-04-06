from village.tests import *
from village.building import SLEEP_SECS
from village.utils import setup_test_area
import mcpi.minecraft as minecraft

from mcpi import block
from mcpi.vec3 import Vec3

from village.building import Building

mc = minecraft.Minecraft.create()
pl = mc.player
cm = mc.camera

def connect():
	global mc, pl, cm
	mc = minecraft.Minecraft.create()
	pl = mc.player
	cm = mc.camera

def test_pl_pos():
	global mc, pl, cm

	ps = pl.getPos()
	print "Player pos: " + str(ps)
	pl.setPos(ps + Vec3(20,0,-15))
	ps = pl.getPos()
	print "Player pos: " + str(ps)



def run_all_tests(mc):
	setup_test_area(mc)
	
	#BuildingBlockTester.run_tests(mc)
	#BuildingLayerTester.run_tests(mc)
	#BuildingTester.run_tests(mc)

	LampPostTester.run_tests(mc)

	WellTester.run_tests(mc)
	SmallHouseV1Tester.run_tests(mc)
	SmallHouseV2Tester.run_tests(mc)
	SmallHouseV3Tester.run_tests(mc)

	FarmTester.run_tests(mc)
	LibraryTester.run_tests(mc)
	LargeHouseTester.run_tests(mc)

	ChurchTester.run_tests(mc)
	ButcherTester.run_tests(mc)
	BlacksmithTester.run_tests(mc)
	

def run_build_tests(klass, mc):
	tst = klass.create_tester(mc)
	tst.run(TEST_BUILD_ONLY)
	return tst

def clear_build_tests(tst):
	tst.run(TEST_CLEAR_ONLY)

def test_current_buildings(mc):
	tests = [(LampPostTester, "Lamp post"),
			(WellTester, "Well"),
			(SmallHouseV1Tester, "SmallHouseV1"),
			(SmallHouseV2Tester, "SmallHouseV2"),
			(SmallHouseV3Tester, "SmallHouseV3"),
			(FarmTester, "Farm"),
			(LibraryTester, "Library"),
			(LargeHouseTester, "LargeHouse"),
			(ChurchTester, "Church"),
			(ButcherTester, "Butcher"),
			(BlacksmithTester, "Blacksmith")]

	for tester, desc in tests:
		print "Running %s tests"%(desc)
		tst = run_build_tests(tester, mc)
		raw_input("Press Enter to clear and run next tests ...")
		clear_build_tests(tst)


def slow_build_all_buildings(mc):
	''' Build all buildings with 1 sec delay between layers,
		buildings in a line, move player to front of each new building before starting build '''

	 # test class, building offset, building width, relative offset from pl pos
	tests = [(WellTester, Vec3(-45,0,0), 6, Vec3(-3,0,-2)),
			(SmallHouseV1Tester, Vec3(-37,0,0), 6, Vec3(0,0,-2)),
			(SmallHouseV2Tester, Vec3(-29,0,0), 4, Vec3(0,0,-2)),
			(SmallHouseV3Tester, Vec3(-23,0,0), 4, Vec3(0,0,-2)),
			(LargeHouseTester, Vec3(-17,0,0), 9, Vec3(0,0,-2)),
			(FarmTester, Vec3(-6,0,0), 7, Vec3(0,0,-2)),
			(BlacksmithTester, Vec3(3,0,0), 10, Vec3(3,0,-2)),
			(ButcherTester, Vec3(15,0,0), 9, Vec3(0,0,-2)),
			(ChurchTester, Vec3(26,0,0), 5, Vec3(0,0,-2)),
			(LibraryTester, Vec3(33,0,0), 9, Vec3(4,0,-2))]

	pos = mc.player.getTilePos()

	for tester, offset, width, rel_offset in tests:
		tst = tester.create_tester(mc)

		plpos = pos + offset + Vec3(width/2,0,0)
		mc.player.setTilePos(plpos)
		mc.camera.setPos(plpos + Vec3(0,10,0))

		tst.default_offset = rel_offset
		tst.set_pos()
		tst.test_sut(tst._create_building, Building.NORTH, "North", TEST_BUILD_ONLY)

def debug_blocks(x1, y1, z1, x2, y2, z2):
	global mc
	ps = mc.player.getTilePos()

	xd = 1
	if x1 > x2:
		xd = -1
	print "DBG x: %d -> %d, delta: %d  \trange: %s"%(x1, x2, xd, range(x1, x2 + xd, xd))
	
	yd = 1
	if y1 > y2:
		yd = -1
	print "DBG y: %d -> %d, delta: %d  \trange: %s"%(y1, y2, yd, range(y1, y2 + yd, yd))

	zd = 1
	if z1 > z2:
		zd = -1
	print "DBG z: %d -> %d, delta: %d  \trange: %s"%(z1, z2, zd, range(z1, z2 + zd, zd))
	#print "DBG: player pos: " + str(ps)
	
	print "z:  y x",
	for x in range(x1, x2 + xd, xd):
		print "      %03d"%(ps.x + x),
	
	print ""
	#print "DBG: x header printed, printing z & y data"
	
	for z in range(z1, z2 + zd, zd):
		#print "DBG: in z loop z:%d"%(z)
		for y in range(y1, y2 + yd, yd):
			#print "DBG: in y loop y:%d"%(y)
			print "%03d - %d "%(ps.z + z, ps.y + y),
			for x in range(x1, x2 + xd, xd):
				#print "DBG: in x loop x:%d"%(x)
				print "  " + str(mc.getBlockWithData(ps.x + x, ps.y + y, ps.z + z)),
			
			print ""	
	
if __name__ == "__main__":
	global SLEEP_SECS
	SLEEP_SECS = 0.1

	#run_all_tests(mc)

	#test_house_variations(mc)
	test_current_buildings(mc)

	#slow_build_all_buildings(mc)

