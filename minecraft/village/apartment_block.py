from building import Building, BuildingLayer, BuildingBlock
from farm import LargeFarm
from oriented_blocks import Stair, Torch, Door
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

# TODO: Actually maybe this can be done composed of other buildings
#		 - need to override the rotate functions
#		 - add positions for each sub building and rotate psns in the rotate methods
#		 - add layers for walkways, stairs, & end windows
#		need to layout apartment block as whole building
#		add surrounding farms in construction, 1 for each orientation, can be rotatedin override
#       6 apartments per floor with window beside front door, end apts can have side windows too.
#		add stone walkway (1x block wide) on ground floor
#		add wooden plank walkway around top with stairs down at front
class Apartment(Building):
	
	WALLS_CORNER_POS = {'South East' : Building.SE_CORNER_POS,
						'South West' : Building.SE_CORNER_POS + Vec3(-6,0,0),
						'North West' : Building.SE_CORNER_POS + Vec3(-6,0,-4),
						'North East' : Building.SE_CORNER_POS + Vec3(0,0,-4)}

	WALL_SPANS = [(WALLS_CORNER_POS['South West'] + Vec3(0,0,-1), 
						WALLS_CORNER_POS['North West'] + Vec3(0,0,1), "West Wall"),
					(WALLS_CORNER_POS['North West'] + Vec3(1,0,0), 
						WALLS_CORNER_POS['North East'] + Vec3(-1,0,0), "North Wall"),
					(WALLS_CORNER_POS['North East'] + Vec3(0,0,1), 
						WALLS_CORNER_POS['South East'] + Vec3(0,0,-1), "East Wall"),
					(WALLS_CORNER_POS['South East'] + Vec3(-1,0,0), 
						WALLS_CORNER_POS['South West'] + Vec3(1,0,0), "South Wall")]

	DOOR_POS = WALLS_CORNER_POS['South East'] + Vec3(-2,0,0)
	TORCH_POS = DOOR_POS + Vec3(0,0,-1)

	WIN_POS = WALLS_CORNER_POS['South East'] + Vec3(-4,0,0)

	WIDTH = 7
	def __init__(self, *args, **kwargs):
		super(Apartment, self).__init__(width=Apartment.WIDTH, *args, **kwargs)

		#######################################################################
		# Level 1:
		layer_blocks = []
		layer_blocks.append(BuildingBlock(Apartment.WALLS_CORNER_POS['South West'], 
							  block.COBBLESTONE, Apartment.WALLS_CORNER_POS['North East'],
							  description="House base"))
		self.add_layer(BuildingLayer(layer_blocks, 0))
		del layer_blocks [:]

		#######################################################################
		# Common blocks:
		walls = []
		
		# cobblestone corners
		for key, pos in Apartment.WALLS_CORNER_POS.items():
			walls.append(BuildingBlock(pos, block.COBBLESTONE, description="Corner stone"))
		
		# wood plank walls 
		for pos1, pos2, desc in Apartment.WALL_SPANS:
			walls.append(BuildingBlock(pos1, block.WOOD_PLANKS, pos2, desc))

		#######################################################################
		# Level 2:
		# add walls as above & clear door	
		layer_blocks.extend(walls)
		
		layer_blocks.append(BuildingBlock(Apartment.DOOR_POS, block.AIR, description="Clear door"))
		self.add_layer(BuildingLayer(layer_blocks, 1))
		del layer_blocks [:]

		#######################################################################
		# Level 3:
		# add walls, clear door	& add windows
		layer_blocks.extend(walls)
			
		layer_blocks.append(BuildingBlock(Apartment.DOOR_POS, block.AIR, description="Clear door"))

		for pos in Apartment.WIN_POS:
			layer_blocks.append(BuildingBlock(pos, block.GLASS_PANE, description="Window"))

		self.add_layer(BuildingLayer(layer_blocks, 2))
		del layer_blocks [:]

		#######################################################################
		# Level 4:
		# add walls & torch over door	
		layer_blocks.extend(walls)
			
		layer_blocks.append(Torch(Apartment.TORCH_POS, block.TORCH.withData(Torch.NORTH), 
									description="Torch over door"))
		self.add_layer(BuildingLayer(layer_blocks, 3))
		del layer_blocks [:]

		#######################################################################
		# build the roof
		layer_blocks.append(BuildingBlock(Apartment.WALLS_CORNER_POS['South East'], 
							block.WOOD, Apartment.WALLS_CORNER_POS['North West'],
							description="Roof wood span"))
		layer_blocks.append(BuildingBlock(Apartment.WALLS_CORNER_POS['South East'] + Vec3(-1,0,-1), 
							block.WOOD_PLANKS, Apartment.WALLS_CORNER_POS['North West'] + Vec3(1,0,1),
							description="Roof wood plank span"))

		layer_blocks.append(BuildingBlock(Apartment.LADDER_POS, block.AIR, description="Clear ladder space"))
		
		layer_blocks.append(ladder)

		self.add_layer(BuildingLayer(layer_blocks, 4))
		del layer_blocks [:]

		#######################################################################
		# add the fences to the roof
		layer_blocks.append(BuildingBlock(Apartment.WALLS_CORNER_POS['South East'], 
							block.FENCE, Apartment.WALLS_CORNER_POS['North West'],
							description="Cover roof with fences"))
		layer_blocks.append(BuildingBlock(Apartment.WALLS_CORNER_POS['South East'] + Vec3(-1,0,-1), 
							block.AIR, Apartment.WALLS_CORNER_POS['North West'] + Vec3(1,0,1),
							description="Clear fences from inner roof"))

		self.add_layer(BuildingLayer(layer_blocks, 5))
		del layer_blocks [:]

		#######################################################################
		# add the door
		self.add_block(Door(Door.HINGE_RIGHT, 
							Vec3(Apartment.DOOR_POS.x, 1, Apartment.DOOR_POS.z), 
							block.DOOR_WOOD.withData(Door.SOUTH)))

		self._set_orientation()

		
	def build(self, mc):
		super(Apartment, self).build(mc)

#wwwwwwwwwwwwwwwwwwwwwwwww
#wffwffwffwffwffwffwffwffw
#wffwffwffwffwffwffwffwffw
#wffwffwffwffwffwffwffwffw
#wffwffwffwffwffwffwffwffw
#wffwffwffwffwffwffwffwffw
#wffwffwffwffwffwffwffwffw
#wffwffwffwffwffwffwffwffw
#wwwwwwwwwwwwwwwwwwwwwwwww	=> 2 large farms (overlapping border) to north
#	   1     2     3     4
#
#
#wwwwwwwww   wwswwwswwwsww	=> 3 large farms (no overlap) to west
#wfffffffw   www   w   www
#wfffffffw   wwd   w   gww
#wwwwwwwww   www   w   www
#wfffffffw   wwg   w   dww
#wfffffffw   www   w   www
#wwwwwwwww   wwswwwswwwsww
#wwwwwwwww   www   w   www
#wfffffffw   wwd   w   gww
#wfffffffw   www   w   www
#wwwwwwwww   wwg   w   dww
#wfffffffw   www   w   www
#wfffffffw   wwswwwswwwsww
#wwwwwwwww   www   w   www
#wwwwwwwww   wwd   w   gww
#wfffffffw   www   w   www
#wfffffffw   wwg   w   dww
#wwwwwwwww   www   w   www
#wfffffffw   wwswwwswwwsww
#wfffffffw   wwwwwwwwwwwww
#wwwwwwwww   wwwwwwwwwwwww
#            s   ssss    s

# => depth = 34
# => width = 26

class ApartmentBlock(Building):
	CORNER_POS = {'South East' : Building.SE_CORNER_POS + Vec3(0,0,0), 
				  'South West' : Building.SE_CORNER_POS + Vec3(-13,0,0),
				  'North West' : Building.SE_CORNER_POS + Vec3(-13,0,-22),
				  'North East' : Building.SE_CORNER_POS + Vec3(0,0,-22) }
	# 2 deep upper walkway with fences on outside. + stairs at front
	# add fence posts underneath at corners
	APT_POSNS = [Vec3(-1,0-1)] # TODO all 6 apt relative posns, for original SE corner of apt?
	WIDTH = 13 # TODO add full span of block + farms to the width 

	END_WIN_POS = []
	FARM_POS = [] #  figure out large farms & regular farm layout

	
	def __init__(self, *args, **kwargs):
		super(ApartmentBlock, self).__init__(width=ApartmentBlock.WIDTH, *args, **kwargs)


		# TODO, need to adjust orientation of each of sub buildings based on current orientation
		self.apartments = [Apartment(Building.EAST, Apartment.WIDTH), # west facing apt built to east
						   Apartment(Building.WEST, Apartment.WIDTH)] # east facing built to west of player posn
		self.farms = [LargeFarm(Building.WEST, LargeFarm.WIDTH),
					  LargeFarm(Building.NORTH, LargeFarm.WIDTH)]
		self._set_orientation()
	
	def build(self, mc):
		# Building has no build method? how's this working?
		# calling super will build the stuff added as layers
		# need to build the apts at specified points first so windows get placed properly 

		# (do I need to override the build_to_xxx methods?)
		super(ApartmentBlock, self).build(mc)

