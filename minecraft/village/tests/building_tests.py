from village.building import Building, BuildingLayer, BuildingBlock
import village.direction
from mcpi import minecraft
from mcpi.vec3 import Vec3
import mcpi.block as block
import time

SLEEP_SECS = 1

class BuildingTestsBase(object):
	def __init__(self, mc, sleep):
		self.mc = mc
		self.sleep = sleep
		self.pos = None
		self.post_to_chat = False

	def set_post_to_chat(self, do_post):
		self.post_to_chat = do_post

	def postToChat(self, msg):
		if self.post_to_chat:
			self.mc.postToChat(msg)

	def run(self):
		self.pos = self.mc.player.getTilePos()
		
class BuildingBlockTests(BuildingTestsBase):
	def __init__(self, *args, **kwargs):
		super(BuildingBlockTests, self).__init__(*args, **kwargs)
	
	def _test_block_build(self, block):
		self.postToChat("Building Block")
		block.build(self.mc)
		time.sleep(self.sleep)
		
	def _test_block_clear(self, block):
		self.postToChat("Clearing Block")
		block.clear(self.mc)
		time.sleep(self.sleep)
		
	def _run_block_test(self, block):
		self._test_block_build(block)
		self._test_block_clear(block)
	
	def _create_single_block(self):
		bl = BuildingBlock(self.pos, Vec3(0, 0, 2), block.STONE)
		return bl
	
	def _create_block_range(self):
		bl = BuildingBlock(self.pos, Vec3(-1, 0, 2), block.STONE, Vec3(1, 0, 2))
		return bl

	def test_single_block(self):
		bl = self._create_single_block()
		self.postToChat("Single Block Test")
		self._run_block_test(bl)
		
	def test_single_block_rot90(self):
		bl = self._create_single_block()
		self.postToChat("Single Block Test rotated 90")
		bl.rotateRight()
		self._run_block_test(bl)
		
	def test_single_block_rot180(self):
		bl = self._create_single_block()
		self.postToChat("Single Block Test rotated 180")
		bl.rotateRight(2)
		self._run_block_test(bl)
		
	def test_single_block_rot270(self):
		bl = self._create_single_block()
		self.postToChat("Single Block Test rotated 270")
		bl.rotateLeft()
		self._run_block_test(bl)
		
	def test_block_range(self):
		bl = self._create_block_range()
		self.postToChat("Block Range Test")
		self._run_block_test(bl)
		
	def test_block_range_rot90(self):
		bl = self._create_block_range()
		self.postToChat("Block Range Test rotated 90")
		bl.rotateRight()
		self._run_block_test(bl)
		
	def test_block_range_rot180(self):
		bl = self._create_block_range()
		self.postToChat("Block Range Test rotated 180")
		bl.rotateRight(2)
		self._run_block_test(bl)
		
	def test_block_range_rot270(self):
		bl = self._create_block_range()
		self.postToChat("Block Range Test rotated 270")
		bl.rotateLeft()
		self._run_block_test(bl)
		
	def run(self):
		super(BuildingBlockTests, self).run()

		self.test_single_block()
		self.test_single_block_rot90()
		self.test_single_block_rot180()
		self.test_single_block_rot270()
		
		self.test_block_range()
		self.test_block_range_rot90()
		self.test_block_range_rot180()
		self.test_block_range_rot270()


def create_block_tester():
	mc = minecraft.Minecraft.create()
	tester = BuildingBlockTests(mc, SLEEP_SECS)
	return tester

def run_block_tests():
	tester = create_block_tester()
	tester.run()

	
class BuildingLayerTests(BuildingTestsBase):
	def __init__(self, **kwargs):
		super(BuildingLayerTests, self).__init__(**kwargs)

	def _test_layer_build(self, layer):
		self.postToChat("Building Layer")
		layer.build(self.mc)
		time.sleep(self.sleep)
		
	def _test_layer_clear(self, layer):
		self.postToChat("Clearing Layer")
		layer.clear(self.mc)
		time.sleep(self.sleep)
		
	def _run_layer_test(self, layer):
		self._test_layer_build(layer)
		self._test_layer_clear(layer)
	
	def _create_singlepart_layer(self):
		WELL_CORE = (Vec3(-1,0,2), Vec3(2,0,5))
		WELL_BASE = []
		WELL_BASE.append(BuildingBlock(WELL_CORE[0], block.STONE, WELL_CORE[1]))
		return BuildingLayer(WELL_BASE, -1)
	
	def _create_multipart_layer(self):
		WELL_OUTER = (Vec3(-2,0,1), Vec3(3,0,6))
		WELL_CORE = (Vec3(-1,0,2), Vec3(2,0,5))
		WELL_INNER = (Vec3(0,0,3), Vec3(1,0,4))

		WELL_GROUND = []
		WELL_GROUND.append(BuildingBlock(WELL_OUTER[0], block.GRAVEL, WELL_OUTER[1]))
		WELL_GROUND.append(BuildingBlock(WELL_CORE[0], block.STONE, WELL_CORE[1]))
		WELL_GROUND.append(BuildingBlock(WELL_INNER[0], block.WATER, WELL_INNER[1]))

		return BuildingLayer(WELL_GROUND, -1)

	def test_singlepart_layer(self):
		ly = self._create_singlepart_layer()
		self.postToChat("Single Layer Test")
		self._run_layer_test(ly)
		
	def test_singlepart_layer_rot90(self):
		ly = self._create_singlepart_layer()
		self.postToChat("Single Layer Test rotated 90")
		ly.rotateRight()
		self._run_layer_test(ly)
		
	def test_singlepart_layer_rot180(self):
		ly = self._create_singlepart_layer()
		self.postToChat("Single Layer Test rotated 180")
		ly.rotateRight(2)
		self._run_layer_test(ly)
		
	def test_singlepart_layer_rot270(self):
		ly = self._create_singlepart_layer()
		self.postToChat("Single Layer Test rotated 270")
		ly.rotateLeft()
		self._run_layer_test(ly)
		
	def test_multipart_layer(self):
		ly = self._create_multipart_layer()
		self.postToChat("Multipart Layer Test")
		self._run_layer_test(ly)
		
	def test_multipart_layer_rot90(self):
		ly = self._create_multipart_layer()
		self.postToChat("Multipart Layer Test rotated 90")
		ly.rotateRight()
		self._run_layer_test(ly)
		
	def test_multipart_layer_rot180(self):
		ly = self._create_multipart_layer()
		self.postToChat("Multipart Layer Test rotated 180")
		ly.rotateRight(2)
		self._run_layer_test(ly)
		
	def test_multipart_layer_rot270(self):
		ly = self._create_multipart_layer()
		self.postToChat("Multipart Layer Test rotated 270")
		ly.rotateLeft()
		self._run_layer_test(ly)
		
	def run(self):
		super(BuildingLayerTests, self).run()
		
		self.test_singlepart_layer()
		self.test_singlepart_layer_rot90()
		self.test_singlepart_layer_rot180()
		self.test_singlepart_layer_rot270()
		
		self.test_multipart_layer()
		self.test_multipart_layer_rot90()
		self.test_multipart_layer_rot180()
		self.test_multipart_layer_rot270()
		

def create_layer_tester():
	mc = minecraft.Minecraft.create()
	return BuildingLayerTests(mc, SLEEP_SECS)

def run_layer_tests():
	tester = create_layer_tester()
	tester.run()

	
class BuildingTests(BuildingTestsBase):
	def __init__(self, **kwargs):
		super(BuildingTests, self).__init__(**kwargs)

	def _test_building_build(self, building):
		self.postToChat("Building building")
		building.build(self.mc)
		time.sleep(self.sleep)
		
	def _test_building_clear(self, building):
		self.postToChat("Clearing building")
		building.clear(self.mc)
		time.sleep(self.sleep)
		
	def _run_building_test(self, block):
		self._test_building_build(block)
		self._test_building_clear(block)
	
	def _create_building(self, orientation):
		WELL_OUTER = (Vec3(-2,0,1), Vec3(3,0,6))
		WELL_CORE = (Vec3(-1,0,2), Vec3(2,0,5))
		WELL_INNER = (Vec3(0,0,3), Vec3(1,0,4))

		WELL_BASE = []
		WELL_BASE.append(BuildingBlock(WELL_CORE[0], block.STONE, WELL_CORE[1]))

		WELL_WATER = []
		WELL_WATER.append(BuildingBlock(WELL_CORE[0], block.STONE, WELL_CORE[1]))
		WELL_WATER.append(BuildingBlock(WELL_INNER[0], block.WATER, WELL_INNER[1]))

		WELL_GROUND = []
		WELL_GROUND.append(BuildingBlock(WELL_OUTER[0], block.GRAVEL, WELL_OUTER[1]))
		WELL_GROUND.append(BuildingBlock(WELL_CORE[0], block.STONE, WELL_CORE[1]))
		WELL_GROUND.append(BuildingBlock(WELL_INNER[0], block.WATER, WELL_INNER[1]))

		WELL_WALLS = []
		WELL_WALLS.append(BuildingBlock(WELL_CORE[0], block.STONE, WELL_CORE[1]))
		WELL_WALLS.append(BuildingBlock(WELL_INNER[0], block.AIR, WELL_INNER[1]))

		WELL_SUPPORT = []
		WELL_SUPPORT.append(BuildingBlock(Vec3(-1,0,2), block.FENCE))
		WELL_SUPPORT.append(BuildingBlock(Vec3(-1,0,5), block.FENCE))
		WELL_SUPPORT.append(BuildingBlock(Vec3(2,0,5), block.FENCE))
		WELL_SUPPORT.append(BuildingBlock(Vec3(2,0,2), block.FENCE))
		
		bl = Building(Vec3(0,0,1), orientation)
		bl.layers.append(BuildingLayer(WELL_BASE, -3))
		bl.layers.append(BuildingLayer(WELL_WATER, -2))
		bl.layers.append(BuildingLayer(WELL_GROUND, -1))
		bl.layers.append(BuildingLayer(WELL_WALLS, 0))
		bl.layers.append(BuildingLayer(WELL_SUPPORT, 1))
		bl.layers.append(BuildingLayer(WELL_SUPPORT, 2))
		bl.layers.append(BuildingLayer(WELL_BASE, 3))
		
		return bl
	
	def test_building_north(self):
		bl = self._create_building(direction.NORTH)
		self.postToChat("Building Test direction NORTH")
		self._run_building_test(bl)
		
	def test_building_east(self):
		bl = self._create_building(direction.EAST)
		self.postToChat("Building Test direction EAST")
		self._run_building_test(bl)
		
	def test_building_south(self):
		bl = self._create_building(direction.SOUTH)
		self.postToChat("Building Test direction SOUTH")
		self._run_building_test(bl)
		
	def test_building_west(self):
		bl = self._create_building(direction.WEST)
		self.postToChat("Building Test direction WEST")
		self._run_building_test(bl)
		
	def run(self):
		super(BuildingTests, self).run()
		
		self.test_building_north()
		self.test_building_east()
		self.test_building_south()
		self.test_building_west()
		
def create_building_tester():
	mc = minecraft.Minecraft.create()
	return BuildingTests(mc, SLEEP_SECS)

def run_building_tests():
	tester = create_building_tester()
	tester.run()


if __name__ == "__main__":
	run_block_tests()