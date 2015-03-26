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

def run_build_tests(klass, mc):
	tst = klass.create_tester(mc)
	tst.run(TEST_BUILD_ONLY)
	return tst

def clear_build_tests(tst):
	tst.run(TEST_CLEAR_ONLY)

if __name__ == "__main__":
	SLEEP_SECS = 0.1

	mc = minecraft.Minecraft.create()
	#run_all_tests(mc)
	tstV1 = SmallHouseV1Tester.create_tester(mc)
	tstV1.default_offset += Vec3(0,0,-5)
	tstV1.run(TEST_BUILD_ONLY)

	tstV2 = SmallHouseV2Tester.create_tester(mc)
	tstV2.default_offset += Vec3(10,0,-5)
	tstV2.run(TEST_BUILD_ONLY)

	tstV3 = SmallHouseV3Tester.create_tester(mc)
	tstV3.default_offset += Vec3(20,0,-5)
	tstV3.run(TEST_BUILD_ONLY)

	clear_build_tests(tstV1)
	clear_build_tests(tstV2)
	clear_build_tests(tstV3)
