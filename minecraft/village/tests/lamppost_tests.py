from village.tests.building_tests import BuildingTestsBase
from village.lamppost import LampPost
import village.direction
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
	
	def _get_offset(self):
		return  Vec3(0,0,2)
		
	def test_lamppost_north(self):
		offset = self._get_offset()
		wl = LampPost(self.pos + offset, direction.NORTH)
		self.run_lamppost_test(wl)
		
	def test_lamppost_east(self):
		offset = self._get_offset()
		offset.rotateRight()
		wl = LampPost(self.pos + offset, direction.EAST)
		self.run_lamppost_test(wl)
		
	def test_lamppost_south(self):
		offset = self._get_offset()
		offset.rotateRight()
		offset.rotateRight()
		wl = LampPost(self.pos + offset, direction.SOUTH)
		self.run_lamppost_test(wl)
		
	def test_lamppost_west(self):
		offset = self._get_offset()
		offset.rotateLeft()
		wl = LampPost(self.pos + offset, direction.WEST)
		self.run_lamppost_test(wl)
		
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
