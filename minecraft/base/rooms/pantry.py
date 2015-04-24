from building import Building, BuildingEx, BuildingBlock, SubBuilding, Torch, Chest
from base_room import RoomBase
from base.fixtures import OpenDoorway
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

class Pantry(RoomBase):
	# TODO: implement 
	# - pantry (chests for raw & cooked food)

	"""description of class"""
	def __init__(self, *args, **kwargs):
		super(Pantry, self).__init__(*args, **kwargs)

		builds = []
		builds.append(SubBuilding(OpenDoorway(Building.NORTH), Building.SE_CORNER_POS + Vec3(-3,0,0)))
		builds.append(SubBuilding(OpenDoorway(Building.EAST), RoomBase.WALLS_CORNER_POS['South East'] + Vec3(0,0,-2)))

		self._add_section("Doorways", builds)
		# TODO: add chests

		self._set_orientation()
		


