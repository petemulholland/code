from building import Building, BuildingEx, BuildingBlock, Torch
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3


WHEAT = Block(59)
POTATOES = Block(142)
CARROTS =  Block(391)

class CropFarm(Building):
	# TODO: implement my current deisgn 7x8 with dispensers on bottom at back of 8 long side
	#		surrounded on 3 sides & top by glass
	#       run redstone around 
	pass

class DoubleCropFarm(BuildingEx):
	WIDTH = 19
	# TODO add 2 farms 1 east, 1 west (use case for mirroring so redstone all comes to same side.
	#      add central collection channel
	#      fill gap & add water channel.
	#	   add redtone mech for button to operate dispensers
	#      add hoppers & chest for collection
	#	   add door & trapdoor over collection channel
	# take 2 init params for crops left & crops right
	pass

