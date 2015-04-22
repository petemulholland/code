from village.building import Building, BuildingLayer, BuildingBlock, CompositeBuilding
from village.oriented_blocks import Torch
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

# http://minecraft.gamepedia.com/Data_values#Block_IDs
from base.types import PlankData

FLOORING = block.WOOD_PLANKS.withData(PlankData.DARK_OAK)
PANELING = block.WOOD_PLANKS.withData(PlankData.ACACIA)

class DiningHall(Building):
	# TODO: implement table & chairs, fireplaces & paintings on walls
     #- dining hall 
     #     - table 7x3
     #     - +1 around for chairs
     #     - +2 all around to leave space for ornaments
     #     - carpet on table at chair positions for place settings
     #     - => 13 x 9
     #     - maybe 15 to 17  long for fireplaces at  both ends  - 20 long?
	WALLS_CORNER_POS = {'South East' : Building.SE_CORNER_POS, 
						'South West' : Building.SE_CORNER_POS + Vec3(-16,0,0),
						'North West' : Building.SE_CORNER_POS + Vec3(-16,0,-10),
						'North East' : Building.SE_CORNER_POS + Vec3(0,0,-10) }
	
	WIDTH = WALLS_CORNER_POS['South East'].x - WALLS_CORNER_POS['South West'].x
	
	# TODO: want to update/extend Building class to use ordered list of collections idea
	# add blocks/block spans to a collection 
	def __init__(self, *args, **kwargs):
		super(DiningHall, self).__init__(width=DiningHall.WIDTH, *args, **kwargs)

