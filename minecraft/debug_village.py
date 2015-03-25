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

if __name__ == "__main__":
	SLEEP_SECS = 0.1

	mc = minecraft.Minecraft.create()

	#setup_test_area(mc)
	#LampPostTester.run_tests(mc)
	#BuildingBlockTester.run_tests(mc, TEST_BUILD_ONLY)
	BuildingBlockTester.run_tests(mc,TEST_BUILD_ONLY)
	BuildingLayerTester.run_tests(mc,TEST_BUILD_ONLY)
	BuildingTester.run_tests(mc,TEST_BUILD_ONLY)
	WellTester.run_tests(mc,TEST_BUILD_ONLY)
	LampPostTester.run_tests(mc,TEST_BUILD_ONLY)
	SmallHouseV1Tester.run_tests(mc,TEST_BUILD_ONLY)
	SmallHouseV2Tester.run_tests(mc,TEST_BUILD_ONLY)
	SmallHouseV3Tester.run_tests(mc,TEST_BUILD_ONLY)
