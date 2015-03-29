from building import Building, BuildingLayer, BuildingBlock
from oriented_blocks import Torch
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

class LampPost(Building):
	BLACK_WOOL = 15
	
	LAMPPOST_WIDTH = 3
	def __init__(self, *args, **kwargs):
		super(LampPost, self).__init__(width=LampPost.LAMPPOST_WIDTH, *args, **kwargs)

		post = BuildingBlock(Vec3(-1,0,-1), block.FENCE, description="Post")
		self.layers.append(BuildingLayer([post], 0))
		self.layers.append(BuildingLayer([post], 1))
		self.layers.append(BuildingLayer([post], 2))

		torches = [(Vec3(-2,0,-1), block.TORCH.withData(Torch.WEST), "West torch"),
					(Vec3(-1,0,-2), block.TORCH.withData(Torch.NORTH), "North torch"),
					(Vec3(0,0,-1), block.TORCH.withData(Torch.EAST), "East torch"),
					(Vec3(-1,0,0), block.TORCH.withData(Torch.SOUTH), "South torch")]
		
		wool_block = block.WOOL.withData(LampPost.BLACK_WOOL)
		lamp_blocks = []
		lamp_blocks.append(BuildingBlock(Vec3(-1,0,-1), wool_block, description="Lamp block"))
		for pos, block_type, desc in torches:
			lamp_blocks.append(Torch(pos, block_type, description=desc))

		self.layers.append(BuildingLayer(lamp_blocks, 3))
		
		self._set_orientation()

	def build(self, mc):
		super(LampPost, self).build(mc)
	
