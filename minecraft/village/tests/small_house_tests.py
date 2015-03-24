from village.tests.building_tests import BuildingTestsBase
from village.small_house import SmallHouse
from village.building import Building
from mcpi import minecraft
from mcpi.vec3 import Vec3
import time

SLEEP_SECS = 0.5

# TODO: lots of common code in tests, how to move copy/paste to base class
# add create_building(orientation) method, & override in each test class.
# move _test_buils(), _test_clear(), _run_test(), test_oriented_north() etc to base
# pass _create_building() as param to methods (what about double set of block tests?)
class SmallHouseTests(BuildingTestsBase):
	def __init__(self, *args, **kwargs):
		super(SmallHouseTests, self).__init__(*args, **kwargs)

	def _test_small_house_build(self, small_house):
		self.postToChat("Building SmallHouse")
		small_house.build(self.mc)
		time.sleep(self.sleep)
		
	def _test_small_house_clear(self, small_house):
		self.postToChat("Clearing SmallHouse")
		small_house.clear(self.mc)
		time.sleep(self.sleep)
		
	def _run_small_house_test(self, small_house):
		self._test_small_house_build(small_house)
		self._test_small_house_clear(small_house)
	
	def test_small_house_north(self):
		self.postToChat("Small House Test NORTH")
		wl = SmallHouse(self.default_offset, Building.NORTH)
		self._run_small_house_test(wl)
		
	def test_small_house_east(self):
		self.postToChat("Small House Test EAST")
		wl = SmallHouse(self.default_offset, Building.EAST)
		self._run_small_house_test(wl)
		
	def test_small_house_south(self):
		self.postToChat("Small House Test SOUTH")
		wl = SmallHouse(self.default_offset, Building.SOUTH)
		self._run_small_house_test(wl)
		
	def test_small_house_west(self):
		self.postToChat("Small House Test WEST")
		wl = SmallHouse(self.default_offset, Building.WEST)
		self._run_small_house_test(wl)
		
	def run(self):
		super(SmallHouseTests, self).run()

		self.test_small_house_north()
		self.test_small_house_east()
		self.test_small_house_south()
		self.test_small_house_west()
		
def create_small_house_tester():
	mc = minecraft.Minecraft.create()
	return SmallHouseTests(mc, SLEEP_SECS)

def run_small_house_tests():
	tester = create_small_house_tester()
	tester.run()

if __name__ == "__main__":
	run_small_house_tests()
