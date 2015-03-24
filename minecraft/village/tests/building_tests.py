from village.building import Building, BuildingLayer, BuildingBlock
from mcpi import minecraft
from mcpi.vec3 import Vec3
import mcpi.block as block
import time

SLEEP_SECS = 1
TEST_OUTPUT = False
DEFAULT_TEST_OFFSET = Vec3(0,0,1)

class BuildingTestsBase(object):
	def __init__(self, mc, sleep, sut_name):
		self.mc = mc
		self.sleep = sleep
		self.pos = None
		self.post_to_chat = TEST_OUTPUT
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

	def _run_test(self, sut):
		self._test_build(sut)
		time.sleep(self.sleep * 2)
		self._test_clear(sut)

	def test_sut(self, creator, orientation, orientation_display):
		self.postToChat("")
		self.postToChat("Testing {0} oriented {1}".format(self.sut_name, orientation_display))
		sut = creator(orientation)
		self._run_test(sut)

	def run(self, creator):
		self.set_pos()
		self.postToChat("")
		self.postToChat("Running tests for {0}".format(self.sut_name))
		self.postToChat("=================={0}".format("=" * len(self.sut_name)))
		
		self.test_sut(creator, Building.NORTH, "North")
		self.test_sut(creator, Building.EAST, "East")
		self.test_sut(creator, Building.SOUTH, "South")
		self.test_sut(creator, Building.WEST, "West")


		
class BuildingBlockTests(BuildingTestsBase):
	def __init__(self, *args, **kwargs):
		super(BuildingBlockTests, self).__init__(sut_name = "Block", *args, **kwargs)
	
	def _rotate_sut(self, sut, orientation):
		if orientation == Building.EAST:
			sut.rotateRight()
		elif orientation == Building.SOUTH:
			sut.rotateRight(2)
		elif orientation == Building.WEST:
			sut.rotateLeft()
		
		return sut

	def _create_single_block(self, orientation):
		sut = BuildingBlock(self.pos, Vec3(0, 0, 2), block.STONE)
		sut = self._rotate_sut(sut, orientation)
		return sut
	
	def _create_block_range(self, orientation):
		sut = BuildingBlock(self.pos, Vec3(-1, 0, 2), block.STONE, Vec3(1, 0, 2))
		sut = self._rotate_sut(sut, orientation)
		return sut

	def run(self):
		super(BuildingBlockTests, self).run(self._create_single_block)

		self.sut_name = "Block Range"
		super(BuildingBlockTests, self).run(self._create_block_range)


def create_block_tester():
	mc = minecraft.Minecraft.create()
	tester = BuildingBlockTests(mc, SLEEP_SECS)
	return tester

def run_block_tests():
	tester = create_block_tester()
	tester.run()

	
class BuildingLayerTests(BuildingTestsBase):
	def __init__(self, *args, **kwargs):
		super(BuildingLayerTests, self).__init__(sut_name = "Single part Building Layer", *args, **kwargs)

	def _rotate_sut(self, sut, orientation):
		if orientation == Building.EAST:
			sut.rotateRight()
		elif orientation == Building.SOUTH:
			sut.rotateRight(2)
		elif orientation == Building.WEST:
			sut.rotateLeft()
		
		return sut

	def _create_singlepart_layer(self, orientation):
		WELL_CORE = (Vec3(-1,0,2), Vec3(2,0,5))
		WELL_BASE = []
		WELL_BASE.append(BuildingBlock(self.pos, WELL_CORE[0], block.STONE, WELL_CORE[1]))
		sut = BuildingLayer(WELL_BASE, 0)
		sut = self._rotate_sut(sut, orientation)
		return sut
	
	def _create_multipart_layer(self, orientation):
		WELL_OUTER = (Vec3(-2,0,1), Vec3(3,0,6))
		WELL_CORE = (Vec3(-1,0,2), Vec3(2,0,5))
		WELL_INNER = (Vec3(0,0,3), Vec3(1,0,4))

		WELL_GROUND = []
		WELL_GROUND.append(BuildingBlock(self.pos, WELL_OUTER[0], block.GRAVEL, WELL_OUTER[1]))
		WELL_GROUND.append(BuildingBlock(self.pos, WELL_CORE[0], block.STONE, WELL_CORE[1]))
		WELL_GROUND.append(BuildingBlock(self.pos, WELL_INNER[0], block.WATER, WELL_INNER[1]))
		# TODO: add ladder, stair & torch to this & move up to ground level.

		sut = BuildingLayer(WELL_GROUND, 0)
		sut = self._rotate_sut(sut, orientation)
		return sut

	def run(self):
		super(BuildingLayerTests, self).run(self._create_singlepart_layer)

		self.sut_name = "Multi-part Building Layer"
		super(BuildingLayerTests, self).run(self._create_multipart_layer)
		

def create_layer_tester():
	mc = minecraft.Minecraft.create()
	return BuildingLayerTests(mc, SLEEP_SECS)

def run_layer_tests():
	tester = create_layer_tester()
	tester.run()

	
class BuildingTests(BuildingTestsBase):
	def __init__(self, *args, **kwargs):
		super(BuildingTests, self).__init__(sut_name = "Building", *args, **kwargs)

	def _create_building(self, orientation):
		WELL_OUTER = (Vec3(-2,0,1), Vec3(3,0,6))
		WELL_CORE = (Vec3(-1,0,2), Vec3(2,0,5))
		WELL_INNER = (Vec3(0,0,3), Vec3(1,0,4))

		WELL_BASE = []
		WELL_BASE.append(BuildingBlock(self.pos, WELL_CORE[0], block.STONE, WELL_CORE[1]))

		WELL_WATER = []
		WELL_WATER.append(BuildingBlock(self.pos, WELL_CORE[0], block.STONE, WELL_CORE[1]))
		WELL_WATER.append(BuildingBlock(self.pos, WELL_INNER[0], block.WATER, WELL_INNER[1]))

		WELL_GROUND = []
		WELL_GROUND.append(BuildingBlock(self.pos, WELL_OUTER[0], block.GRAVEL, WELL_OUTER[1]))
		WELL_GROUND.append(BuildingBlock(self.pos, WELL_CORE[0], block.STONE, WELL_CORE[1]))
		WELL_GROUND.append(BuildingBlock(self.pos, WELL_INNER[0], block.WATER, WELL_INNER[1]))

		WELL_WALLS = []
		WELL_WALLS.append(BuildingBlock(self.pos, WELL_CORE[0], block.STONE, WELL_CORE[1]))
		WELL_WALLS.append(BuildingBlock(self.pos, WELL_INNER[0], block.AIR, WELL_INNER[1]))

		WELL_SUPPORT = []
		WELL_SUPPORT.append(BuildingBlock(self.pos, Vec3(-1,0,2), block.FENCE))
		WELL_SUPPORT.append(BuildingBlock(self.pos, Vec3(-1,0,5), block.FENCE))
		WELL_SUPPORT.append(BuildingBlock(self.pos, Vec3(2,0,5), block.FENCE))
		WELL_SUPPORT.append(BuildingBlock(self.pos, Vec3(2,0,2), block.FENCE))
		
		bl = Building(Vec3(0,0,1), orientation)
		bl.layers.append(BuildingLayer(WELL_BASE, -3))
		bl.layers.append(BuildingLayer(WELL_WATER, -2))
		bl.layers.append(BuildingLayer(WELL_GROUND, -1))
		bl.layers.append(BuildingLayer(WELL_WALLS, 0))
		bl.layers.append(BuildingLayer(WELL_SUPPORT, 1))
		bl.layers.append(BuildingLayer(WELL_SUPPORT, 2))
		bl.layers.append(BuildingLayer(WELL_BASE, 3))
		
		# set_direction needs to be called after adding layers to building
		bl._set_orientation()
		return bl
	
	def run(self):
		super(BuildingTests, self).run(self._create_building)
		
		
def create_building_tester():
	mc = minecraft.Minecraft.create()
	return BuildingTests(mc, SLEEP_SECS)

def run_building_tests():
	tester = create_building_tester()
	tester.run()


if __name__ == "__main__":
	tst = create_building_tester()
	tst.test_building_east()
	