from building import Building, BuildingLayer, BuildingBlock, CompositeBuilding
from farm import Farm, LargeFarm
from street import Street
from oriented_blocks import Stair, Torch, Door
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

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
		# add the door
		self.add_block(Door(Door.HINGE_RIGHT, 
							Vec3(Apartment.DOOR_POS.x, 1, Apartment.DOOR_POS.z), 
							block.DOOR_WOOD.withData(Door.SOUTH),
							description="Front door"))

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
#4321098765432109876543210 4 
#                          3
#                          2
#wwwwwwwwX  gwwswwwswwwXww 1	=> 3 regular farms (no overlap) to west
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
# 2 deep upper walkway with fences on outside. + stairs at front
# add fence posts underneath at corners
# => depth = 34
# => width = 26

# add surrounding farms in construction, 1 for each orientation, can be rotatedin override
# 6 apartments per floor with window beside front door, end apts can have side windows too.
# add stone walkway (2x block wide) on ground floor
# add wooden plank walkway around top with stairs down at front

class ApartmentBlock(CompositeBuilding):
	CORNER_POS = {'South East' : Building.SE_CORNER_POS + Vec3(0,0,-1), 
				  'South West' : Building.SE_CORNER_POS + Vec3(-12,0,-1),
				  'North West' : Building.SE_CORNER_POS + Vec3(-12,0,-21),
				  'North East' : Building.SE_CORNER_POS + Vec3(0,0,-21) }
	EAST_APTS_POS = [Vec3(-10,0,-3), Vec3(-10,0,-9), Vec3(-10,0,-15)]
	WEST_APTS_POS = [Vec3(-2,0,-10), Vec3(-2,0,-15), Vec3(-2,0,-21)]
	
	WEST_FARMS_POS = [Vec3(-16,0,-7), Vec3(-16,0,-14), Vec3(-16,0,-21)]
	NORTH_FARMS_POS = [Vec3(0,0,-25), Vec3(-12,0,-25)]

	END_WINS_POS = [Vec3(-4,0,-3), Vec3(-8,0,-3), Vec3(-4,0,-21), Vec3(-8,0,-21)]

	WIDTH = 26 
	def __init__(self, *args, **kwargs):
		super(ApartmentBlock, self).__init__(width=ApartmentBlock.WIDTH, *args, **kwargs)

		# Apartment & farm sub-building objects & placement positions for each
		# Add the apartment subbuildings
		apartments = [Apartment(Building.EAST), # west facing apt built to east
		 		      Apartment(Building.WEST)] # east facing built to west of player posn
		
		for pos in ApartmentBlock.EAST_APTS_POS:
			self.add_subbuilding(apartments[0], pos)
			self.add_subbuilding(apartments[0], pos + Vec3(0,4,0))
		for pos in ApartmentBlock.WEST_APTS_POS:
			self.add_subbuilding(apartments[1], pos)
			self.add_subbuilding(apartments[1], pos + Vec3(0,4,0))

		# Add the farm subbuildings
		farms = [Farm(Building.WEST),
				 LargeFarm(Building.NORTH)]

		for pos in ApartmentBlock.WEST_FARMS_POS:
			self.add_subbuilding(farms[0], pos)
		for pos in ApartmentBlock.NORTH_FARMS_POS:
			self.add_subbuilding(farms[1], pos)


		# Add the streets between as subbuildings
		street = Street(Building.NORTH)
		for i in range(0,9):
			self.add_subbuilding(street, Vec3(i*-3,0,3))
			self.add_subbuilding(street, Vec3(i*-3,0,-22))
			if i < 8:
				self.add_subbuilding(street, Vec3(-13,0,i*-3))


		#######################################################################
		# level 0 blocks.
		layer_blocks = []
		# cobblestone walk way
		layer_blocks.extend(self._add_walkway(block.COBBLESTONE))
		# cobblestone steps at end of each walkway
		layer_blocks.append(Stair(ApartmentBlock.CORNER_POS['South East'] + Vec3(0,0,1), 
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
		layer_blocks.append(BuildingBlock(ApartmentBlock.CORNER_POS['South East'] + Vec3(-7,0,1), 
								block.WOOD_PLANKS,
								description="Steps to upper floor"))

		self.add_layer(BuildingLayer(layer_blocks, 0))
		del layer_blocks [:]

		#######################################################################
		# levels 1 - 3 blocks
		# fence posts at each corner
		for i in range(1,4):
			for pos in ApartmentBlock.CORNER_POS.values():
				layer_blocks.append(BuildingBlock(pos, block.FENCE, description="Corner post"))

			# wooden steps to 2nd floor.
			layer_blocks.append(Stair(ApartmentBlock.CORNER_POS['South East'] + Vec3(-8+i,0,1), 
									block.STAIRS_WOOD.withData(Stair.EAST),
									description="Steps to upper floor"))
			layer_blocks.append(BuildingBlock(ApartmentBlock.CORNER_POS['South East'] + Vec3(-7+i,0,1), 
									block.WOOD_PLANKS,
									description="Steps to upper floor"))

			self.add_layer(BuildingLayer(layer_blocks, i))
			del layer_blocks [:]

		#######################################################################
		# level 4 blocks
		# wooden walk way aroudn 2nd floor
		layer_blocks.extend(self._add_walkway(block.WOOD_PLANKS))
		# wooden steps to 2nd floor.
		layer_blocks.append(Stair(ApartmentBlock.CORNER_POS['South East'] + Vec3(-4,0,1), 
								block.STAIRS_WOOD.withData(Stair.EAST),
								description="Steps to upper floor"))
		layer_blocks.append(BuildingBlock(ApartmentBlock.CORNER_POS['South East'] + Vec3(-3,0,1), 
								block.WOOD_PLANKS,
								description="Steps to upper floor"))

		self.add_layer(BuildingLayer(layer_blocks, 4))
		del layer_blocks [:]

		#######################################################################
		# level 5 blocks
		# west side railings
		layer_blocks.append(BuildingBlock(ApartmentBlock.CORNER_POS['North West'], 
										  block.FENCE, ApartmentBlock.CORNER_POS['South West'], 
										  description="Balcony railings"))
		# close off west side railings on north end
		layer_blocks.append(BuildingBlock(ApartmentBlock.CORNER_POS['North West'] + Vec3(1,0,0), 
										  block.FENCE, description="Balcony railings"))
		# east side railings
		layer_blocks.append(BuildingBlock(ApartmentBlock.CORNER_POS['North East'], 
										  block.FENCE, ApartmentBlock.CORNER_POS['South East'], 
										  description="Balcony railings"))
		# close off east side railings on north end
		layer_blocks.append(BuildingBlock(ApartmentBlock.CORNER_POS['North East'] + Vec3(-1,0,0), 
										  block.FENCE, description="Balcony railings"))

		# south balcony railings
		layer_blocks.append(BuildingBlock(ApartmentBlock.CORNER_POS['South East'], 
										  block.FENCE, ApartmentBlock.CORNER_POS['South East'] + Vec3(-5,0,0), 
										  description="Balcony railings"))
		layer_blocks.append(BuildingBlock(ApartmentBlock.CORNER_POS['South West'], 
										  block.FENCE, ApartmentBlock.CORNER_POS['South West'] + Vec3(6,0,0), 
										  description="Balcony railings"))

		self.add_layer(BuildingLayer(layer_blocks, 5))
		del layer_blocks [:]

		#######################################################################
		# Add the extra windows to the end apts on both levels.
		for pos in ApartmentBlock.END_WINS_POS:
			self._blocks.append(BuildingBlock(pos + Vec3(0,2,0), block.GLASS_PANE, description="End window"))
			self._blocks.append(BuildingBlock(pos + Vec3(0,6,0), block.GLASS_PANE, description="End window"))

		#######################################################################
		self._set_orientation()

	def _add_walkway(self, type):
		blocks = []
		blocks.append(BuildingBlock(ApartmentBlock.CORNER_POS['South East'] + Vec3(0,0,0), 
									type, ApartmentBlock.CORNER_POS['North East'] + Vec3(-1,0,0),
									description="East walkway"))
		blocks.append(BuildingBlock(ApartmentBlock.CORNER_POS['South West'] + Vec3(0,0,0), 
									type, ApartmentBlock.CORNER_POS['North West'] + Vec3(1,0,0),
									description="West walkway"))
		blocks.append(BuildingBlock(ApartmentBlock.CORNER_POS['South East'] + Vec3(0,0,0), 
									type, ApartmentBlock.CORNER_POS['South West'] + Vec3(0,0,-1),
									description="South walkway"))
		return blocks

