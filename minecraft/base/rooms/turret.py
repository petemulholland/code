from building import Building, BuildingEx, BuildingBlock, SubBuilding, Torch, Furnace, Chest, Door
from base_room import RoomBase
from building.types import CAULDRON
from base.fixtures import OpenDoorway
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

class Turret(BuildingEx):
	# TODO: implement 
  #    X
  #    X
  #   XXwww
  #  Xss  d
  # X ss  w
  # XssX  XXXX
  # Xssss X
  #  X ssX
  #   XXX   

	WIDTH = 7
	def __init__(self, *args, **kwargs):
		super(Turret, self).__init__(width=Turret.WIDTH, *args, **kwargs)

	def _create_structure(self):
		super(Turret, self)._create_structure()

