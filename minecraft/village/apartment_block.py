from building import BuildingBlock, Building, BuildingEx, SubBuilding
from farm import Farm, LargeFarm
from street import Street
from oriented_blocks import Stair, Torch, Door
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

# increased delays between section builds didn't appear to prevent bukkit from crashing
# using BuildingEx to reduce number of required setBlock calls
# build time has reduced from 40s to 15s with updated build.
# TODO: wrap setBlock calls with a counter?

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

DO_2ND_FLOOR_RAILINGS = False

class ApartmentBlock(BuildingEx):
	# full stone span
	APT_BLOCK_SPAN = (Building.SE_CORNER_POS + Vec3(-2,0,-3),
					  Building.SE_CORNER_POS + Vec3(-10,8,-21))
	# span of bottom, SE span for wood plank span through apt block above.
	# there'll be 3 east-west and 2 north-south on each floor
	# wood plank positions in next collection are relative to this span.

	# TODO: for spans applied at multiple positions, maybe adjust the spans to start at 0,0,0
	#       and apply positions relative to SE corner (of entire building or just apt block super structure?)
	WOOD_PLANK_SPANS = {"East West" : (Building.SE_CORNER_POS + Vec3(-2,1,-4),
										Building.SE_CORNER_POS + Vec3(-10,3,-8)),
						"North South": (Building.SE_CORNER_POS + Vec3(-3,1,-3),
										Building.SE_CORNER_POS + Vec3(-5,3,-21))
						}

	WOOD_PLANK_POS = {"East West" : [Vec3(0,0,0), Vec3(0,0,-6), Vec3(0,0,-12)],
					  "North South": [Vec3(0,0,0), Vec3(-4,0,0)]
					 }

	# span for bottom SE apartment interior
	# Positions relative to this span are in the next collection
	APT_INTERIOR_SPAN = (Building.SE_CORNER_POS + Vec3(-3,1,-4),
						 Building.SE_CORNER_POS + Vec3(-5,3,-8))
	APT_INTERIOR_POS = [Vec3(0,0,0), Vec3(0,0,-6), Vec3(0,0,-12),
						Vec3(-4,0,0), Vec3(-4,0,-6), Vec3(-4,0,-12)]

	APT_DOORS_POS = { "East" : [Building.SE_CORNER_POS + Vec3(-2,1,-5),
								Building.SE_CORNER_POS + Vec3(-2,1,-11),
								Building.SE_CORNER_POS + Vec3(-2,1,-17)
							   ],
					  "West" : [Building.SE_CORNER_POS + Vec3(-10,1,-5),
								Building.SE_CORNER_POS + Vec3(-10,1,-11),
								Building.SE_CORNER_POS + Vec3(-10,1,-17)
								]
					}

	APT_WINS_POS = [Building.SE_CORNER_POS + Vec3(-2,2,-7),
					Building.SE_CORNER_POS + Vec3(-2,2,-13),
					Building.SE_CORNER_POS + Vec3(-2,2,-19),
					Building.SE_CORNER_POS + Vec3(-10,2,-7),
					Building.SE_CORNER_POS + Vec3(-10,2,-13),
					Building.SE_CORNER_POS + Vec3(-10,2,-19),
					Building.SE_CORNER_POS + Vec3(-5,2,-3),
					Building.SE_CORNER_POS + Vec3(-8,2,-3),
					Building.SE_CORNER_POS + Vec3(-5,2,-21),
					Building.SE_CORNER_POS + Vec3(-8,2,-21)]
	
	# corner positions for apt block span including walkways, but not steps
	CORNER_POS = {'South East' : Building.SE_CORNER_POS + Vec3(0,0,-1), 
				  'South West' : Building.SE_CORNER_POS + Vec3(-12,0,-1),
				  'North West' : Building.SE_CORNER_POS + Vec3(-12,0,-21),
				  'North East' : Building.SE_CORNER_POS + Vec3(0,0,-21) }
	WEST_FARMS_POS = [Building.SE_CORNER_POS + Vec3(-16,0,-7), 
					  Building.SE_CORNER_POS + Vec3(-16,0,-14), 
					  Building.SE_CORNER_POS + Vec3(-16,0,-21)]
	NORTH_FARMS_POS = [Building.SE_CORNER_POS + Vec3(0,0,-25), 
					   Building.SE_CORNER_POS + Vec3(-12,0,-25)]


	WIDTH = 26 
	def __init__(self, *args, **kwargs):
		super(ApartmentBlock, self).__init__(width=ApartmentBlock.WIDTH, *args, **kwargs)

		builds = []
		#######################################################################
		# build entire apt block from spans:
		# "concrete" structure (smooth stone)
		builds.append(BuildingBlock(ApartmentBlock.APT_BLOCK_SPAN[0], block.STONE,
									ApartmentBlock.APT_BLOCK_SPAN[1], 
									description="Apt block stone super structure"))

		# 17 apt wall sections per floor can be done using 5 wood spans & 6 interior spaces
		# build wood plank spans
		for key, span in ApartmentBlock.WOOD_PLANK_SPANS.items():
			for pos in ApartmentBlock.WOOD_PLANK_POS[key]:
				# ground floor
				builds.append(BuildingBlock(span[0] + pos, block.WOOD_PLANKS,
											span[1] + pos, 
											description="%s wood span ground floor"%(key)))

				# 2nd floor
				builds.append(BuildingBlock(span[0] + pos + Vec3(0,4,0), block.WOOD_PLANKS,
											span[1] + pos + Vec3(0,4,0), 
											description="%s wood span 2nd floor"%(key)))
		# clear apt interiors (this will leave concrete floors & ceilings)
		for pos in ApartmentBlock.APT_INTERIOR_POS:
			# ground floor
			builds.append(BuildingBlock(ApartmentBlock.APT_INTERIOR_SPAN[0] + pos, block.AIR,
										ApartmentBlock.APT_INTERIOR_SPAN[1] + pos, 
										description="Clear apt interior ground floor"))

			# 2nd floor
			builds.append(BuildingBlock(ApartmentBlock.APT_INTERIOR_SPAN[0] + pos + Vec3(0,4,0), block.AIR,
										ApartmentBlock.APT_INTERIOR_SPAN[1] + pos + Vec3(0,4,0), 
										description="Clear apt interior 2nd floor"))

		# doors & torches
		# TODO: debug this: East side apartments have doors "facing" east (built on east side of block)
		#					East side apts torches should face west, but applied on east face of containing block (west face of support block)
		# TODO: add doc strings to doors and torches on what the orientation means
		for pos in ApartmentBlock.APT_DOORS_POS["East"]:
			# ground floor
			builds.append(Door(Door.HINGE_RIGHT, pos, 
								block.DOOR_WOOD.withData(Door.WEST),
								description="Ground floor door east side"))
			builds.append(Torch(pos + Vec3(-1,2,0), block.TORCH.withData(Torch.EAST), 
								description="Ground floor torch"))
			# 2nd floor
			builds.append(Door(Door.HINGE_RIGHT, pos + Vec3(0,4,0), 
								block.DOOR_WOOD.withData(Door.WEST),
								description="2nd floor door east side"))
			builds.append(Torch(pos + Vec3(-1,6,0), block.TORCH.withData(Torch.EAST), 
								description="2nd floor torch"))

		for pos in ApartmentBlock.APT_DOORS_POS["West"]:
			# ground floor
			builds.append(Door(Door.HINGE_LEFT, pos, 
								block.DOOR_WOOD.withData(Door.EAST),
								description="Ground floor door west side"))
			builds.append(Torch(pos + Vec3(1,2,0), block.TORCH.withData(Torch.WEST), 
								description="Ground floor torch"))
			# 2nd floor
			builds.append(Door(Door.HINGE_LEFT, pos + Vec3(0,4,0), 
								block.DOOR_WOOD.withData(Door.EAST),
								description="2nd floor door west side"))
			builds.append(Torch(pos + Vec3(1,6,0), block.TORCH.withData(Torch.WEST), 
								description="2nd floor torch"))

		# windows
		for pos in ApartmentBlock.APT_WINS_POS:
			builds.append(BuildingBlock(pos, block.GLASS_PANE, description="ground floor window"))
			builds.append(BuildingBlock(pos + Vec3(0,4,0), block.GLASS_PANE, description="2nd floor window"))

		self._add_section("Apt block", builds)

		#######################################################################
		# Ground floor walkway & steps
		# stone walk way
		builds.extend(self._add_walkway(block.STONE, 0))
		# stone steps at end of each walkway
		# TODO: block data for stone brick stairs
		builds.append(Stair(ApartmentBlock.CORNER_POS['South East'] + Vec3(0,0,1), 
								block.STAIRS_COBBLESTONE.withData(Stair.NORTH),
								ApartmentBlock.CORNER_POS['South East'] + Vec3(-1,0,1),
								description="Ground floor steps"))
		builds.append(Stair(ApartmentBlock.CORNER_POS['South West'] + Vec3(1,0,1), 
								block.STAIRS_COBBLESTONE.withData(Stair.NORTH),
								ApartmentBlock.CORNER_POS['South West'] + Vec3(0,0,1),
								description="Ground floor steps"))

		self._add_section("Ground floor walkway", builds)

		#######################################################################
		# Support posts for 2nd floor walkway
		for pos in ApartmentBlock.CORNER_POS.values():
			builds.append(BuildingBlock(pos + Vec3(0,1,0), block.FENCE, 
									    pos + Vec3(0,3,0), 
										description="Corner post"))

		self._add_section("2nd floor support posts", builds)

		#######################################################################
		# 2nd floor walkway
		# wooden walk way around 2nd floor
		builds.extend(self._add_walkway(block.WOOD_PLANKS, 4))
		self._add_section("2nd floor wooden walkway", builds)

		#######################################################################
		# Stairs to 2nd floor
		for i in range(0,5):
			# wooden steps to 2nd floor.
			builds.append(Stair(ApartmentBlock.CORNER_POS['South East'] + Vec3(-8+i,i,1), 
									block.STAIRS_WOOD.withData(Stair.EAST),
									description="Steps to upper floor"))
			# TODO: figure out block data for upside down stairs and use this instead of support block
			builds.append(BuildingBlock(ApartmentBlock.CORNER_POS['South East'] + Vec3(-7+i,i,1), 
									block.WOOD_PLANKS,
									description="stair support"))

		self._add_section("Stairs to 2nd floor", builds)

		#######################################################################
		if DO_2ND_FLOOR_RAILINGS:
			# 2nd floor walkway railings (should extend these out by 1 block all around so walkway is 2 blocks wide)
			# west side railings
			builds.append(BuildingBlock(ApartmentBlock.CORNER_POS['North West'] + Vec3(0,5,0), 
										block.FENCE, ApartmentBlock.CORNER_POS['South West'] + Vec3(0,5,0), 
										description="Balcony railings"))
			# close off west side railings on north end
			builds.append(BuildingBlock(ApartmentBlock.CORNER_POS['North West'] + Vec3(1,5,0), 
										block.FENCE, description="Balcony railings"))
			# east side railings
			builds.append(BuildingBlock(ApartmentBlock.CORNER_POS['North East'] + Vec3(0,5,0), 
										block.FENCE, ApartmentBlock.CORNER_POS['South East'] + Vec3(0,5,0), 
										description="Balcony railings"))
			# close off east side railings on north end
			builds.append(BuildingBlock(ApartmentBlock.CORNER_POS['North East'] + Vec3(-1,5,0), 
										block.FENCE, description="Balcony railings"))

			# south balcony railings
			builds.append(BuildingBlock(ApartmentBlock.CORNER_POS['South East'] + Vec3(0,5,0), 
										block.FENCE, ApartmentBlock.CORNER_POS['South East'] + Vec3(-5,5,0), 
										description="Balcony railings"))
			builds.append(BuildingBlock(ApartmentBlock.CORNER_POS['South West'] + Vec3(0,5,0), 
										block.FENCE, ApartmentBlock.CORNER_POS['South West'] + Vec3(6,5,0), 
										description="Balcony railings"))

			self._add_section("2nd floor railings", builds)

		#######################################################################
		# Add the streets between as subbuildings
		street_ew = Street(9, Building.WEST)
		street_ns = Street(8, Building.NORTH)

		builds.append(SubBuilding(street_ew, Building.SE_CORNER_POS + Vec3(0,0,1)))
		builds.append(SubBuilding(street_ew, Building.SE_CORNER_POS + Vec3(0,0,-24)))
		builds.append(SubBuilding(street_ns, Building.SE_CORNER_POS + Vec3(-13,0,0)))
		
		self._add_section("Streets", builds)

		#######################################################################
		# Add the farm subbuildings
		farms = [Farm(Building.WEST),
				 LargeFarm(Building.NORTH)]

		for pos in ApartmentBlock.WEST_FARMS_POS:
			builds.append(SubBuilding(farms[0], pos))
		for pos in ApartmentBlock.NORTH_FARMS_POS:
			builds.append(SubBuilding(farms[1], pos))

		self._add_section("Farms", builds)

		#######################################################################
		self._set_orientation()

	def _add_walkway(self, type, level):
		blocks = []
		blocks.append(BuildingBlock(ApartmentBlock.CORNER_POS['South East'] + Vec3(0,level,0), 
									type, ApartmentBlock.CORNER_POS['North East'] + Vec3(-1,level,0),
									description="East walkway"))
		blocks.append(BuildingBlock(ApartmentBlock.CORNER_POS['South West'] + Vec3(0,level,0), 
									type, ApartmentBlock.CORNER_POS['North West'] + Vec3(1,level,0),
									description="West walkway"))
		blocks.append(BuildingBlock(ApartmentBlock.CORNER_POS['South East'] + Vec3(0,level,0), 
									type, ApartmentBlock.CORNER_POS['South West'] + Vec3(0,level,-1),
									description="South walkway"))
		return blocks

