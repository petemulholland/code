from mcpi import minecraft
from mcpi.vec3 import Vec3
from mcpi import block
import time

def find_north(mc=None):
	if mc is None:
		mc = minecraft.Minecraft.create()

	pl = mc.player
	ps = pl.getTilePos()
	nps = ps + Vec3(0,0,1)

	# TODO update this to draw arrow of Block with big N over it
	# then set camera pos? (without direction, this isn't much good?)
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
	

def setup_test_area(mc=None):
	if mc is None:
		mc = minecraft.Minecraft.create()

	pl = mc.player
	ps = pl.getTilePos()
	sw = ps + Vec3(-20, 0, -20)
	ne = ps + Vec3(20, 0, 20)
	
	# from bottom up set 2 layers of stone & 2 layers of dirt
	mc.setBlocks(sw.x, sw.y - 4, sw.z,
			ne.x, ne.y - 4, ne.z, block.STONE)
	mc.setBlocks(sw.x, sw.y - 3, sw.z,
			ne.x, ne.y - 3, ne.z, block.STONE)
	mc.setBlocks(sw.x, sw.y - 2, sw.z,
			ne.x, ne.y - 2, ne.z, block.DIRT)
	mc.setBlocks(sw.x, sw.y - 1, sw.z,
			ne.x, ne.y - 1, ne.z, block.DIRT)

	# clear air down from level 3
	mc.setBlocks(sw.x, sw.y + 3, sw.z,
			ne.x, ne.y + 3, ne.z, block.AIR)
	mc.setBlocks(sw.x, sw.y + 2, sw.z,
			ne.x, ne.y + 2, ne.z, block.AIR)
	mc.setBlocks(sw.x, sw.y + 1, sw.z,
			ne.x, ne.y + 1, ne.z, block.AIR)
	mc.setBlocks(sw.x, sw.y, sw.z,
			ne.x, ne.y, ne.z, block.AIR)

	