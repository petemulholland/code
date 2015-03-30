from building import Building, BuildingLayer, BuildingBlock
import mcpi.block as block
from mcpi.vec3 import Vec3

class Well(Building):
	
	WELL_OUTER_SPAN = (Building.SE_CORNER_POS, Building.SE_CORNER_POS + Vec3(-5,0,-5))
	WELL_CORE_POS = (WELL_OUTER_SPAN[0] + Vec3(-1,0,-1), 
					WELL_OUTER_SPAN[0] + Vec3(-4,0,-4), 
					WELL_OUTER_SPAN[0] + Vec3(-4,0,-1), 
					WELL_OUTER_SPAN[0] + Vec3(-1,0,-4))
	WELL_INNER_SPAN = (WELL_OUTER_SPAN[0] + Vec3(-2,0,-2), 
						WELL_OUTER_SPAN[0] + Vec3(-3,0,-3))

	WIDTH = 6
	def __init__(self, *args, **kwargs):
		super(Well, self).__init__(width=Well.WIDTH, *args, **kwargs)

		# level -3, base
		base = []
		base.append(BuildingBlock(Well.WELL_CORE_POS[0], 
									block.COBBLESTONE, Well.WELL_CORE_POS[1],
									description="Well base"))
		self.layers.append(BuildingLayer(base, -3))

		# level -2, water
		water = []
		water.extend(base)
		water.append(BuildingBlock(Well.WELL_INNER_SPAN[0], 
									block.WATER, Well.WELL_INNER_SPAN[1],
									description="Well water"))

		self.layers.append(BuildingLayer(water, -2))

		layer_blocks = []
		# level -1, ground
		layer_blocks.append(BuildingBlock(Well.WELL_OUTER_SPAN[0], 
										block.GRAVEL, Well.WELL_OUTER_SPAN[1],
										description="Well ground surround"))
		layer_blocks.extend(water)

		self.layers.append(BuildingLayer(layer_blocks, -1))
		del layer_blocks[:]

		# level 0, walls 
		layer_blocks.extend(base)
		layer_blocks.append(BuildingBlock(Well.WELL_INNER_SPAN[0], 
										block.AIR, Well.WELL_INNER_SPAN[1],
										description="Well clear inner"))

		self.layers.append(BuildingLayer(layer_blocks, 0))
		del layer_blocks[:]

		# levels 1 & 2, supports
		supports = []
		for pos in Well.WELL_CORE_POS:
			supports.append(BuildingBlock(pos, block.FENCE, description="Well support"))

		self.layers.append(BuildingLayer(supports, 1))
		self.layers.append(BuildingLayer(supports, 2))

		# level 3 roof
		self.layers.append(BuildingLayer(base, 3))
		
		self._set_orientation()

	