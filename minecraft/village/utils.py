from mcpi import minecraft
from mcpi.vec3 import Vec3
from mcpi import block
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
	

def setup_test_area(mc):
	pl = mc.player
	ps = pl.getTilePos()
	sw = ps - Vec3(20, 0, 20)
	ne = ps + Vec3(20, 0, 20)
	
	mc.setBlocks(sw.x, sw.y + 1, sw.z,
			ne.x, ne.y + 1, ne.z, block.AIR)
	mc.setBlocks(sw.x, sw.y, sw.z,
			ne.x, ne.y, ne.z, block.DIRT)
	mc.setBlocks(sw.x, sw.y - 1, sw.z,
			ne.x, ne.y - 1, ne.z, block.DIRT)
	mc.setBlocks(sw.x, sw.y - 2, sw.z,
			ne.x, ne.y - 2, ne.z, block.DIRT)
	