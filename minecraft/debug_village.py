from village.tests import *
from village.building import SLEEP_SECS
from village.utils import setup_test_area
import mcpi.minecraft as minecraft

from mcpi import block
from mcpi.vec3 import Vec3

def run_all_tests(mc):
	setup_test_area(mc)
	
	BuildingBlockTester.run_tests(mc)
	BuildingLayerTester.run_tests(mc)
	BuildingTester.run_tests(mc)
	LampPostTester.run_tests(mc)
	WellTester.run_tests(mc)
	SmallHouseV1Tester.run_tests(mc)
	SmallHouseV2Tester.run_tests(mc)
	SmallHouseV3Tester.run_tests(mc)
	BlacksmithTester.run_tests(mc)
	ChurchTester.run_tests(mc)

def run_build_tests(klass, mc):
	tst = klass.create_tester(mc)
	tst.run(TEST_BUILD_ONLY)
	return tst

def clear_build_tests(tst):
	tst.run(TEST_CLEAR_ONLY)

def test_current_buildings(mc):
	tst = LampPostTester.create_tester(mc)
	tst.default_offset += Vec3(0,0,-2)
	tst.run(TEST_BUILD_ONLY)

	tst = SmallHouseV1Tester.create_tester(mc)
	tst.default_offset += Vec3(0,0,-5)
	tst.run(TEST_BUILD_ONLY)

	tst = SmallHouseV2Tester.create_tester(mc)
	tst.default_offset += Vec3(10,0,-5)
	tst.run(TEST_BUILD_ONLY)

	tst = SmallHouseV3Tester.create_tester(mc)
	tst.default_offset += Vec3(20,0,-5)
	tst.run(TEST_BUILD_ONLY)

	tst = WellTester.create_tester(mc)
	tst.default_offset += Vec3(0,0,-15)
	tst.run(TEST_BUILD_ONLY)

	tst = BlacksmithTester.create_tester(mc)
	tst.default_offset += Vec3(15,0,-15)
	tst.run(TEST_BUILD_ONLY)

	tst = ChurchTester.create_tester(mc)
	tst.default_offset += Vec3(25,0,-15)
	tst.run(TEST_BUILD_ONLY)



if __name__ == "__main__":
	SLEEP_SECS = 0.1

	mc = minecraft.Minecraft.create()
	#run_all_tests(mc)
	#test_house_variations(mc)

	BlacksmithTester.run_tests(mc)
	ChurchTester.run_tests(mc)
	#test_current_buildings(mc)