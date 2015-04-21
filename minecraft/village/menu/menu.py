from village.debug.debug_utils import mc, pl, cm
from village.building import Building
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

def display_menu_l1(pos):
	cls()
	print "Block hit at: %s"%(pos)
	print "Do you want to build at this position?"

def process_hit(blockEvent):
	# TODO get pos from blockEvent - check real mcpi api
	pos = Vec3(0,0,0)
	direction = get_direction()
	display_menu_l1(pos)

# TODO implement menu as a class
class Menu(object):
	def __init__(self, pos, direction):
		self.pos = pos
		self.direction = direction

	def display_menu(self):
		pass

	def get_input(self):
		pass


if __name__ == "__main__":
	mc.events.clear()
	while True:
		blockEvents = mc.events.pollBlockHits()
		for blockEvent in blockEvents:
			pass