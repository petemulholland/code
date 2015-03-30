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
		sut.build_to_right(self.mc, self.default_offset + self.pos)
		time.sleep(self.sleep)

	def _test_clear(self, sut):
		self.postToChat("Clearing {0}".format(self.sut_name))
		sut.clear_to_right(self.mc, self.default_offset + self.pos)
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
	def run_tests(klass, mc=None, test_flags=TEST_BUILD_CLEAR):
		tester = klass.create_tester(mc)
		tester.run(test_flags)
	

class BuildingTesterBase(TesterBase):
	def __init__(self, sut_type=None, *args, **kwargs):
		super(BuildingTesterBase, self).__init__(*args, **kwargs)
		self.sut_type = sut_type

	def _get_build_pos(self, sut, orientation):
		offset_depth = -2 - sut.width
		left_offset = Vec3(-2,0,offset_depth)
		right_offset = Vec3(2,0,offset_depth)
		if orientation == Building.WEST:		
			left_offset.rotateLeft()
			right_offset.rotateLeft()
		elif orientation == Building.EAST:		
			left_offset.rotateRight()
			right_offset.rotateRight()
		elif orientation == Building.SOUTH:	
			left_offset.rotateRight()
			left_offset.rotateRight()
			right_offset.rotateRight()
			right_offset.rotateRight()

		return (left_offset, right_offset)

	def _test_build(self, sut, orientation):
		offsets = self._get_build_pos(sut, orientation)
		
		self.postToChat("")
		self.postToChat("Building {0} to left of {1}".format(self.sut_name, offsets[0] + self.pos))
		sut.build_to_left(self.mc, offsets[0] + self.pos)
		self.postToChat("")
		self.postToChat("Building {0} to right of {1}".format(self.sut_name, offsets[1] + self.pos))
		sut.build_to_right(self.mc, offsets[1] + self.pos)

		time.sleep(self.sleep)

	def _test_clear(self, sut, orientation):
		offsets = self._get_build_pos(sut, orientation)

		self.postToChat("")
		self.postToChat("Clearing {0} to left of {1}".format(self.sut_name, offsets[0] + self.pos))
		sut.clear_to_left(self.mc, offsets[0] + self.pos)
		self.postToChat("")
		self.postToChat("Clearing {0} to right of {1}".format(self.sut_name, offsets[1] + self.pos))
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

		sut = self.sut_type(orientation=orientation)
		self._run_test(sut, orientation, test_flags)

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

