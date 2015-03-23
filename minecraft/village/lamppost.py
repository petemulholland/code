from building import Building, BuildingLayer, BuildingBlock
import mcpi.block as block
from mcpi.vec3 import Vec3

class LampPost(Building):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		offset = Vec3(0,0,1)
		post = BuildingBlock(offset, Vec3(0,0,0), block.FENCE)
		self.layers.append(BuildingLayer(post, 0)
		self.layers.append(BuildingLayer(post, 1)
		self.layers.append(BuildingLayer(post, 2)

		lamp_blocks = []
		lamp_blocks.append(BuildingBlock(offset, Vec3(0,0,0), block.WOOL) # TODO: black wool? 
		lamp_blocks.append(BuildingBlock(offset, Vec3(-1,0,0), block.TORCH)
		lamp_blocks.append(BuildingBlock(offset, Vec3(1,0,0), block.TORCH)
		lamp_blocks.append(BuildingBlock(offset, Vec3(0,0,-1), block.TORCH)
		lamp_blocks.append(BuildingBlock(offset, Vec3(0,0,1), block.TORCH)
		self.layers.append(BuildingLayer(lamp_blocks, 3)
		
		self._set_direction()

	def build(self, mc):
		super().build(mc)
	
