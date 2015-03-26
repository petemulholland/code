from mcpi.vec3 import Vec3
import mcpi.block as block
from village.building import Building, BuildingLayer, BuildingBlock
from village.tests.tester_base import TesterBase
import time

		
class BuildingBlockTester(TesterBase):
	def __init__(self, *args, **kwargs):
		super(BuildingBlockTester, self).__init__(sut_name = "Block", *args, **kwargs)
		self.default_offset = Vec3(0,0-2)

	def _rotate_sut(self, sut, orientation):
		if orientation == Building.EAST:
			sut.rotateRight()
		elif orientation == Building.SOUTH:
			sut.rotateRight(2)
		elif orientation == Building.WEST:
			sut.rotateLeft()
		
		return sut

	def _create_single_block(self, orientation):
		sut = BuildingBlock(self.pos, Vec3(0, 0, -2), block.STONE)
		sut = self._rotate_sut(sut, orientation)
		return sut
	
	def _create_block_range(self, orientation):
		sut = BuildingBlock(self.pos, Vec3(-1, 0, -2), block.STONE, Vec3(1, 0, -2))
		sut = self._rotate_sut(sut, orientation)
		return sut

	def run(self, *args, **kwargs):
		super(BuildingBlockTester, self).run(self._create_single_block, *args, **kwargs)

		self.sut_name = "Block Range"
		super(BuildingBlockTester, self).run(self._create_block_range, *args, **kwargs)


class BuildingLayerTester(TesterBase):
	def __init__(self, *args, **kwargs):
		super(BuildingLayerTester, self).__init__(sut_name = "Single part Building Layer", *args, **kwargs)
		self.default_offset = Vec3(0,0-3)

	def _rotate_sut(self, sut, orientation):
		if orientation == Building.EAST:
			sut.rotateRight()
		elif orientation == Building.SOUTH:
			sut.rotateRight(2)
		elif orientation == Building.WEST:
			sut.rotateLeft()
		
		return sut

	def _create_singlepart_layer(self, orientation):
		WELL_CORE = (Vec3(-1,0,-2), Vec3(2,0,-5))
		WELL_BASE = []
		WELL_BASE.append(BuildingBlock(self.pos, WELL_CORE[0], block.STONE, WELL_CORE[1]))
		sut = BuildingLayer(WELL_BASE, 0)
		sut = self._rotate_sut(sut, orientation)
		return sut
	
	def _create_multipart_layer(self, orientation):
		WELL_OUTER = (Vec3(-2,0,-1), Vec3(3,0,-6))
		WELL_CORE = (Vec3(-1,0,-2), Vec3(2,0,-5))
		WELL_INNER = (Vec3(0,0,-3), Vec3(1,0,-4))

		WELL_GROUND = []
		WELL_GROUND.append(BuildingBlock(self.pos, WELL_OUTER[0], block.GRAVEL, WELL_OUTER[1]))
		WELL_GROUND.append(BuildingBlock(self.pos, WELL_CORE[0], block.STONE, WELL_CORE[1]))
		WELL_GROUND.append(BuildingBlock(self.pos, WELL_INNER[0], block.WATER, WELL_INNER[1]))

		sut = BuildingLayer(WELL_GROUND, 0)
		sut = self._rotate_sut(sut, orientation)
		return sut

	def run(self, *args, **kwargs):
		super(BuildingLayerTester, self).run(self._create_singlepart_layer, *args, **kwargs)

		self.sut_name = "Multi-part Building Layer"
		super(BuildingLayerTester, self).run(self._create_multipart_layer, *args, **kwargs)
		

class BuildingTester(TesterBase):
	def __init__(self, *args, **kwargs):
		super(BuildingTester, self).__init__(sut_name = "Building", *args, **kwargs)
		self.default_offset = Vec3(0,0-5)

	def _create_building(self, orientation):
		WELL_OUTER = (Vec3(-2,0,0), Vec3(3,0,-5))
		WELL_CORE = (Vec3(-1,0,-1), Vec3(2,0,-4))
		WELL_INNER = (Vec3(0,0,-2), Vec3(1,0,-3))

		WELL_BASE = []
		WELL_BASE.append(BuildingBlock(self.pos, WELL_CORE[0], block.COBBLESTONE, WELL_CORE[1]))

		WELL_WATER = []
		WELL_WATER.append(BuildingBlock(self.pos, WELL_CORE[0], block.COBBLESTONE, WELL_CORE[1]))
		WELL_WATER.append(BuildingBlock(self.pos, WELL_INNER[0], block.WATER, WELL_INNER[1]))

		WELL_GROUND = []
		WELL_GROUND.append(BuildingBlock(self.pos, WELL_OUTER[0], block.GRAVEL, WELL_OUTER[1]))
		WELL_GROUND.append(BuildingBlock(self.pos, WELL_CORE[0], block.COBBLESTONE, WELL_CORE[1]))
		WELL_GROUND.append(BuildingBlock(self.pos, WELL_INNER[0], block.WATER, WELL_INNER[1]))

		WELL_WALLS = []
		WELL_WALLS.append(BuildingBlock(self.pos, WELL_CORE[0], block.COBBLESTONE, WELL_CORE[1]))
		WELL_WALLS.append(BuildingBlock(self.pos, WELL_INNER[0], block.AIR, WELL_INNER[1]))

		WELL_SUPPORT = []
		WELL_SUPPORT.append(BuildingBlock(self.pos, Vec3(-1,0,-1), block.FENCE))
		WELL_SUPPORT.append(BuildingBlock(self.pos, Vec3(-1,0,-4), block.FENCE))
		WELL_SUPPORT.append(BuildingBlock(self.pos, Vec3(2,0,-4), block.FENCE))
		WELL_SUPPORT.append(BuildingBlock(self.pos, Vec3(2,0,-1), block.FENCE))
		
		bl = Building(self.pos, orientation, self.default_offset)
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
	
	def run(self, *args, **kwargs):
		super(BuildingTester, self).run(self._create_building, *args, **kwargs)
		

if __name__ == "__main__":
	BuildingBlockTester.run_tests(mc)
	BuildingLayerTester.run_tests(mc)
	BuildingTester.run_tests(mc)
	