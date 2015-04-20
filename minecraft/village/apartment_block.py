from building import Building, BuildingLayer, BuildingBlock
from farm import LargeFarm
from street import Street
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
		layer_blocks.append(BuildingBlock(Apartment.WIN_POS, block.GLASS_PANE, description="Window"))

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

#wwwwwwwwwwwwwwwwwwwwwwwww 3
#wffwffwffwffwffwffwffwffw 2
#wffwffwffwffwffwffwffwffw 1
#wffwffwffwffwffwffwffwffw 03
#wffwffwffwffwffwffwffwffw 9
#wffwffwffwffwffwffwffwffw 8
#wffwffwffwffwffwffwffwffw 7
#wffwffwffwffwffwffwffwffw 6
#wwwwwwwwwwwwXwwwwwwwwwwwX 5 	=> 2 large farms (overlapping border) to north
#	   1     2     3     4 4 
#                          3
#                          2
#wwwwwwwwX  gwwswwwswwwXww 1	=> 3 large farms (no overlap) to west
#wfffffffw   www   w   www 02
#wfffffffw   wwd   w   gww 9
#wwwwwwwww  gwww   w   www 8
#wfffffffw   wwg   w   dww 7
#wfffffffw   www   w   www 6
#wwwwwwwww  gwwXwwwswwwXww 5
#wwwwwwwwX   www   w   www 4
#wfffffffw   wwd   w   gww 3
#wfffffffw  gwww   w   www 2
#wwwwwwwww   wwg   w   dww 1 
#wfffffffw   www   w   www 01
#wfffffffw  gwwXwwwswwwXww 9
#wwwwwwwww   www   w   www 8
#wwwwwwwwX   wwd   w   gww 7
#wfffffffw  gwww   w   www 6
#wfffffffw   wwg   w   dww 5
#wwwwwwwww   www   w   www 4
#wfffffffw  gwwXwwwswwwsww 3
#wfffffffw   wwwwwwwwwwwww 2
#wwwwwwwww   wwwwwwwwwwwww 1
#           gss  ssss   ss 0
#g  g  g  g  g  g  g  g  g  
#4321098765432109876543210
#    2         1

# => depth = 34
# => width = 26

class ApartmentBlock(Building):
	CORNER_POS = {'South East' : Building.SE_CORNER_POS + Vec3(0,0,-1), 
				  'South West' : Building.SE_CORNER_POS + Vec3(-12,0,-1),
				  'North West' : Building.SE_CORNER_POS + Vec3(-12,0,-21),
				  'North East' : Building.SE_CORNER_POS + Vec3(0,0,-21) }
	# 2 deep upper walkway with fences on outside. + stairs at front
	# add fence posts underneath at corners
	EAST_APTS_POS = [Vec3(-3,0,-10), Vec3(-9,0,-10), Vec3(-15,0,-10)] # TODO all 6 apt relative posns, for original SE corner of apt?
	WEST_APTS_POS = [Vec3(-10,0,-2), Vec3(-15,0,-2), Vec3(-21,0,-2)] # TODO all 6 apt relative posns, for original SE corner of apt?
	
	WEST_FARMS_POS = [Vec3(-7,0,-16), Vec3(-14,0,-16), Vec3(-21,0,-16)]
	NORTH_FARMS_POS = [Vec3(-25,0,0), Vec3(-25,0,-12)]
	WIDTH = 26 

	END_WINS_POS = [Vec3(-3,0,-4), Vec3(-3,0,-8), Vec3(-21,0,-4), Vec3(-21,0,-8)]

	def __init__(self, *args, **kwargs):
		super(ApartmentBlock, self).__init__(width=ApartmentBlock.WIDTH, *args, **kwargs)

		# Apartment & farm sub-building objects & placement positions for each
		self._apartments = [Apartment(Building.EAST), # west facing apt built to east
						   Apartment(Building.WEST)] # east facing built to west of player posn
		self._farms = [LargeFarm(Building.WEST, LargeFarm.WIDTH),
				 	   LargeFarm(Building.NORTH, LargeFarm.WIDTH)]
		self._east_apts_pos = list(ApartmentBlock.EAST_APTS_POS)
		self._west_apts_pos = list(ApartmentBlock.WEST_APTS_POS)
		self._west_farms_pos = list(ApartmentBlock.WEST_FARMS_POS)
		self._north_farms_pos = list(ApartmentBlock.NORTH_FARMS_POS)

		self._street = Street(Building.NORTH)
		self._streets_pos = []
		for i in range(0,9):
			self._streets_pos.append(Vec3(3,0,i*3))
			self._streets_pos.append(Vec3(-22,0,i*3))
			if i < 8:
				self._streets_pos.append(Vec3(i*3,0,-13))


		#######################################################################
		# level 0 blocks.
		layer_blocks = []
		# cobblestone walk way
		layer_blocks.append(self._add_walkway(0, block.COBBLESTONE)) + Vec3(0,0,1)
		# cobblestone steps at end of each walkway
		layer_blocks.append(Stair(ApartmentBlock.CORNER_POS['South East'], 
								block.STAIRS_COBBLESTONE.withData(Stair.NORTH),
								ApartmentBlock.CORNER_POS['South East'] + Vec3(-1,0,1),
								description="Ground floor steps"))
		layer_blocks.append(Stair(ApartmentBlock.CORNER_POS['South West'] + Vec3(1,0,1), 
								block.STAIRS_COBBLESTONE.withData(Stair.NORTH),
								ApartmentBlock.CORNER_POS['South West'] + Vec3(0,0,1),
								description="Ground floor steps"))
		# wooden steps to 2nd floor.
		layer_blocks.append(Stair(ApartmentBlock.CORNER_POS['South East'] + Vec3(-8,0,1), 
								block.STAIRS_WOOD.withData(Stair.EAST),
								description="Steps to upper floor"))
		layer_blocks.append(Stair(ApartmentBlock.CORNER_POS['South East'] + Vec3(-7,0,1), 
								block.WOOD_PLANKS,
								description="Steps to upper floor"))

		self.add_layer(BuildingLayer(layer_blocks, 0))
		del layer_blocks [:]

		#######################################################################
		# levels 1 - 3 blocks
		# fence posts at each corner
		for i in range(1,4):
			for pos in ApartmentBlock.CORNER_POS.values:
				layer_blocks.append(BuildingBlock(pos, block.FENCE, description="Corner post"))

			# wooden steps to 2nd floor.
			layer_blocks.append(Stair(ApartmentBlock.CORNER_POS['South East'] + Vec3(-8+i,0,1), 
									block.STAIRS_WOOD.withData(Stair.EAST),
									description="Steps to upper floor"))
			layer_blocks.append(Stair(ApartmentBlock.CORNER_POS['South East'] + Vec3(-7+i,0,1), 
									block.WOOD_PLANKS,
									description="Steps to upper floor"))

			self.add_layer(BuildingLayer(layer_blocks, i))
			del layer_blocks [:]

		#######################################################################
		# level 4 blocks
		# wooden steps to 2nd floor.
		layer_blocks.append(Stair(ApartmentBlock.CORNER_POS['South East'] + Vec3(-4,0,1), 
								block.STAIRS_WOOD.withData(Stair.EAST),
								description="Steps to upper floor"))
		layer_blocks.append(Stair(ApartmentBlock.CORNER_POS['South East'] + Vec3(-3,0,1), 
								block.WOOD_PLANKS,
								description="Steps to upper floor"))

		self.add_layer(BuildingLayer(layer_blocks, i))
		del layer_blocks [:]

		#######################################################################
		# level 5 blocks
		# TODO: add fence railings around upper balcony

		for pos in ApartmentBlock.END_WINS_POS:
			self._blocks.append(BuildingBlock(pos + Vec3(0,3,0), block.GLASS_PANE, description="End window"))
			self._blocks.append(BuildingBlock(pos + Vec3(0,7,0), block.GLASS_PANE, description="End window"))

		self._set_orientation()

	def _add_walkway(self, level, type):
		blocks = []
		blocks.append(BuildingBlock(ApartmentBlock.CORNER_POS['South East'] + Vec3(0,level,0), 
									type, ApartmentBlock.CORNER_POS['North East'] + Vec3(0,level,-1),
									description="East walkway"))
		blocks.append(BuildingBlock(ApartmentBlock.CORNER_POS['South West'] + Vec3(0,level,0), 
									type, ApartmentBlock.CORNER_POS['North West'] + Vec3(0,level,1),
									description="West walkway"))
		blocks.append(BuildingBlock(ApartmentBlock.CORNER_POS['South East'] + Vec3(0,level,0), 
									type, ApartmentBlock.CORNER_POS['South West'] + Vec3(-1,level,0),
									description="South walkway"))

	def _do_rotation(self, rot_func, *args):
		for building in self._apartments:
			building.rot_func(*args)
		for building in self._farms:
			building.rot_func(*args)

		for pos in self._east_apts_pos:
			pos.rot_func(*args)
		for pos in self._west_apts_pos:
			pos.rot_func(*args)
		for pos in self._west_farms_pos:
			pos.rot_func(*args)
		for pos in self._north_farms_pos:
			pos.rot_func(*args)

		for pos in self._end_wins_pos:
			pos.rot_func(*args)
		for pos in self._streets_pos:
			pos.rot_func(*args)

	def rotateLeft(self):
		super(ApartmentBlock, self).rotateLeft()
		#for building in self._apartments:
		#	building.rotateLeft()
		#for building in self._farms:
		#	building.rotateLeft()

		#for pos in self._east_apts_pos:
		#	pos.rotateLeft()
		#for pos in self._west_apts_pos:
		#	pos.rotateLeft()
		#for pos in self._west_farms_pos:
		#	pos.rotateLeft()
		#for pos in self._north_farms_pos:
		#	pos.rotateLeft()

		#for pos in self._end_wins_pos:
		#	pos.rotateLeft()
		self._do_rotation(rotateLeft)

	def rotateRight(self, ct=1):
		super(ApartmentBlock, self).rotateRight(ct)
		self._do_rotation(rotateRight, ct)

	def _build_at(self, mc, pos, debug):
		# Building has no build method? how's this working?
		# calling super will build the stuff added as layers
		# need to build the apts at specified points first so windows get placed properly 
		for _pos in self._east_apts_pos:
			self._apartments[0]._build_at(mc, pos + _pos, debug)
			self._apartments[0]._build_at(mc, pos + _pos + Vec3(0,4,0), debug)
		for _pos in self._west_apts_pos:
			self._apartments[1]._build_at(mc, pos + _pos, debug)
			self._apartments[1]._build_at(mc, pos + _pos + Vec3(0,4,0), debug)

		for _pos in self._west_farms_pos:
			self._farms[0]._build_at(mc, pos + _pos, debug)
		for _pos in self._north_farms_pos:
			self._farms[1]._build_at(mc, pos + _pos, debug)
		for _pos in self._streets_pos:
			self._street._build_at(mc, pos + _pos, debug)

		# (do I need to override the build_to_xxx methods?)
		super(ApartmentBlock, self)._build_at(mc, pos, debug)

