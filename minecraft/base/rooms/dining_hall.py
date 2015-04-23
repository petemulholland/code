from building import Building, BuildingEx, BuildingBlock, SubBuilding, Torch, Stair, Door
from base.fixtures import Fireplace
from base.types import PlankData, EXTERIOR_WALLS
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

# http://minecraft.gamepedia.com/Data_values#Block_IDs
from base.types import PlankData
# Dark Oak & acacia don't seem to be available in the version i'm using
# options are oak, birch, jungle & spruce (only 1 door wood)
#HALL_FLOOR = block.WOOD_PLANKS.withData(PlankData.SPRUCE)
HALL_FLOOR = block.WOOD_PLANKS.withData(PlankData.JUNGLE)
#HALL_FACIA = block.WOOD_PLANKS.withData(PlankData.JUNGLE)
HALL_FACIA = block.WOOD_PLANKS.withData(PlankData.BIRCH)
TABLE_TOP = Block(171, 12)
TABLE_PLACE = Block(171, 0)

class DiningHall(BuildingEx):
	# TODO: implement table & chairs, fireplaces & paintings on walls
	 #- dining hall 
	 #     - table 9x3
	 #     - +1 around for chairs
	 #     - +2 all around to leave space for ornaments
	 #     - carpet on table at chair positions for place settings
	 #     - => 13 x 9
	 #     - maybe 15 to 17  long for fireplaces at  both ends  - 20 long?
	 # 17 x 9 for fireplaces, 
	 # stone walls & wooden facian on interior => 21 x 13

	WALLS_CORNER_POS = {'South East' : Building.SE_CORNER_POS + Vec3(0,0,0), 
						'South West' : Building.SE_CORNER_POS + Vec3(-21,0,0),
						'North West' : Building.SE_CORNER_POS + Vec3(-21,0,-13),
						'North East' : Building.SE_CORNER_POS + Vec3(0,0,-13) }
	
	TABLE_SPAN = (WALLS_CORNER_POS['South East'] + Vec3(-6,0,-6),
				 WALLS_CORNER_POS['South East'] + Vec3(-14,0,-8))
	
	# chair position, orientation and table place offset from chair pos.
	CHAIR_POS = [(TABLE_SPAN[0] + Vec3(-1,0,1), Stair.SOUTH, Vec3(0,1,-1)),
				 (TABLE_SPAN[0] + Vec3(-3,0,1), Stair.SOUTH, Vec3(0,1,-1)),
				 (TABLE_SPAN[0] + Vec3(-5,0,1), Stair.SOUTH, Vec3(0,1,-1)),
				 (TABLE_SPAN[0] + Vec3(-7,0,1), Stair.SOUTH, Vec3(0,1,-1)),
				 (TABLE_SPAN[0] + Vec3(-9,0,-1), Stair.WEST, Vec3(1,1,0)),
				 (TABLE_SPAN[0] + Vec3(-1,0,-3), Stair.NORTH, Vec3(0,1,1)),
				 (TABLE_SPAN[0] + Vec3(-3,0,-3), Stair.NORTH, Vec3(0,1,1)),
				 (TABLE_SPAN[0] + Vec3(-5,0,-3), Stair.NORTH, Vec3(0,1,1)),
				 (TABLE_SPAN[0] + Vec3(-7,0,-3), Stair.NORTH, Vec3(0,1,1)),
				 (TABLE_SPAN[0] + Vec3(1,0,-1), Stair.EAST, Vec3(-1,1,0))
				]

	FIREPLACE_POS = [WALLS_CORNER_POS['South East'] + Vec3(-3,0,-6),
					 WALLS_CORNER_POS['South East'] + Vec3(3,0,-9)]

	MAIN_DOOR_SPANS = [(Building.SE_CORNER_POS + Vec3(-7,0,0),
						Building.SE_CORNER_POS + Vec3(-8,1,-1)),
					   (Building.SE_CORNER_POS + Vec3(-13,0,0),
						Building.SE_CORNER_POS + Vec3(-14,1,-1))]
	KITCHEN_DOOR = (Building.SE_CORNER_POS + Vec3(-17,0,0),
					Building.SE_CORNER_POS + Vec3(-17,1,-1))
												  
	WINDOW_SPANS = [(WALLS_CORNER_POS['North East'] + Vec3(-5,1,0),
					 WALLS_CORNER_POS['North East'] + Vec3(-5,2,1)),
					(WALLS_CORNER_POS['North East'] + Vec3(-9,1,0),
					 WALLS_CORNER_POS['North East'] + Vec3(-9,2,1)),
					(WALLS_CORNER_POS['North East'] + Vec3(-13,1,0),
					 WALLS_CORNER_POS['North East'] + Vec3(-13,2,1)),
					(WALLS_CORNER_POS['North East'] + Vec3(-17,1,0),
					 WALLS_CORNER_POS['North East'] + Vec3(-17,2,1))]
	# pressure plates don't join up, use carpet instead

	WALL_HEIGHT = 3 # 0-3 =>4, can't be arsed doing a -1 everywhere

	WIDTH = WALLS_CORNER_POS['South East'].x - WALLS_CORNER_POS['South West'].x
	
	# TODO: want to update/extend Building class to use ordered list of collections idea
	# add blocks/block spans to a collection 
	def __init__(self, *args, **kwargs):
		super(DiningHall, self).__init__(width=DiningHall.WIDTH, *args, **kwargs)

		# create walls
		builds = []

		builds.append(BuildingBlock(DiningHall.WALLS_CORNER_POS['South East'],
									EXTERIOR_WALLS, 
									DiningHall.WALLS_CORNER_POS['North West'] + Vec3(0,DiningHall.WALL_HEIGHT,0),
									description="Wall fill"))
		builds.append(BuildingBlock(DiningHall.WALLS_CORNER_POS['South East'] + Vec3(-1,0,-1),
									HALL_FACIA, 
									DiningHall.WALLS_CORNER_POS['North West'] + Vec3(1,DiningHall.WALL_HEIGHT,1),
									description="facia fill"))
		builds.append(BuildingBlock(DiningHall.WALLS_CORNER_POS['South East'] + Vec3(-2,0,-2),
									block.AIR, 
									DiningHall.WALLS_CORNER_POS['North West'] + Vec3(2,DiningHall.WALL_HEIGHT,2),
									description="clear interior"))
		builds.append(BuildingBlock(DiningHall.WALLS_CORNER_POS['South East'] + Vec3(-1,-1,-1),
									HALL_FLOOR, 
									DiningHall.WALLS_CORNER_POS['North West'] + Vec3(1,-1,1),
									description="floor"))
				 
		self._add_section("RoomShell", builds)

		# create doors & windows
		builds.append(BuildingBlock(DiningHall.MAIN_DOOR_SPANS[0][0],
									block.AIR, 
									DiningHall.MAIN_DOOR_SPANS[0][1],
									description="Clear door"))
		builds.append(BuildingBlock(DiningHall.MAIN_DOOR_SPANS[1][0],
									block.AIR, 
									DiningHall.MAIN_DOOR_SPANS[1][1],
									description="Clear door"))
		builds.append(BuildingBlock(DiningHall.KITCHEN_DOOR[0],
									block.AIR, 
									DiningHall.KITCHEN_DOOR[1],
									description="Clear door"))

		for span in DiningHall.WINDOW_SPANS:
			builds.append(BuildingBlock(span[0], block.AIR, 
										span[1], description="Clear window"))
			builds.append(BuildingBlock(span[0], block.GLASS_PANE, 
										span[0]+ Vec3(0,1,0), description="Window pane"))

		builds.append(Door(Door.HINGE_RIGHT, 
							DiningHall.MAIN_DOOR_SPANS[0][0] + Vec3(0,0,-1), 
							block.DOOR_WOOD.withData(Door.SOUTH),
							description="Door"))
		builds.append(Door(Door.HINGE_LEFT, 
							DiningHall.MAIN_DOOR_SPANS[0][0] + Vec3(-1,0,-1), 
							block.DOOR_WOOD.withData(Door.SOUTH),
							description="Door"))
		builds.append(Door(Door.HINGE_RIGHT, 
							DiningHall.MAIN_DOOR_SPANS[1][0] + Vec3(0,0,-1), 
							block.DOOR_WOOD.withData(Door.SOUTH),
							description="Door"))
		builds.append(Door(Door.HINGE_LEFT, 
							DiningHall.MAIN_DOOR_SPANS[1][0] + Vec3(-1,0,-1), 
							block.DOOR_WOOD.withData(Door.SOUTH),
							description="Door"))
		builds.append(Door(Door.HINGE_LEFT, 
							DiningHall.KITCHEN_DOOR[0] + Vec3(0,0,-1), 
							block.DOOR_WOOD.withData(Door.SOUTH),
							description="Door"))
		
		self._add_section("WallOpenings", builds)
		
		# add table & chairs
		builds.append(BuildingBlock(DiningHall.TABLE_SPAN[0],
									block.FENCE, 
									DiningHall.TABLE_SPAN[1],
									description="Table base"))
		builds.append(BuildingBlock(DiningHall.TABLE_SPAN[0] + Vec3(0,1,0),
									TABLE_TOP, 
									DiningHall.TABLE_SPAN[1] + Vec3(0,1,0),
									description="Table top"))
		# chairs & table place settings
		for pos, orientation, place_offset in DiningHall.CHAIR_POS:
			builds.append(Stair(pos, 
								block.STAIRS_WOOD.withData(orientation), 
								description="Chair"))
			builds.append(BuildingBlock(pos + place_offset,
										TABLE_PLACE, 
										description="Table place setting"))

		self._add_section("Table", builds)
		
		# add fireplaces
		builds.append(SubBuilding(Fireplace(Building.EAST), DiningHall.FIREPLACE_POS[0]))
		builds.append(SubBuilding(Fireplace(Building.WEST), DiningHall.FIREPLACE_POS[1]))
		self._add_section("Fireplaces", builds)

		# add Torches
		#self._add_section("xxx", builds)


		self._set_orientation()


