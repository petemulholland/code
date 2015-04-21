from village.debug.debug_utils import mc, pl, cm
from village import *
from mcpi.vec3 import Vec3
import os

def cls():
	os.system('CLS')

def get_direction():
	direction = mc.player.getDirection()
	if (abs(direction.x) > abs(direction.z)): # x value is treater = > east-west
		if direction.x >= 0:
			return Building.EAST
		else: 
			return Building.WEST
	else:
		if direction.z >= 0:
			return Building.SOUTH
		else:
			return Building.NORTH

def process_hit(blockEvent):
	# TODO get pos from blockEvent - check real mcpi api
	pos = Vec3(0,0,0)
	direction = get_direction()
	display_menu_l1(pos)

# TODO P3OOP, ch2 case study (loc 1217) has a single level menu class implementation
#             the way i'm implementing this is a bit tedious, look into P3OOP
# gonna want 
# 1. get building type, 
#	- small houses version?
#	- farm version small/large?
#	- street multiplier
# 2. build orientation, currently facing X, build in that direction?
# 3. build to left or right of hit pos


class Menu(object):

	def __init__(self):
		self.pos = None
		self.direction = None

	def cls(self):
		os.system('CLS')

	def display_hit_menu(self):
		self.cls()
		print "Block hit at: %s"%(str(self.pos))
		ret = raw_input("do you want to build here y/n: [y]")
		if len(ret) == 0:
			ret = 'y'

		return ret.lower()

	def get_building_type(self):
		self.cls()
		while True:
			print "Are you building infrastructure or dwellings:"
			print "\t1  Infrastructure"
			print "\t2  Dwellings"
			print "\tQ  Abandon build"
			
			ret = self.get_input("Enter building type: [q]")
			if ret == 'q' or len(ret) == 0:
				return None
			elif ret == '1':
				return get_infrastructure_type()
			elif ret == '2':
				return get_dwelling_type()
			else:
				self.cls()
				print "%s is not a vaild choice"%(ret)
				print
			
	def get_infrastructure_type(self):
		self.cls()
		while True:
			pass
		pass

#SmallHouseV1 
#SmallHouseV2
#SmallHouseV3
#LargeHouse
#ApartmentBlock

#LampPost
#Well
#Street
#Farm
#LargeFarm
#Library
#Church
#Butcher
#Blacksmith

	def get_dwelling_type(self):
		self.cls()
		pass

	def get_small_house_type(self):
		self.cls()
		pass

	def get_farm_type(self):
		self.cls()
		pass

	def get_input(self, prompt):
		return raw_input(prompt).lower()

	def run(self, pos, direction):
		self.pos = pos
		self.direction = direction
		ret = self.display_hit_menu()
		
		if ret == 'y':
			display_building_menu()


if __name__ == "__main__":
	mc.events.clearAll()
	menu = Menu()
	while True:
		blockEvents = mc.events.pollBlockHits()
		for blockEvent in blockEvents:
			menu.run(Vec3(0,0,0), get_direction())