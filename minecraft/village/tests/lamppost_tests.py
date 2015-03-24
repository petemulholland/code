from village.tests.building_tests import BuildingTestsBase
from village.building import Building
from village.lamppost import LampPost
from mcpi import minecraft
from mcpi.vec3 import Vec3
import time

SLEEP_SECS = 0.5

class LampPostTests(BuildingTestsBase):
	def __init__(self, *args, **kwargs):
		super(LampPostTests, self).__init__(*args, **kwargs)

	def _test_lamppost_build(self, lamppost):
		self.postToChat("Building LampPost")
		lamppost.build(self.mc)
		time.sleep(self.sleep)
		
	def _test_lamppost_clear(self, lamppost):
		self.postToChat("Clearing LampPost")
		lamppost.clear(self.mc)
		time.sleep(self.sleep)
		
	def _run_lamppost_test(self, lamppost):
		self._test_lamppost_build(lamppost)
		self._test_lamppost_clear(lamppost)
	
	def test_lamppost_north(self):
		self.postToChat("Lamppost Test NORTH")
		wl = LampPost(self.default_offset, Building.NORTH)
		self._run_lamppost_test(wl)
		
	def test_lamppost_east(self):
		self.postToChat("Lamppost Test EAST")
		wl = LampPost(self.default_offset, Building.EAST)
		self._run_lamppost_test(wl)
		
	def test_lamppost_south(self):
		self.postToChat("Lamppost Test SOUTH")
		wl = LampPost(self.default_offset, Building.SOUTH)
		self._run_lamppost_test(wl)
		
	def test_lamppost_west(self):
		self.postToChat("Lamppost Test WEST")
		wl = LampPost(self.default_offset, Building.WEST)
		self._run_lamppost_test(wl)
		
	def run(self):
		super(LampPostTests, self).run()

		self.test_lamppost_north()
		self.test_lamppost_east()
		self.test_lamppost_south()
		self.test_lamppost_west()
		
def create_lamppost_tester():
	mc = minecraft.Minecraft.create()
	return LampPostTests(mc, SLEEP_SECS)

def run_lamppost_tests():
	tester = create_lamppost_tester()
	tester.run()
