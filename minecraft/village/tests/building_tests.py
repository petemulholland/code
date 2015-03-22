from village.building import Building, BuildingLayer, BuildingBlock
from mcpi import minecraft
from mcpi.vec3 import Vec3
import mcpi.block as block
import time

class BuildingBlockTests():
	def __init__(self, mc, pos, sleep):
		self.mc = mc
		self.pos = pos
		self.sleep = sleep
	
	def _test_block_build(self, block):
		self.mc.postToChat("Building Block")
		block.build()
		time.sleep(self.sleep)
		
	def _test_block_clear(self, block):
		self.mc.postToChat("Clearing Block")
		block.clear()
		time.sleep(self.sleep)
		
	def _run_block_test(self, block):
		self._test_block_build(block)
		self._test_block_clear(block)
	
	def _create_single_block(self):
		bl = Block(self.pos, Vec3(0, 0, 1), block.STONE)
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
		
	def _create_block_range(self):
		bl = Block(self.pos, Vec3(-1, 0, 2), block.STONE, Vec3(1, 0, 2))
		return bl

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
		
	def run():
		self.test_single_block()
		self.test_single_block_rot90()
		self.test_single_block_rot180()
		self.test_single_block_rot270()
		
		self.test_block_range()
		self.test_block_range_rot90()
		self.test_block_range_rot180()
		self.test_block_range_rot270()
		
		
		pass
		
class BuildingLayerTests():
	def run(mc, pos):
		pass
		
class BuildingTests():
	def run(mc, pos):
		pass
		
		
if __name__ == "__main__":
	mc = minecraft.Minecraft.create()

	pl = minecraft.player
	plpos = pl.getTilePos()
	
	tester = BuildingBlockTests(mc, plpos, 5)
	tester.run()
	