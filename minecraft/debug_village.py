from village.tests import *
from village.building import SLEEP_SECS
from village.utils import setup_test_area
import mcpi.minecraft as minecraft

if __name__ == "__main__":
	SLEEP_SECS = 0.1

	mc = minecraft.Minecraft.create()

	setup_test_area(mc)

	run_block_tests(mc)
	run_layer_tests(mc)
	run_building_tests(mc)
	run_lamppost_tests(mc)
	run_well_tests(mc)
	run_small_house_v1_tests(mc)
	run_small_house_v2_tests(mc)
	run_small_house_v3_tests(mc)
