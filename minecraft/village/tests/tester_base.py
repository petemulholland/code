from mcpi import minecraft
from mcpi.vec3 import Vec3
import mcpi.block as block
from village.building import Building, SLEEP_SECS
import time

IN_GAME_TEST_OUTPUT = False
DEFAULT_TEST_OFFSET = Vec3(0,0,-2)

TEST_BUILD_ONLY = 1
TEST_CLEAR_ONLY = 2
TEST_BUILD_CLEAR = TEST_CLEAR_ONLY + TEST_BUILD_ONLY

class TesterBase(object):
	def __init__(self, mc, sleep, sut_name, klass):
		self.mc = mc
		self.sleep = sleep
		self.pos = None
		self.post_to_chat = IN_GAME_TEST_OUTPUT
		self.default_offset = DEFAULT_TEST_OFFSET
		self.sut_name = sut_name
		self.klass = klass

	def set_post_to_chat(self, do_post):
		self.post_to_chat = do_post

	def postToChat(self, msg):
		if self.post_to_chat:
			self.mc.postToChat(msg)
		else:
			print msg

	def set_pos(self):
		self.pos = self.mc.player.getTilePos()

	def _get_build_pos(self, sut, orientation):
		offset_depth = -1 - sut.width
		left_offset = Vec3(-1,0,offset_depth)
		right_offset = Vec3(1,0,offset_depth)
		if orientation == Building.WEST:		
			left_offset.rotateLeft()
			right_offset.rotateLeft()
		elif orientation == Building.EAST:		
			left_offset.rotateRight()
			right_offset.rotateRight()
		elif orientation == Building.SOUTH:	
			left_offset.rotateRight(2)
			right_offset.rotateRight(2)

		return (left_offset, right_offset)

	def _test_build(self, sut, orientation):
		self.postToChat("Building {0}".format(self.sut_name))

		offsets = self._get_build_pos(sut, orientation)

		sut.build_to_left(self.mc, offsets[0] + self.pos)
		sut.build_to_right(self.mc, offsets[1] + self.pos)

		time.sleep(self.sleep)

	def _test_clear(self, sut, orientation):
		self.postToChat("Clearing {0}".format(self.sut_name))

		offsets = self._get_build_pos(sut, orientation)

		sut.clear_to_left(self.mc, offsets[0] + self.pos)
		sut.clear_to_right(self.mc, offsets[1] + self.pos)

		time.sleep(self.sleep)

	def _run_test(self, sut, orientation, test_flags):
		if (test_flags & TEST_BUILD_ONLY) > 0:
			self._test_build(sut, orientation)
			if (test_flags & TEST_CLEAR_ONLY) > 0:
				time.sleep(self.sleep * 2)

		if (test_flags & TEST_CLEAR_ONLY) > 0:
			self._test_clear(sut, orientation)

	def test_sut(self, orientation, orientation_display, test_flags):
		self.postToChat("")
		self.postToChat("Testing {0} oriented {1}".format(self.sut_name, orientation_display))
		sut = self.klass(orientation)
		self._run_test(sut, test_flags, orientation)

	def run(self, test_flags=TEST_BUILD_CLEAR):
		if self.pos is None:
			self.set_pos()

		self.postToChat("")
		self.postToChat("Running tests for {0}".format(self.sut_name))
		self.postToChat("=================={0}".format("=" * len(self.sut_name)))
		
		self.test_sut(Building.NORTH, "North", test_flags)
		self.test_sut(Building.EAST, "East", test_flags)
		self.test_sut(Building.SOUTH, "South", test_flags)
		self.test_sut(Building.WEST, "West", test_flags)

	# TODO: want to search methods on class to return _create_* method for each tester.

	@classmethod
	def create_tester(klass, mc=None):
		if mc is None:
			mc = minecraft.Minecraft.create()

		tester = klass(mc, SLEEP_SECS)
		return tester
	
	@classmethod
	def run_tests(klass, mc=None, test_flags=TEST_BUILD_CLEAR):
		tester = klass.create_tester(mc)
		tester.run(test_flags)
	

