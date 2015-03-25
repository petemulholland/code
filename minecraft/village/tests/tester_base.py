from village.building import Building, SLEEP_SECS
from mcpi import minecraft
from mcpi.vec3 import Vec3
import mcpi.block as block
import time

IN_GAME_TEST_OUTPUT = False
DEFAULT_TEST_OFFSET = Vec3(0,0,1)

TEST_BUILD_ONLY = 1
TEST_CLEAR_ONLY = 2
TEST_BUILD_CLEAR = TEST_CLEAR_ONLY + TEST_BUILD_ONLY

class TesterBase(object):
	def __init__(self, mc, sleep, sut_name):
		self.mc = mc
		self.sleep = sleep
		self.pos = None
		self.post_to_chat = IN_GAME_TEST_OUTPUT
		self.default_offset = DEFAULT_TEST_OFFSET
		self.sut_name = sut_name

	def set_post_to_chat(self, do_post):
		self.post_to_chat = do_post

	def postToChat(self, msg):
		if self.post_to_chat:
			self.mc.postToChat(msg)
		else:
			print msg

	def set_pos(self):
		self.pos = self.mc.player.getTilePos()

	def _test_build(self, sut):
		self.postToChat("Building {0}".format(self.sut_name))
		sut.build(self.mc)
		time.sleep(self.sleep)

	def _test_clear(self, sut):
		self.postToChat("Clearing {0}".format(self.sut_name))
		sut.clear(self.mc)
		time.sleep(self.sleep)

	def _run_test(self, sut, test_flags):
		if (test_flags & TEST_BUILD_ONLY) > 0:
			self._test_build(sut)
			if (test_flags & TEST_CLEAR_ONLY) > 0:
				time.sleep(self.sleep * 2)

		if (test_flags & TEST_CLEAR_ONLY) > 0:
			self._test_clear(sut)

	def test_sut(self, creator, orientation, orientation_display, test_flags):
		self.postToChat("")
		self.postToChat("Testing {0} oriented {1}".format(self.sut_name, orientation_display))
		sut = creator(orientation)
		self._run_test(sut, test_flags)

	def run(self, creator, test_flags=TEST_BUILD_CLEAR):
		if self.pos is None:
			self.set_pos()

		self.postToChat("")
		self.postToChat("Running tests for {0}".format(self.sut_name))
		self.postToChat("=================={0}".format("=" * len(self.sut_name)))
		
		self.test_sut(creator, Building.NORTH, "North", test_flags)
		self.test_sut(creator, Building.EAST, "East", test_flags)
		self.test_sut(creator, Building.SOUTH, "South", test_flags)
		self.test_sut(creator, Building.WEST, "West", test_flags)


	@classmethod
	def create_tester(klass, mc=None):
		if mc is None:
			mc = minecraft.Minecraft.create()

		tester = klass(mc, SLEEP_SECS)
		return tester
	
	@classmethod
	def run_tests(klass, mc=None):
		tester = klass.create_tester(mc)
		tester.run()
	

