from village.building import Building, BuildingLayer, BuildingBlock
from mcpi import minecraft
from mcpi.vec3 import Vec3
import mcpi.block as block
import time

SLEEP_SECS = 1

class BuildingBlockTests():
	def __init__(self, mc, sleep):
		self.mc = mc
		self.sleep = sleep
		self.pos = None
	
	def _test_block_build(self, block):
		self.mc.postToChat("Building Block")
		block.build(self.mc)
		time.sleep(self.sleep)
		
	def _test_block_clear(self, block):
		self.mc.postToChat("Clearing Block")
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
		self.mc.postToChat("Single Block Test")
		self._run_block_test(bl)
		
	def test_single_block_rot90(self):
		bl = self._create_single_block()
		self.mc.postToChat("Single Block Test rotated 90")
		bl.rotateRight()
		self._run_block_test(bl)
		
	def test_single_block_rot180(self):
		bl = self._create_single_block()
		self.mc.postToChat("Single Block Test rotated 180")
		bl.rotateRight(2)
		self._run_block_test(bl)
		
	def test_single_block_rot270(self):
		bl = self._create_single_block()
		self.mc.postToChat("Single Block Test rotated 270")
		bl.rotateLeft()
		self._run_block_test(bl)
		
	def test_block_range(self):
		bl = self._create_block_range()
		self.mc.postToChat("Block Range Test")
		self._run_block_test(bl)
		
	def test_block_range_rot90(self):
		bl = self._create_block_range()
		self.mc.postToChat("Block Range Test rotated 90")
		bl.rotateRight()
		self._run_block_test(bl)
		
	def test_block_range_rot180(self):
		bl = self._create_block_range()
		self.mc.postToChat("Block Range Test rotated 180")
		bl.rotateRight(2)
		self._run_block_test(bl)
		
	def test_block_range_rot270(self):
		bl = self._create_block_range()
		self.mc.postToChat("Block Range Test rotated 270")
		bl.rotateLeft()
		self._run_block_test(bl)
		
	def run(self):
		self.pos = self.mc.player.getTilePos()

		self.test_single_block()
		self.test_single_block_rot90()
		self.test_single_block_rot180()
		self.test_single_block_rot270()
		
		self.test_block_range()
		self.test_block_range_rot90()
		self.test_block_range_rot180()
		self.test_block_range_rot270()


def run_block_tests():
	mc = minecraft.Minecraft.create()
	tester = BuildingBlockTests(mc, SLEEP_SECS)
	tester.run()

	
class BuildingLayerTests():
	def __init__(self, mc, sleep):
		self.mc = mc
		self.sleep = sleep
		self.pos = None

	def _test_layer_build(self, layer):
		self.mc.postToChat("Building Layer")
		layer.build(self.mc)
		time.sleep(self.sleep)
		
	def _test_layer_clear(self, layer):
		self.mc.postToChat("Clearing Layer")
		layer.clear(self.mc)
		time.sleep(self.sleep)
		
	def _run_layer_test(self, block):
		self._test_layer_build(block)
		self._test_layer_clear(block)
	
	def _create_singlepart_layer(self):
		# TODO: write code for single part layer
		bl = BuildingBlock(self.pos, Vec3(0, 0, 2), block.STONE)
		return bl
	
	def _create_multipart_layer(self):
		# TODO: write code to create multipart layer
		bl = BuildingBlock(self.pos, Vec3(-1, 0, 2), block.STONE, Vec3(1, 0, 2))
		return bl

	def test_singlepart_layer(self):
		ly = self._create_singlepart_layer()
		self.mc.postToChat("Single Layer Test")
		self._run_layer_test(ly)
		
	def test_singlepart_layer_rot90(self):
		ly = self._create_singlepart_layer()
		self.mc.postToChat("Single Layer Test rotated 90")
		ly.rotateRight()
		self._run_layer_test(ly)
		
	def test_singlepart_layer_rot180(self):
		ly = self._create_singlepart_layer()
		self.mc.postToChat("Single Layer Test rotated 180")
		ly.rotateRight(2)
		self._run_layer_test(ly)
		
	def test_singlepart_layer_rot270(self):
		ly = self._create_singlepart_layer()
		self.mc.postToChat("Single Layer Test rotated 270")
		ly.rotateLeft()
		self._run_layer_test(ly)
		
	def test_multipart_layer(self):
		ly = self._create_multipart_layer()
		self.mc.postToChat("Multipart Layer Test")
		self._run_layer_test(ly)
		
	def test_multipart_layer_rot90(self):
		ly = self._create_multipart_layer()
		self.mc.postToChat("Multipart Layer Test rotated 90")
		ly.rotateRight()
		self._run_layer_test(ly)
		
	def test_multipart_layer_rot180(self):
		ly = self._create_multipart_layer()
		self.mc.postToChat("Multipart Layer Test rotated 180")
		ly.rotateRight(2)
		self._run_layer_test(ly)
		
	def test_multipart_layer_rot270(self):
		ly = self._create_multipart_layer()
		self.mc.postToChat("Multipart Layer Test rotated 270")
		ly.rotateLeft()
		self._run_layer_test(ly)
		
	def run(self):
		self.pos = self.mc.player.getTilePos()
		
		self.test_singlepart_layer()
		self.test_singlepart_layer_rot90()
		self.test_singlepart_layer_rot180()
		self.test_singlepart_layer_rot270()
		
		self.test_multipart_layer()
		self.test_multipart_layer_rot90()
		self.test_multipart_layer_rot180()
		self.test_multipart_layer_rot270()
		
def run_layer_tests():
	mc = minecraft.Minecraft.create()
	tester = BuildingLayerTests(mc, SLEEP_SECS)
	tester.run()

	
class BuildingTests():
	def __init__(self, mc, sleep):
		self.mc = mc
		self.sleep = sleep
		self.pos = None

	def run(self):
		self.pos = self.mc.player.getTilePos()
		pass
		
def run_building_tests():
	mc = minecraft.Minecraft.create()
	tester = BuildingTests(mc, SLEEP_SECS)
	tester.run()

if __name__ == "__main__":
	run_block_tests()