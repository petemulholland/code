from building import Building, BuildingLayer, BuildingBlock
from oriented_blocks import Torch
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3



class LampPost(Building):
	BLACK_WOOL = 15
	
	def __init__(self, *args, **kwargs):
		super(LampPost, self).__init__(*args, **kwargs)

		offset = self.build_pos
		post = BuildingBlock(offset, Vec3(0,0,0), block.FENCE)
		self.layers.append(BuildingLayer([post], 0))
		self.layers.append(BuildingLayer([post], 1))
		self.layers.append(BuildingLayer([post], 2))

		west1 = (Vec3(-1,0,0), block.TORCH.withData(Torch.WEST))
		north1 = (Vec3(0,0,1), block.TORCH.withData(Torch.NORTH))
		east1 = (Vec3(1,0,0), block.TORCH.withData(Torch.EAST))
		south1 = (Vec3(0,0,-1), block.TORCH.withData(Torch.SOUTH))
		
		wool_block = block.WOOL.withData(LampPost.BLACK_WOOL)
		lamp_blocks = []
		lamp_blocks.append(BuildingBlock(offset, Vec3(0,0,0), wool_block))
		lamp_blocks.append(Torch(offset, west1[0], west1[1]))
		lamp_blocks.append(Torch(offset, east1[0], east1[1]))
		lamp_blocks.append(Torch(offset, south1[0], south1[1])) 
		lamp_blocks.append(Torch(offset, north1[0], north1[1])) 
		self.layers.append(BuildingLayer(lamp_blocks, 3))
		
		self._set_orientation()

	def build(self, mc):
		super(LampPost, self).build(mc)
	
