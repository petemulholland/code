from building import Building, BuildingLayer, BuildingBlock, CompositeBuilding, Torch
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3
import random

WHEAT = Block(59)
POTATOES = Block(142)
CARROTS =  Block(141)

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

		# all wheat on one side , with random choice of ripeness
		layer_blocks.append(BuildingBlock(Farm.CROPS_LEFT_SPAN[0], 
									Block(WHEAT.id, random.randint(3,7)), 
									Farm.CROPS_LEFT_SPAN[1],
									description="Wheat crops"))
		layer_blocks.append(BuildingBlock(Farm.CROPS_RIGHT_SPAN[0], 
									Block(POTATOES.id, random.randint(3,7)), 
									Farm.CROPS_RIGHT_SPAN[1] + Vec3(1,0,0),
									description="Potatoes"))
		layer_blocks.append(BuildingBlock(Farm.CROPS_RIGHT_SPAN[0] + Vec3(-1,0,0,), 
									Block(CARROTS.id, random.randint(3,7)), 
									Farm.CROPS_RIGHT_SPAN[1],
									description="Carrots"))

		self.add_layer(BuildingLayer(layer_blocks, 1))
		self._set_orientation()


	
class LargeFarm(CompositeBuilding):
	WIDTH = 13
	def __init__(self, *args, **kwargs):
		super(LargeFarm, self).__init__(width=LargeFarm.WIDTH, *args, **kwargs)

		self.add_subbuilding(Farm(Building.NORTH), Building.SE_CORNER_POS)
		self.add_subbuilding(Farm(Building.NORTH), Building.SE_CORNER_POS + Vec3(-6,0,0))
		
		self._set_orientation()


