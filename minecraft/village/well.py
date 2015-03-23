from building import Building, BuildingBlock
import mcpi.block as block
from mcpi.vec3 import Vec3

#WELL_OUTER = [(Vec3(-2,0,1), Vec3(-2,0,6)), (Vec3(-1,0,6), Vec3(3,0,6)), (Vec3(3,0,5), Vec3(3,0,1)), (Vec3(2,0,1), Vec3(-1,0,1))]
#WELL_WALL = [(Vec3(-1,0,2), Vec3(-1,0,5)), (Vec3(0,0,5), Vec3(2,0,5)), (Vec3(2,0,4), Vec3(2,0,2)), (Vec3(1,0,2), Vec3(0,0,2))]
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

	
class Well(Building):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		# looks like super flat worlds on pi =>  just 3 deep wells
		self.layers.append(BuildingLayer(WELL_BASE, -3))
		self.layers.append(BuildingLayer(WELL_WATER, -2))
		self.layers.append(BuildingLayer(WELL_GROUND, -1))
		self.layers.append(BuildingLayer(WELL_WALLS, 0))
		self.layers.append(BuildingLayer(WELL_SUPPORT, 1))
		self.layers.append(BuildingLayer(WELL_SUPPORT, 2))
		self.layers.append(BuildingLayer(WELL_BASE, 3))
		
		self._set_direction()

	def build(self, mc):
		super().build(mc)
	