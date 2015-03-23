from mcpi import minecraft
from mcpi.vec3 import Vec3
import time

def find_north(mc):
	pl = mc.player
	ps = pl.getTilePos()
	nps = ps + Vec3(0,0,1)

	mc.postToChat("Moving North")
	pl.setPos(nps)
	time.sleep(0.5)
	pl.setPos(ps)
	time.sleep(1)
	
	mc.postToChat("Moving North")
	pl.setPos(nps)
	time.sleep(0.5)
	pl.setPos(ps)
	time.sleep(1)
	