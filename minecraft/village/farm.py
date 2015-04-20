from building import Building, BuildingLayer, BuildingBlock
from oriented_blocks import Torch
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

WHEAT = Block(59)
POTATOES = Block(142)
CARROTS =  Block(391)

class Farm(Building):
	BOUNDARY_SPAN = (Building.SE_CORNER_POS, Building.SE_CORNER_POS + Vec3(-6,0,-8))
	LAND_SPAN = (BOUNDARY_SPAN[0] + Vec3(-1,0,-1), 
					BOUNDARY_SPAN[1] + Vec3(1,0,1))
	WATER_SPAN = (BOUNDARY_SPAN[0] + Vec3(-3,0,-1), 
					BOUNDARY_SPAN[0] + Vec3(-3,0,-7))
	
	CROPS_LEFT_SPAN = (BOUNDARY_SPAN[0] + Vec3(-4,0,-1), 
						BOUNDARY_SPAN[0] + Vec3(-5,0,-7))
	CROPS_RIGHT_SPAN = (BOUNDARY_SPAN[0] + Vec3(-1,0,-1), 
						BOUNDARY_SPAN[0] + Vec3(-2,0,-7))

	WIDTH = 7
	def __init__(self, *args, **kwargs):
		super(Farm, self).__init__(width=Farm.WIDTH, *args, **kwargs)

		layer_blocks = []
		layer_blocks.append(BuildingBlock(Farm.BOUNDARY_SPAN[0], 
									block.WOOD, Farm.BOUNDARY_SPAN[1],
									description="Farm boundary"))
		layer_blocks.append(BuildingBlock(Farm.LAND_SPAN[0], 
									block.FARMLAND, Farm.LAND_SPAN[1],
									description="Farm land"))
		layer_blocks.append(BuildingBlock(Farm.WATER_SPAN[0], 
									block.WATER, Farm.WATER_SPAN[1],
									description="Farm irrigation"))

		self.add_layer(BuildingLayer(layer_blocks, 0))
		del layer_blocks[:]

		for i in range(7):
			layer_blocks.append(BuildingBlock(Farm.CROPS_LEFT_SPAN[0] + Vec3(0,0,-i), 
										Block(WHEAT.id, i), description="Wheat crops"))
			layer_blocks.append(BuildingBlock(Farm.CROPS_LEFT_SPAN[0] + Vec3(-1,0,-i), 
										Block(POTATOES.id, i), description="Potatoes"))
			layer_blocks.append(BuildingBlock(Farm.CROPS_RIGHT_SPAN[0] + Vec3(-1,0,-i), 
										Block(WHEAT.id, i), description="Wheat crops"))
			layer_blocks.append(BuildingBlock(Farm.CROPS_RIGHT_SPAN[0] + Vec3(0,0,-i), 
										Block(CARROTS.id, i), description="Carrots"))

		self.add_layer(BuildingLayer(layer_blocks, 1))
		self._set_orientation()


	def build(self, mc):
		super(Farm, self).build(mc)
	
class LargeFarm(Farm):
	BOUNDARY_SPAN_L = (Building.SE_CORNER_POS + Vec3(-6,0,0), Building.SE_CORNER_POS + Vec3(-12,0,-8))
	LAND_SPAN_L = (BOUNDARY_SPAN[0] + Vec3(-1,0,-1), 
					BOUNDARY_SPAN[1] + Vec3(1,0,1))
	WATER_SPAN_L = (BOUNDARY_SPAN[0] + Vec3(-3,0,-1), 
					BOUNDARY_SPAN[0] + Vec3(-3,0,-7))
	
	CROPS_LEFT_SPAN_L = (BOUNDARY_SPAN[0] + Vec3(-4,0,-1), 
						BOUNDARY_SPAN[0] + Vec3(-5,0,-7))
	CROPS_RIGHT_SPAN_L = (BOUNDARY_SPAN[0] + Vec3(-1,0,-1), 
						BOUNDARY_SPAN[0] + Vec3(-2,0,-7))

	WIDTH = 13
	def __init__(self, *args, **kwargs):
		super(LargeFarm, self).__init__(width=LargeFarm.WIDTH, *args, **kwargs)

		layer_blocks = []
		layer_blocks.append(BuildingBlock(LargeFarm.BOUNDARY_SPAN_L[0], 
									block.WOOD, LargeFarm.BOUNDARY_SPAN_L[1],
									description="Farm boundary"))
		layer_blocks.append(BuildingBlock(LargeFarm.LAND_SPAN[0], 
									block.FARMLAND, LargeFarm.LAND_SPAN_L[1],
									description="Farm land"))
		layer_blocks.append(BuildingBlock(LargeFarm.WATER_SPAN_L[0], 
									block.WATER, LargeFarm.WATER_SPAN_L[1],
									description="Farm irrigation"))

		self.add_layer(BuildingLayer(layer_blocks, 0))
		del layer_blocks[:]

		for i in range(7):
			layer_blocks.append(BuildingBlock(LargeFarm.CROPS_LEFT_SPAN_L[0] + Vec3(0,0,-i), 
										Block(WHEAT.id, i), description="Wheat crops"))
			layer_blocks.append(BuildingBlock(LargeFarm.CROPS_LEFT_SPAN_L[0] + Vec3(-1,0,-i), 
										Block(POTATOES.id, i), description="Potatoes"))
			layer_blocks.append(BuildingBlock(LargeFarm.CROPS_RIGHT_SPAN_L[0] + Vec3(-1,0,-i), 
										Block(WHEAT.id, i), description="Wheat crops"))
			layer_blocks.append(BuildingBlock(LargeFarm.CROPS_RIGHT_SPAN_L[0] + Vec3(0,0,-i), 
										Block(CARROTS.id, i), description="Carrots"))

		self.add_layer(BuildingLayer(layer_blocks, 1))
		self._set_orientation()


	def build(self, mc):
		super(LargeFarm, self).build(mc)
