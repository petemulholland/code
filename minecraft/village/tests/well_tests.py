from village.tests.building_tests import BuildingTestsBase
from village.well import Well
from village.building import Building
from mcpi import minecraft
from mcpi.vec3 import Vec3
import time

SLEEP_SECS = 0.5

# TODO: lots of common code in tests, how to move copy/paste to base class
# add create_building(orientation) method, & override in each test class.
# move _test_buils(), _test_clear(), _run_test(), test_oriented_north() etc to base
# pass _create_building() as param to methods (what about double set of block tests?)

class WellTests(BuildingTestsBase):
	def __init__(self, *args, **kwargs):
		super(WellTests, self).__init__(*args, **kwargs)

	def _test_well_build(self, well):
		self.postToChat("Building Well")
		well.build(self.mc)
		time.sleep(self.sleep)
		
	def _test_well_clear(self, well):
		self.postToChat("Clearing Well")
		well.clear(self.mc)
		time.sleep(self.sleep)
		
	def _run_well_test(self, well):
		self._test_well_build(well)
		self._test_well_clear(well)
	
	def test_well_north(self):
		self.postToChat("Well Test NORTH")
		wl = Well(self.default_offset, Building.NORTH)
		self._run_well_test(wl)
		
	def test_well_east(self):
		self.postToChat("Well Test EAST")
		wl = Well(self.default_offset, Building.EAST)
		self._run_well_test(wl)
		
	def test_well_south(self):
		self.postToChat("Well Test SOUTH")
		wl = Well(self.default_offset, Building.SOUTH)
		self._run_well_test(wl)
		
	def test_well_west(self):
		self.postToChat("Well Test WEST")
		wl = Well(self.default_offset, Building.WEST)
		self._run_well_test(wl)
		
	def run(self):
		super(WellTests, self).run()

		self.test_well_north()
		self.test_well_east()
		self.test_well_south()
		self.test_well_west()
		
def create_well_tester():
	mc = minecraft.Minecraft.create()
	return WellTests(mc, SLEEP_SECS)

def run_well_tests():
	tester = create_well_tester()
	tester.run()

