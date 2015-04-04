from village.tests import *
from village.building import SLEEP_SECS
from village.building import Building
from village.utils import setup_test_area
from village.oriented_blocks import *

import mcpi.minecraft as minecraft

from mcpi import block
from mcpi.vec3 import Vec3
import time

mc = minecraft.Minecraft.create()
pl = mc.player
cm = mc.camera

def debug_doors():
	ps = mc.player.getTilePos()

	doors = { 'NR' : Door(Door.HINGE_RIGHT, Vec3(0,0,0), block.DOOR_WOOD.withData(Door.NORTH)),
				'NL' : Door(Door.HINGE_LEFT, Vec3(0,0,0), block.DOOR_WOOD.withData(Door.NORTH)),

				'ER' : Door(Door.HINGE_RIGHT, Vec3(0,0,0), block.DOOR_WOOD.withData(Door.EAST)),
				'EL' : Door(Door.HINGE_LEFT, Vec3(0,0,0), block.DOOR_WOOD.withData(Door.EAST)),

				'SR' : Door(Door.HINGE_RIGHT, Vec3(0,0,0), block.DOOR_WOOD.withData(Door.SOUTH)),
				'SL' : Door(Door.HINGE_LEFT, Vec3(0,0,0), block.DOOR_WOOD.withData(Door.SOUTH)),

				'WR' : Door(Door.HINGE_RIGHT, Vec3(0,0,0), block.DOOR_WOOD.withData(Door.WEST)),
				'WL' : Door(Door.HINGE_LEFT, Vec3(0,0,0), block.DOOR_WOOD.withData(Door.WEST)) 
			}

	time.sleep(4)

	mc.setBlock(Vec3(ps.x -1, ps.y, ps.z -4), block.COBBLESTONE)
	mc.setBlock(Vec3(ps.x -1, ps.y +1, ps.z -4), block.COBBLESTONE)

	mc.setBlock(Vec3(ps.x +2, ps.y, ps.z -4), block.COBBLESTONE)
	mc.setBlock(Vec3(ps.x +2, ps.y +1, ps.z -4), block.COBBLESTONE)

	doors['NR'].build_at(mc, Vec3(ps.x, ps.y, ps.z -4))
	doors['NL'].build_at(mc, Vec3(ps.x +1, ps.y, ps.z -4))
	
	mc.setBlock(Vec3(ps.x -1, ps.y, ps.z -2), block.COBBLESTONE)
	mc.setBlock(Vec3(ps.x -1, ps.y +1, ps.z -2), block.COBBLESTONE)

	mc.setBlock(Vec3(ps.x +2, ps.y, ps.z -2), block.COBBLESTONE)
	mc.setBlock(Vec3(ps.x +2, ps.y +1, ps.z -2), block.COBBLESTONE)

	doors['SL'].build_at(mc, Vec3(ps.x, ps.y, ps.z -2))
	doors['SR'].build_at(mc, Vec3(ps.x +1, ps.y, ps.z -2))
	
def display_doors():
	ps = mc.player.getTilePos()

	#print "DBG: player pos: " + str(ps)
	
	print "z:  y x",
	for x in range(-3, 5, 1):
		print "      %03d"%(ps.x + x),
	
	print ""
	#print "DBG: x header printed, printing z & y data"
	
	for z in range(-8, 0, 1):
		#print "DBG: in z loop z:%d"%(z)
		for y in range(1, -1, -1):
			#print "DBG: in y loop y:%d"%(y)
			print "%03d - %d "%(ps.z + z, ps.y + y),
			for x in range(-3, 5, 1):
				#print "DBG: in x loop x:%d"%(x)
				print "  " + str(mc.getBlockWithData(ps.x + x, ps.y + y, ps.z + z)),
			
			print ""	

def set_doors():
	ps = mc.player.getTilePos()

	doors = { 'NR' : Door(Door.HINGE_RIGHT, Vec3(0,0,0), block.DOOR_WOOD.withData(Door.NORTH)),
				'NL' : Door(Door.HINGE_LEFT, Vec3(0,0,0), block.DOOR_WOOD.withData(Door.NORTH)),

				'ER' : Door(Door.HINGE_RIGHT, Vec3(0,0,0), block.DOOR_WOOD.withData(Door.EAST)),
				'EL' : Door(Door.HINGE_LEFT, Vec3(0,0,0), block.DOOR_WOOD.withData(Door.EAST)),

				'SR' : Door(Door.HINGE_RIGHT, Vec3(0,0,0), block.DOOR_WOOD.withData(Door.SOUTH)),
				'SL' : Door(Door.HINGE_LEFT, Vec3(0,0,0), block.DOOR_WOOD.withData(Door.SOUTH)),

				'WR' : Door(Door.HINGE_RIGHT, Vec3(0,0,0), block.DOOR_WOOD.withData(Door.WEST)),
				'WL' : Door(Door.HINGE_LEFT, Vec3(0,0,0), block.DOOR_WOOD.withData(Door.WEST)) 
			}


	doors['NR'].build_at(mc, Vec3(ps.x, ps.y, ps.z -8))
	doors['NL'].build_at(mc, Vec3(ps.x +1, ps.y, ps.z -8))
	
	doors['SR'].build_at(mc, Vec3(ps.x +1, ps.y, ps.z -1))
	doors['SL'].build_at(mc, Vec3(ps.x, ps.y, ps.z -1))


	doors['WR'].build_at(mc, Vec3(ps.x -3, ps.y, ps.z -4))
	doors['WL'].build_at(mc, Vec3(ps.x -3, ps.y, ps.z -5))
	
	doors['ER'].build_at(mc, Vec3(ps.x +4, ps.y, ps.z -5))
	doors['EL'].build_at(mc, Vec3(ps.x +4, ps.y, ps.z -4))


if __name__ == "__main__":
	debug_doors()

	time.sleep(5)

	display_doors()
