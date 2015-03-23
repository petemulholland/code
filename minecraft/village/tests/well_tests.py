from village.tests.building_tests import BuildingTestsBase
from village.well import Well
import village.direction
from mcpi import minecraft
from mcpi.vec3 import Vec3
import time

SLEEP_SECS = 1

class WellTests(BuildingTestsBase):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	

	def _test_well_build(self, well):
		self.mc.postToChat("Building Well")
		well.build(self.mc)
		time.sleep(self.sleep)
		
	def _test_well_clear(self, well):
		self.mc.postToChat("Clearing Well")
		well.clear(self.mc)
		time.sleep(self.sleep)
		
	def _run_well_test(self, well):
		self._test_well_build(well)
		self._test_well_clear(well)
	
	def test_well_north(self):
		wl = Well(Vec3(0,0,1), direction.NORTH)
		self.run_well_test(wl)
		
	def test_well_east(self):
		wl = Well(Vec3(0,0,1), direction.EAST)
		self.run_well_test(wl)
		
	def test_well_south(self):
		wl = Well(Vec3(0,0,1), direction.SOUTH)
		self.run_well_test(wl)
		
	def test_well_west(self):
		wl = Well(Vec3(0,0,1), direction.WEST)
		self.run_well_test(wl)
		
	def run(self):
		super().run()

		self.test_well_north()
		self.test_well_east()
		self.test_well_south()
		self.test_well_west()
		
def run_well_tests():
	mc = minecraft.Minecraft.create()
	tester = WellTests(mc, SLEEP_SECS)
	tester.run()
