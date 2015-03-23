from village.test.building_tests import BuildingTestsBase
from village.small_house import SmallHouse
import village.direction
from mcpi import minecraft
from mcpi.vec3 import Vec3
import time

SLEEP_SECS = 1

class SmallHouseTests(BuildingTestsBase):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	

	def _test_small_house_build(self, small_house):
		self.mc.postToChat("Building SmallHouse")
		small_house.build(self.mc)
		time.sleep(self.sleep)
		
	def _test_small_house_clear(self, small_house):
		self.mc.postToChat("Clearing SmallHouse")
		small_house.clear(self.mc)
		time.sleep(self.sleep)
		
	def _run_small_house_test(self, small_house):
		self._test_small_house_build(small_house)
		self._test_small_house_clear(small_house)
	
	def test_small_house_north(self):
		wl = SmallHouse(Vec3(0,0,1), direction.NORTH)
		self.run_small_house_test(wl)
		
	def test_small_house_east(self):
		wl = SmallHouse(Vec3(0,0,1), direction.EAST)
		self.run_small_house_test(wl)
		
	def test_small_house_south(self):
		wl = SmallHouse(Vec3(0,0,1), direction.SOUTH)
		self.run_small_house_test(wl)
		
	def test_small_house_west(self):
		wl = SmallHouse(Vec3(0,0,1), direction.WEST)
		self.run_small_house_test(wl)
		
	def run(self):
		super().run()

		self.test_small_house_north()
		self.test_small_house_east()
		self.test_small_house_south()
		self.test_small_house_west()
		
def run_small_house_tests():
	mc = minecraft.Minecraft.create()
	tester = SmallHouseTests(mc, SLEEP_SECS)
	tester.run()
