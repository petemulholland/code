from building import Building, BuildingBlock
import mcpi.block as block

WELL_OUTER = [Vec3(0,0,1), Vec3(-1,0,1), Vec3(-2,0,1), Vec3(-2,0,2), Vec3(-2,0,3), Vec3(-2,0,4), Vec3(-2,0,5), Vec3(-2,0,6),
			   Vec3(-1,0,6), Vec3(0,0,6), Vec3(1,0,6), Vec3(2,0,6), Vec3(3,0,6), Vec3(3,0,5), Vec3(3,0,4), Vec3(3,0,3),
			   Vec3(3,0,2), Vec3(3,0,1), Vec3(3,0,1), Vec3(2,0,1), Vec3(1,0,1)]
WELL_WALL = [Vec3(0,0,2), Vec3(-1,0,2), Vec3(-1,0,3), Vec3(-1,0,4), Vec3(-1,0,5), Vec3(0,0,5), Vec3(1,0,5), Vec3(2,0,5),
			 Vec3(2,0,4), Vec3(2,0,3), Vec3(2,0,2), Vec3(1,0,2)]
WELL_INNER = [Vec3(0,0,3), Vec3(0,0,4), Vec3(1,0,4), Vec3(1,0,3)]

WELL_BASE = []
WELL_WATER = []
WELL_GROUND = []
for vec in WELL_OUTER:
	WELL_GROUND.append(BuildingBlock(vec, block.GRAVEL))
	
for vec in WELL_WALL:
	WELL_BASE.append(BuildingBlock(vec, block.STONE))
	WELL_WATER.append(BuildingBlock(vec, block.STONE))
	WELL_GROUND.append(BuildingBlock(vec, block.STONE))

for vec in WELL_INNER:
	WELL_BASE.append(BuildingBlock(vec, block.STONE))
	WELL_WATER.append(BuildingBlock(vec, block.WATER))
	WELL_GROUND.append(BuildingBlock(vec, block.WATER))
	
class Well(Building):
	def __init__(self):#, **kwargs):
		#super().__init__(**kwargs)
		self.layers.append(BuildingLayer(WELL_BASE, -10))
		for i = -10; i < 0; ++i:
			self.layers.append(BuildingLayer(WELL_WATER, i))
		self.layers.append(BuildingLayer(WELL_GROUND, 0))
		layer = []
		for vec in WELL_WALL:
			layer.append(BuildingBlock(vec, block.STONE))
		self.layers.append(BuildingLayer(layer, 1))

		layer = []
		layer.append(BuildingBlock(Vec3(-1,0,2), block.FENCE))
		layer.append(BuildingBlock(Vec3(-1,0,5), block.FENCE))
		layer.append(BuildingBlock(Vec3(2,0,5), block.FENCE))
		layer.append(BuildingBlock(Vec3(2,0,2), block.FENCE))
		self.layers.append(BuildingLayer(layer, 2))
		self.layers.append(BuildingLayer(WELL_BASE, 3))

	def build(self):
		