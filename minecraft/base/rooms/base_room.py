from building import Building, BuildingEx, BuildingBlock, Torch
from base.fixtures import OpenDoorway
from base.constants import WALL_HEIGHT, EXTERIOR_WALLS
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

class RoomBase(BuildingEx):
	''' basic 6x6 (internal) room to base other castle rooms off '''
	WALLS_CORNER_POS = {'South East' : Building.SE_CORNER_POS + Vec3(0,0,0), 
						'South West' : Building.SE_CORNER_POS + Vec3(-7,0,0),
						'North West' : Building.SE_CORNER_POS + Vec3(-7,0,-7),
						'North East' : Building.SE_CORNER_POS + Vec3(0,0,-7) }

	WIDTH = WALLS_CORNER_POS['South East'].x - (WALLS_CORNER_POS['South West'].x - 1)
	#TODO: figure out how to specify block type for each wall
	def __init__(self, *args, **kwargs):
		''' derived classes must call _set_orientation '''
		super(RoomBase, self).__init__(width=RoomBase.WIDTH, *args, **kwargs)

		# create walls
		builds = []
		builds.append(BuildingBlock(RoomBase.WALLS_CORNER_POS['South East'],
									EXTERIOR_WALLS, 
									RoomBase.WALLS_CORNER_POS['South West'] + Vec3(0,WALL_HEIGHT,0),
									description="South wall"))
		builds.append(BuildingBlock(RoomBase.WALLS_CORNER_POS['South West'],
									EXTERIOR_WALLS, 
									RoomBase.WALLS_CORNER_POS['North West'] + Vec3(0,WALL_HEIGHT,0),
									description="West wall"))
		builds.append(BuildingBlock(RoomBase.WALLS_CORNER_POS['North East'],
									EXTERIOR_WALLS, 
									RoomBase.WALLS_CORNER_POS['North West'] + Vec3(0,WALL_HEIGHT,0),
									description="North wall"))
		builds.append(BuildingBlock(RoomBase.WALLS_CORNER_POS['South East'],
									EXTERIOR_WALLS, 
									RoomBase.WALLS_CORNER_POS['North East'] + Vec3(0,WALL_HEIGHT,0),
									description="East wall"))

		self._add_section("Base room walls", builds)

		#self._set_orientation()
