from building import Building, BuildingEx, BuildingBlock, SubBuilding, Torch, Stair, Door
from base.fixtures import Fireplace
from base.constants import EXTERIOR_WALLS, WALL_HEIGHT
from building.types import PlankData
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

# http://minecraft.gamepedia.com/Data_values#Block_IDs

HALL_FLOOR = block.WOOD_PLANKS.withData(PlankData.SPRUCE)
HALL_FACIA = block.WOOD_PLANKS.withData(PlankData.JUNGLE)
TABLE_TOP = Block(171, 12)
TABLE_PLACE = Block(171, 0)

# TODO: rework positions with laid out plan for castle ground floor.
#       
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
						'South West' : Building.SE_CORNER_POS + Vec3(-27,0,0),
						'North West' : Building.SE_CORNER_POS + Vec3(-27,0,-13),
						'North East' : Building.SE_CORNER_POS + Vec3(0,0,-13) }

	WIDTH = WALLS_CORNER_POS['South East'].x - (WALLS_CORNER_POS['South West'].x - 1)
	
	TABLE_SPAN = (WALLS_CORNER_POS['South East'] + Vec3(-9,0,-6),
				 WALLS_CORNER_POS['South East'] + Vec3(-19,0,-8))
	
	# TODO get table length/2 for number of chairs on long sides.
	#       use this data to place chairs & place settings in a loop
	# chair position, orientation and table place offset from chair pos.
	CHAIR_POS = [(TABLE_SPAN[0] + Vec3(-1,0,1), Stair.SOUTH, Vec3(0,1,-1)),
				 (TABLE_SPAN[0] + Vec3(-3,0,1), Stair.SOUTH, Vec3(0,1,-1)),
				 (TABLE_SPAN[0] + Vec3(-5,0,1), Stair.SOUTH, Vec3(0,1,-1)),
				 (TABLE_SPAN[0] + Vec3(-7,0,1), Stair.SOUTH, Vec3(0,1,-1)),
				 (TABLE_SPAN[0] + Vec3(-9,0,1), Stair.SOUTH, Vec3(0,1,-1)),
				 (TABLE_SPAN[0] + Vec3(-11,0,-1), Stair.WEST, Vec3(1,1,0)),
				 (TABLE_SPAN[0] + Vec3(-1,0,-3), Stair.NORTH, Vec3(0,1,1)),
				 (TABLE_SPAN[0] + Vec3(-3,0,-3), Stair.NORTH, Vec3(0,1,1)),
				 (TABLE_SPAN[0] + Vec3(-5,0,-3), Stair.NORTH, Vec3(0,1,1)),
				 (TABLE_SPAN[0] + Vec3(-7,0,-3), Stair.NORTH, Vec3(0,1,1)),
				 (TABLE_SPAN[0] + Vec3(-9,0,-3), Stair.NORTH, Vec3(0,1,1)),
				 (TABLE_SPAN[0] + Vec3(1,0,-1), Stair.EAST, Vec3(-1,1,0))
				]

	FIREPLACE_POS = [WALLS_CORNER_POS['South East'] + Vec3(-3,-1,-5),
					 WALLS_CORNER_POS['South West'] + Vec3(3,-1,-8)]

	# TODO: calculate these as 3 blocks each way from center point of room
	# => width/2 +/- 3 
	MAIN_DOOR_SPANS = [(Building.SE_CORNER_POS + Vec3(-(WIDTH/2)-2,0,0),
						Building.SE_CORNER_POS + Vec3(-(WIDTH/2)-3,1,-1)),
					   (Building.SE_CORNER_POS + Vec3(-(WIDTH/2)+3,0,0),
						Building.SE_CORNER_POS + Vec3(-(WIDTH/2)+4,1,-1))]
	
	# TODO: fix this from the SW corner +6
	KITCHEN_DOOR = (WALLS_CORNER_POS['South West'] + Vec3(5,0,0),
					WALLS_CORNER_POS['South West'] + Vec3(5,1,-1))
	
	def __init__(self, *args, **kwargs):
		super(DiningHall, self).__init__(width=DiningHall.WIDTH, *args, **kwargs)

	def _create_structure(self):
		super(DiningHall, self)._create_structure()
		# create walls
		builds = []

		builds.append(BuildingBlock(DiningHall.WALLS_CORNER_POS['South East'],
									EXTERIOR_WALLS, 
									DiningHall.WALLS_CORNER_POS['North West'] + Vec3(0,WALL_HEIGHT,0),
									description="Wall fill"))
		builds.append(BuildingBlock(DiningHall.WALLS_CORNER_POS['South East'] + Vec3(-1,0,-1),
									HALL_FACIA, 
									DiningHall.WALLS_CORNER_POS['North West'] + Vec3(1,WALL_HEIGHT,1),
									description="facia fill"))
		builds.append(BuildingBlock(DiningHall.WALLS_CORNER_POS['South East'] + Vec3(-2,0,-2),
									block.AIR, 
									DiningHall.WALLS_CORNER_POS['North West'] + Vec3(2,WALL_HEIGHT,2),
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

		for x in range(5,25,4):
			builds.append(BuildingBlock(DiningHall.WALLS_CORNER_POS['North East'] + Vec3(-x,1,0), 
										block.AIR, 
										DiningHall.WALLS_CORNER_POS['North East'] + Vec3(-x,2,1), 
										description="Clear window"))
			builds.append(BuildingBlock(DiningHall.WALLS_CORNER_POS['North East'] + Vec3(-x,1,0), 
										block.GLASS_PANE, 
										DiningHall.WALLS_CORNER_POS['North East'] + Vec3(-x,2,0),
										description="Window pane"))

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



