from building import Building, BuildingEx, BuildingBlock, Torch
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3


SUGAR_CANE = Block(83, 15) # 15 => first level is fully mature

class SugarCaneFarm(Building):
	# TODO: implement single cane farm with pistons & surrounding redstone
	pass

class DoubleCaneFarm(BuildingEx):
	# TODO double up the cane farm with redstoen path overlapping and 1 button to activate pistons.
	pass
