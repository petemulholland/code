from building import Building, BuildingEx, BuildingBlock, SubBuilding, Torch, Door
from base.constants import *
from base.rooms import *
from base.fixtures import *
from base.enclosure import *
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

# castle ground floor plan
#   sss                        sss   5
#  s   s                      s   s  4
# s     s                    s     s 3
# s  s  ssssgsssgsssgsssgsssss  s  s 2
# s   ww www www www www www www   s 1
#  s  w                        w  s  03
#   ssw                        wss    9
#    sw                        ws    8
#    swff     c c c c c      ffws    7
#    swff    ttttttttttt     ffws    6
#    swff   ctttttttttttc    ffws    5
#    swff    ttttttttttt     ffws    4
#    sw       c c c c c        ws    3
#    sw                        ws    2
#    sw                        ws    1
#    swwwwdwwwddwwwwwwddwwwwwwwws    02
#    sssss sss  ssssss  sssssssss    9
#    d          xxwwxx          d    8
#    sssss ss   xxwwxx   ssssssss    7
#    s      s     xx     sbbbbb s    6
#    s      s     xx     sb     s    5 
#    s            xx     sb     s    4
#    s            xx     sb     s    3
#    s      s                   s    2
#    s      s                   s    1
#    ssss  ss   p    p   ss  ssss    01
#    s      s            s      s    9
#    s      s            s      s    8
#    s                          s    7
#   ss                          ss   6
#  s        s            s        s  5 
# s         s    sdds    s         s 4
# s  s  ssssssssss  ssssssssss  s  s 3
# s     s                    s     s 2
#  s   s                      s   s  1
#   sss                        sss   0
# 
# 3210987654321098765432109876543210
#    3         2         1          

class Castle(BuildingEx):
	# * all levels 4 spaces high (need 6 for smelting room (willneed to borrow 1 space from floor & ceiling)
	#      Mine entrance room somewhere, stairs to base ment under main stairs
	#
	# * Both ceilings support beams
	#   N-S beams over side room walls would only be visible in corridors & large north rooms
	#   but would allow embedding support columns in room walls.
	#	- N-S beams/rafters at: -7 & -20
	#   - E-W beams/rafters at: -6, -12, -18 & -24
	#   - 2nd floor support posts at N: - 7 & -16, would be supported below by stone walls
	#
	#		draft build order:
	#		floor (stone bricks) 2 layers
	#		castle walls 
	#		ground floor rooms
	#		corner turrets - 3x3 interior square surrounded with walls 3m long, no coner blocks (for a 5x5 "circle")
	#			- start turrets from seconds floor tapering in to wall on ground floor
	#		any remaining walls, windows & doors
	#		2nd floor floor
	#		main stairs & balcony
	#		2nd floor rooms
	#		corner turrets
	#		any remaining walls & windows
	#		balconys & doors
	#		rafters & support beams
	#		roof
	#		basement, stairs, corridor, mushroom farm, target practice, portal, mine access & mob farm access
	# Think about mob jail for curing villager to add to village
	# 
	# Probably going to need soul sand & nether wart farm for brewing potions
	#
	WALLS_CORNER_POS = {'South East' : Building.SE_CORNER_POS + Vec3(-3,0,-3), 
						'South West' : Building.SE_CORNER_POS + Vec3(-30,0,-3),
						'North West' : Building.SE_CORNER_POS + Vec3(-30,0,-32),
						'North East' : Building.SE_CORNER_POS + Vec3(-3,0,-32) }
	
	WIDTH = 34
	def __init__(self, *args, **kwargs):
		super(Castle, self).__init__(width=Castle.WIDTH, *args, **kwargs)
		self.upper_floor_level = WALL_HEIGHT + 1
		self.second_storey_level = self.upper_floor_level + 2
		self.ceiling_level = self.second_storey_level + self.upper_floor_level
						
	###########################################################################
	# utility methods
	def _create_surrounding_walls(self, description, level):
		builds = []
		# build surrounding walls
		builds.append(BuildingBlock(Castle.WALLS_CORNER_POS['South East'] + Vec3(0,level,0),
									EXTERIOR_WALLS,
									Castle.WALLS_CORNER_POS['South West'] + Vec3(0,WALL_HEIGHT + level,0),
									description="South wall"))
		builds.append(BuildingBlock(Castle.WALLS_CORNER_POS['South West'] + Vec3(0,level,0),
									EXTERIOR_WALLS,
									Castle.WALLS_CORNER_POS['North West'] + Vec3(0,WALL_HEIGHT + level,0),
									description="West wall"))
		builds.append(BuildingBlock(Castle.WALLS_CORNER_POS['South East'] + Vec3(0,level,0),
									EXTERIOR_WALLS,
									Castle.WALLS_CORNER_POS['North East'] + Vec3(0,WALL_HEIGHT + level,0),
									description="East wall"))
		builds.append(BuildingBlock(Castle.WALLS_CORNER_POS['North East'] + Vec3(0,level,0),
									EXTERIOR_WALLS,
									Castle.WALLS_CORNER_POS['North West'] + Vec3(0,WALL_HEIGHT + level,0),
									description="North wall"))
		self._add_section(description, builds)

	###########################################################################
	# ground floor structure
	def _create_ground_floor_skeleton(self):
		builds = []
		builds.append(SubBuilding(GroundFloor(Building.NORTH), Castle.WALLS_CORNER_POS['South East']))
		self._add_section("Floor", builds)

		self._create_surrounding_walls("Ground floor enclosing walls", 0)

		# Side doors
		builds.append(Door(Door.HINGE_LEFT, 
							Castle.WALLS_CORNER_POS['South East'] + Vec3(0,0,-15),
							block.DOOR_WOOD.withData(Door.EAST),
							description="East side door"))
		builds.append(Door(Door.HINGE_RIGHT, 
							Castle.WALLS_CORNER_POS['South West'] + Vec3(0,0,-15),
							block.DOOR_WOOD.withData(Door.WEST),
							description="West side door"))

		# Front wall & door
		builds.append(Door(Door.HINGE_RIGHT, 
							Castle.WALLS_CORNER_POS['South East'] + Vec3(-13,0,0),
							block.DOOR_WOOD.withData(Door.SOUTH),
							description="Front door"))
		builds.append(Door(Door.HINGE_LEFT, 
							Castle.WALLS_CORNER_POS['South East'] + Vec3(-14,0,0),
							block.DOOR_WOOD.withData(Door.SOUTH),
							description="Front door"))
		self._add_section("Ground floor external doors", builds)

	def _create_ground_floor_rooms(self):
		builds = []
		builds.append(SubBuilding(DiningHall(Building.NORTH), 
								  Castle.WALLS_CORNER_POS['South East'] + Vec3(0,0,-16)))

		builds.append(SubBuilding(Kitchen(Building.WEST), 
								  Castle.WALLS_CORNER_POS['South East'] + Vec3(-20,0,-14)))
		builds.append(SubBuilding(Pantry(Building.WEST), 
								  Castle.WALLS_CORNER_POS['South East'] + Vec3(-20,0,-7)))

		builds.append(SubBuilding(EnchantingRoom(Building.EAST), 
								  Castle.WALLS_CORNER_POS['South East'] + Vec3(-7,0,-7)))
		builds.append(SubBuilding(Smithy(Building.EAST), 
								  Castle.WALLS_CORNER_POS['South East'] + Vec3(-7,0,0)))


		self._add_section("Ground floor rooms", builds)

	def _create_upper_floor_and_main_staircase(self):
		builds = []
		# after applying 2nd storey floor, add main stairs
		builds.append(SubBuilding(UpperFloor(Building.NORTH), 
								  Castle.WALLS_CORNER_POS['South East'] + Vec3(0,self.upper_floor_level,0)))
		builds.append(SubBuilding(MainStairs(Building.NORTH), 
								  Castle.WALLS_CORNER_POS['South East'] + Vec3(-11,0,-10)))
		self._add_section("Upper floor & staircase", builds)

	def _create_ground_floor_fittings(self):
		# TODO: add class for main doorway
		# add windows & torches 
		builds = []
		builds.append(SubBuilding(TurretTaper(Building.NORTH), Castle.WALLS_CORNER_POS['North West'] + Vec3(3,0,3)))
		builds.append(SubBuilding(TurretTaper(Building.EAST), Castle.WALLS_CORNER_POS['North East'] + Vec3(-3,0,3)))
		builds.append(SubBuilding(TurretTaper(Building.SOUTH), Castle.WALLS_CORNER_POS['South East'] + Vec3(-3,0,-3)))
		builds.append(SubBuilding(TurretTaper(Building.WEST), Castle.WALLS_CORNER_POS['South West'] + Vec3(3,0,-3)))
		self._add_section("Turret bases", builds)

		# torches over external side doors
		builds.append(Torch(Castle.WALLS_CORNER_POS['South East'] + Vec3(-1,2,-15),
							block.TORCH.withData(Torch.WEST)))
		builds.append(Torch(Castle.WALLS_CORNER_POS['South East'] + Vec3(-26,2,-15),
							block.TORCH.withData(Torch.EAST)))

		# torches a foyer end of corridors
		builds.append(Torch(Castle.WALLS_CORNER_POS['South East'] + Vec3(-8,2,-15),
							block.TORCH.withData(Torch.SOUTH)))
		builds.append(Torch(Castle.WALLS_CORNER_POS['South East'] + Vec3(-19,2,-15),
							block.TORCH.withData(Torch.SOUTH)))

		# torches on walls of kitchen & enchanting room
		builds.append(Torch(Castle.WALLS_CORNER_POS['South East'] + Vec3(-8,2,-10),
							block.TORCH.withData(Torch.WEST)))
		builds.append(Torch(Castle.WALLS_CORNER_POS['South East'] + Vec3(-19,2,-9),
							block.TORCH.withData(Torch.EAST)))

		# torches on walls of Pantry & smithy
		builds.append(Torch(Castle.WALLS_CORNER_POS['South East'] + Vec3(-8,2,-5),
							block.TORCH.withData(Torch.WEST)))
		builds.append(Torch(Castle.WALLS_CORNER_POS['South East'] + Vec3(-19,2,-5),
							block.TORCH.withData(Torch.EAST)))
		builds.append(Torch(Castle.WALLS_CORNER_POS['South East'] + Vec3(-8,2,-2),
							block.TORCH.withData(Torch.WEST)))
		builds.append(Torch(Castle.WALLS_CORNER_POS['South East'] + Vec3(-19,2,-2),
							block.TORCH.withData(Torch.EAST)))

		self._add_section("Ground floor torches", builds)

		builds.append(BuildingBlock(Castle.WALLS_CORNER_POS['South East'] + Vec3(-9,1,0),
									block.GLASS_PANE, 
									Castle.WALLS_CORNER_POS['South East'] + Vec3(-10,2,0),
									description="window"))
		builds.append(BuildingBlock(Castle.WALLS_CORNER_POS['South East'] + Vec3(-17,1,0),
									block.GLASS_PANE, 
									Castle.WALLS_CORNER_POS['South East'] + Vec3(-18,2,0),
									description="window"))


		self._add_section("Ground floor Windows", builds)

	def _create_ground_floor(self):
		# castle ground floor plan
		#
		# sssssssgsssgsssgsssgssssssss  9
		# sww www www www www www wwws  8
		# swb                      bws  7
		# swb                      bws  6
		# swb                      bws  5
		# swff     c c c c c      ffws  4
		# swff    ttttttttttt     ffws  3
		# swff   ctttttttttttc    ffws  2
		# swff    ttttttttttt     ffws  1
		# swb       c c c c c      bws  02
		# swb                      bws  9
		# swb                      bws  8
		# swwwwdwwwddwwwwwwddwwwwwwwws  7
		# sssss sss  ssssss  sssssssss  6
		# dT      T  xxwwxx  T      Td  5
		# sssss ss   xxwwxx   ssssssss  4
		# s      s     xx     sbbbbb s  3
		# s      s     xx     sb     s  2 
		# s            xx     sb     s  1
		# s            xx    Tsb     s  01
		# s      sT                  s  9
		# s      s                   s  8
		# ssss  ss   p    p   ss  ssss  7
		# s      s            s      s  6
		# s      sT          Ts      s  5
		# s                          s  4
		# s                          s  3
		# s      sT          Ts      s  2 
		# s      s    sdds    s      s  1
		# sssssssssGGss  ssGGsssssssss  0
		# 
		# 7654321098765432109876543210
		#        2         1          
		self._create_ground_floor_skeleton()
		self._create_ground_floor_rooms()
		self._create_upper_floor_and_main_staircase()
		self._create_ground_floor_fittings()

	###########################################################################
	# second floor structure
	def _create_second_floor_skeleton(self):
		self._create_surrounding_walls("Second floor enclosing walls", self.second_storey_level)
		# TODO: add windows & torches & turrets

	def _create_second_floor_turrets(self):
		builds = []

		nw_turret = Turret(Building.NORTH)
		nw_turret.set_access_enclosure_material(block.STONE_BRICK)
		builds.append(SubBuilding(nw_turret, Castle.WALLS_CORNER_POS['North West'] + Vec3(3,self.second_storey_level,3)))

		ne_turret = Turret(Building.NORTH)
		ne_turret.set_access_enclosure_material(block.STONE_BRICK)
		ne_turret.mirror()
		builds.append(SubBuilding(ne_turret, Castle.WALLS_CORNER_POS['North East'] + Vec3(3,self.second_storey_level,3)))

		sw_turret = Turret(Building.WEST)
		sw_turret.set_access_enclosure_material(block.STONE_BRICK)
		builds.append(SubBuilding(sw_turret, Castle.WALLS_CORNER_POS['South West'] + Vec3(3,self.second_storey_level,-3)))

		se_turret = Turret(Building.EAST)
		se_turret.set_access_enclosure_material(block.STONE_BRICK)
		se_turret.mirror()
		builds.append(SubBuilding(se_turret, Castle.WALLS_CORNER_POS['South East'] + Vec3(-3,self.second_storey_level,3)))

		self._add_section("Turrets", builds)

				
	def _create_second_floor_rooms(self):
		builds = []
		builds.append(SubBuilding(StoreRoom(Building.WEST), 
								  Castle.WALLS_CORNER_POS['South East'] + Vec3(-20,self.second_storey_level,-17)))
		builds.append(SubBuilding(DyeRoom(Building.EAST), 
								  Castle.WALLS_CORNER_POS['South East'] + Vec3(-7,self.second_storey_level,-3)))
		builds.append(SubBuilding(Brewery(Building.EAST), 
								  Castle.WALLS_CORNER_POS['South East'] + Vec3(-7,self.second_storey_level,-10)))

		builds.append(SubBuilding(CraftingRoom(Building.SOUTH), 
								  Castle.WALLS_CORNER_POS['South East'] + Vec3(-17,self.second_storey_level,-7)))

		builds.append(SubBuilding(Bedroom(Building.NORTH), 
								  Castle.WALLS_CORNER_POS['South East'] + Vec3(-3,self.second_storey_level,-20)))

		self._add_section("Second storey rooms", builds)

	def _create_second_floor_fittings(self):
		builds = []
		# TODO: add windows to turret access corridors
		# torches by north turret access points
		builds.append(Torch(Castle.WALLS_CORNER_POS['South East'] + Vec3(-2,self.second_storey_level+2,-25),
							block.TORCH.withData(Torch.SOUTH)))
		builds.append(Torch(Castle.WALLS_CORNER_POS['South East'] + Vec3(-25,self.second_storey_level+2,-25),
							block.TORCH.withData(Torch.SOUTH)))
		# torches on north turret access corridors
		builds.append(Torch(Castle.WALLS_CORNER_POS['South East'] + Vec3(-2,self.second_storey_level+2,-18),
							block.TORCH.withData(Torch.NORTH)))
		builds.append(Torch(Castle.WALLS_CORNER_POS['South East'] + Vec3(-25,self.second_storey_level+2,-18),
							block.TORCH.withData(Torch.NORTH)))

		# Bed room door torches
		builds.append(Torch(Castle.WALLS_CORNER_POS['South East'] + Vec3(-11,self.second_storey_level+2,-19),
							block.TORCH.withData(Torch.SOUTH)))
		builds.append(Torch(Castle.WALLS_CORNER_POS['South East'] + Vec3(-16,self.second_storey_level+2,-19),
							block.TORCH.withData(Torch.SOUTH)))
		# east room torches
		builds.append(Torch(Castle.WALLS_CORNER_POS['South East'] + Vec3(-8,self.second_storey_level+2,-5),
							block.TORCH.withData(Torch.WEST)))
		builds.append(Torch(Castle.WALLS_CORNER_POS['South East'] + Vec3(-8,self.second_storey_level+2,-10),
							block.TORCH.withData(Torch.WEST)))
		builds.append(Torch(Castle.WALLS_CORNER_POS['South East'] + Vec3(-8,self.second_storey_level+2,-15),
							block.TORCH.withData(Torch.WEST)))

		# West room torches
		builds.append(Torch(Castle.WALLS_CORNER_POS['South East'] + Vec3(-19,self.second_storey_level+2,-5),
							block.TORCH.withData(Torch.EAST)))
		builds.append(Torch(Castle.WALLS_CORNER_POS['South East'] + Vec3(-19,self.second_storey_level+2,-10),
							block.TORCH.withData(Torch.EAST)))
		builds.append(Torch(Castle.WALLS_CORNER_POS['South East'] + Vec3(-19,self.second_storey_level+2,-15),
							block.TORCH.withData(Torch.EAST)))

		# south room door torches
		builds.append(Torch(Castle.WALLS_CORNER_POS['South East'] + Vec3(-11,self.second_storey_level+2,-8),
							block.TORCH.withData(Torch.NORTH)))
		builds.append(Torch(Castle.WALLS_CORNER_POS['South East'] + Vec3(-16,self.second_storey_level+2,-8),
							block.TORCH.withData(Torch.NORTH)))

		# torches on south turret access corridors
		builds.append(Torch(Castle.WALLS_CORNER_POS['South East'] + Vec3(-9,self.second_storey_level+2,-2),
							block.TORCH.withData(Torch.EAST)))
		builds.append(Torch(Castle.WALLS_CORNER_POS['South East'] + Vec3(-18,self.second_storey_level+2,-2),
							block.TORCH.withData(Torch.WEST)))
		# torches by south turret access points
		builds.append(Torch(Castle.WALLS_CORNER_POS['South East'] + Vec3(-4,self.second_storey_level+2,-2),
							block.TORCH.withData(Torch.WEST)))
		builds.append(Torch(Castle.WALLS_CORNER_POS['South East'] + Vec3(-23,self.second_storey_level+2,-2),
							block.TORCH.withData(Torch.EAST)))

		self._add_section("Second storey torches", builds)

		# North east corridor windows
		builds.append(BuildingBlock(Castle.WALLS_CORNER_POS['South East'] + Vec3(0,self.second_storey_level+1,-25),
									block.GLASS_PANE, 
									Castle.WALLS_CORNER_POS['South East'] + Vec3(0,self.second_storey_level+2,-25),
									description="window"))
		builds.append(BuildingBlock(Castle.WALLS_CORNER_POS['South East'] + Vec3(0,self.second_storey_level+1,-22),
									block.GLASS_PANE, 
									Castle.WALLS_CORNER_POS['South East'] + Vec3(0,self.second_storey_level+2,-22),
									description="window"))
		builds.append(BuildingBlock(Castle.WALLS_CORNER_POS['South East'] + Vec3(0,self.second_storey_level+1,-19),
									block.GLASS_PANE, 
									Castle.WALLS_CORNER_POS['South East'] + Vec3(0,self.second_storey_level+2,-19),
									description="window"))

		# North west corridor windows
		builds.append(BuildingBlock(Castle.WALLS_CORNER_POS['South East'] + Vec3(-27,self.second_storey_level+1,-25),
									block.GLASS_PANE, 
									Castle.WALLS_CORNER_POS['South East'] + Vec3(-27,self.second_storey_level+2,-25),
									description="window"))
		builds.append(BuildingBlock(Castle.WALLS_CORNER_POS['South East'] + Vec3(-27,self.second_storey_level+1,-22),
									block.GLASS_PANE, 
									Castle.WALLS_CORNER_POS['South East'] + Vec3(-27,self.second_storey_level+2,-22),
									description="window"))
		builds.append(BuildingBlock(Castle.WALLS_CORNER_POS['South East'] + Vec3(-27,self.second_storey_level+1,-19),
									block.GLASS_PANE, 
									Castle.WALLS_CORNER_POS['South East'] + Vec3(-27,self.second_storey_level+2,-19),
									description="window"))

		# south east corridor windows
		builds.append(BuildingBlock(Castle.WALLS_CORNER_POS['South East'] + Vec3(-5,self.second_storey_level+1,0),
									block.GLASS_PANE, 
									Castle.WALLS_CORNER_POS['South East'] + Vec3(-5,self.second_storey_level+2,0),
									description="window"))
		builds.append(BuildingBlock(Castle.WALLS_CORNER_POS['South East'] + Vec3(-8,self.second_storey_level+1,0),
									block.GLASS_PANE, 
									Castle.WALLS_CORNER_POS['South East'] + Vec3(-8,self.second_storey_level+2,0),
									description="window"))

		# south west corridor windows
		builds.append(BuildingBlock(Castle.WALLS_CORNER_POS['South East'] + Vec3(-19,self.second_storey_level+1,0),
									block.GLASS_PANE, 
									Castle.WALLS_CORNER_POS['South East'] + Vec3(-19,self.second_storey_level+2,0),
									description="window"))
		builds.append(BuildingBlock(Castle.WALLS_CORNER_POS['South East'] + Vec3(-22,self.second_storey_level+1,0),
									block.GLASS_PANE, 
									Castle.WALLS_CORNER_POS['South East'] + Vec3(-22,self.second_storey_level+2,0),
									description="window"))

		self._add_section("Second storey windows", builds)

	def _create_second_floor(self):
		# first story
		# - master bedroom
		#      - 2 beds surrounded by fence posts with pressure plates & carpet on top for 4 poster
		#      - chest at end of bed
		#           => 4x4 area for bed + 2 minimum all round
		#      - fireplace
		# - store room (non food)
		#      - Sell-able stuff (near door, beside armory)
		#           - wheat, potato, carrots
		#           - string, coal, wool, 
		#           - paper, books
		#           - rotten meat
		#           - raw pork, raw chicken
		#           - leather.
		#      - building material
		# - crafting room, close to store
		# - smelting room -  will need to be 6 high
		# - brewery
		# - dye room
		# 2nd floor plan:
		#   ssssssggssggssssggssggssssss 9
		#   s twb    T  ffff  T    bwt s 8 
		#   s  wb       ffff       bw  s 7 side walls lined with book shelves
		#   swdwb    c  ffff  c    bwdws 6 c  => chair
		#   g twb                  bwt g 5
		#   s  wT       fccf       Tw  s 4  fences posts 3 high around bed, wood slabs on top?
		#   s  wt        bb        cw  s 3  t=> table, c=> chair
		#   g  wtc       bb        cw  g 2	desk & chairs one side, sofa on the other?
		#   s  wt    T  f  f  T     w  s 1
		#   s  wwwwwwddwwwwwwddwwwwww  s 02 TODO: move doors
		#   g          t    t          g 9
		#   s t                      t s 8
		#   swwwwwww            wwwwwwws 7
		#   g      +   ffffff   +      g 6 + => supporting post based on stone wall below
		#   s      wt  xxwwxx  tw      s 5
		#   g      w   xxwwxx   w      g 4
		#   g storew  f      f  w brew g 3
		#   s      d  f      f  d      s 2 
		#   g      d  f      f  d      g 1
		#   swwwwwwwt ffffffff twwwwwwws 01
		#   g      d            d      g 9
		#   s      d   t    t   d      s 8
		#   g      +  wwwddwww  +      g 7 + => supporting post based on stone wall below
		#   g smeltw  w      w  w dye  g 6
		#   s      wt w      w tw      s 5
		#   g      w  w craftw  w      g 4
		#   swwwwwww  w      w  wwwwwwws 3 - posts on corners here would be over door arches below
		#   st d     tw      wt     d ts 2 
		#   s  wt     w      w     tw  s 1
		#   sssssgssgssgsggsgssgssgsssss 0

		#   7654321098765432109876543210
		#          2         1          
		self._create_second_floor_skeleton()
		self._create_second_floor_rooms()
		builds = []
		builds.append(SubBuilding(Roof(Building.NORTH), 
								  Castle.WALLS_CORNER_POS['South East'] + Vec3(0,self.ceiling_level,0)))
		self._add_section("Roof", builds)

		# smelting room need to be added after roof to take some space from ceiling & floor to accomodate hopper fed furnaces
		builds.append(SubBuilding(SmeltingRoom(Building.WEST), 
								  Castle.WALLS_CORNER_POS['South East'] + Vec3(-20,self.second_storey_level,-10)))
		self._add_section("Smelting Room", builds)

		self._create_second_floor_turrets()
		self._create_second_floor_fittings()

	###########################################################################
	# roof structure
	def _create_roof_turrets(self):
		# TODO: add another level of turrets with access to roof
		# add turret tops with battlements
		pass

	def _create_roof_battlements(self):
		# TODO: add surrounding battlements on roof (overhang & fences?)
		pass

	###########################################################################
	# basement structure
	def _create_basement(self):
		# TODO: create stairs to basement
		# basement
		#	target practice room
		#	corridor
		#	mushroom farm
		#	portal room
		#	mine access
		#	mobtrap access
		pass

	###########################################################################
	# Whole building structure
	def _create_structure(self):
		super(Castle, self)._create_structure()
		self._create_ground_floor()
		self._create_second_floor()
		self._create_roof_turrets()
		self._create_roof_battlements()
		self._create_basement()



class CastleEnclosure(BuildingEx):
	 #* well(s)

	 #* crop farm x4 - 2 wheat, 1 potato 1 carrot
	 #     - make plot sizes 8x7, with 7x dispensers - will need to work on surrounding automation for this.
	 #          - but could put the dispensers on the bottom easing automation
	 #          - could use redstone torches underneath dispensers & lever with power on normally
	 #     - this will run to 8x19 x 2
	 #* sugar cane farm x2 (10x9 for 1 plot)
	 #* pumpkin/melon farm - need to investigate designs.
	 #     http://minecraft.gamepedia.com/Tutorials/Pumpkin_and_melon_farming
	 #     check out semi automatic stackable design #7
	 #* mushroom farm - can go under other farms. (20x25 working well - although some mobs spawn inside)

	 #* Animal pens (make fences 2 high with double gates in 1 corner (animals are escaping from stiles in current designs)
	 #     - pens sizes (current = 9x8, maybe go to 10x10)
	 #     - cows, sheep, pigs, chickens
	 #     - could use leads to keep animals in pens.
	 #     - probably want a paddock area for horses too (horses can walk through non solid blocks so maybe just a stables)
	 #* stables - need to work on designs
	 #     - individual stalls & hay inside?
	 #     https://www.pinterest.com/mustanglani/minecraft-barns/
	 #     https://www.google.ie/search?q=minecraft+stable+blueprint&sa=X&biw=1920&bih=958&tbm=isch&tbo=u&source=univ&ei=M9g0Vd3UIoLW7AbXsYHQDA&ved=0CCAQsAQ
	 #     http://www.minecraftforum.net/forums/show-your-creation/screenshots/1588012-howto-build-a-barn (17x17 design, might no need such a high roof (try half slab steps for roof)
	 #* kennels - need to work on designs.
	 #     - think i read a dog bed design - 2 half slabs, with carpet on top & surrounded by signs.
	 #     http://mp3loot.ninja/index.php?q=20+wolf+dog+house+kennel+ideas+and+designs+minecraft&type=video&view=696d525161544e53795838

	 #* pond?

	pass
