from mcpi import minecraft
from mcpi.vec3 import Vec3
from mcpi import block
import time

def draw_north(mc, pos, block_type):
	arrow_long = (pos + Vec3(0,1,1), pos + Vec3(0,1,6))
	arrow_short = (pos + Vec3(-1,1,5), pos + Vec3(1,1,5))
	
	mc.setBlocks(arrow_long[0], arrow_long[1], block_type)
	mc.setBlocks(arrow_short[0], arrow_short[1], block_type)

	n_extent = (pos + Vec3(-1,3,6), pos + Vec3(-1,5,6))
	n_blanks = [(pos + Vec3(0,3,6), pos + Vec3(0,4,6)), 
				(pos + Vec3(0,6,6), pos + Vec3(0,7,6)),
				(pos + Vec3(1,5,6), pos + Vec3(1,7,6))]
	mc.setBlocks(n_extent[0], n_extent[1], block_type)

	for coords in n_blanks:
		mc.setBlocks(coords[0], coords[1], block.AIR)


def find_north(mc=None):
	if mc is None:
		mc = minecraft.Minecraft.create()

	pl = mc.player
	ps = pl.getTilePos()
	nps = ps + Vec3(0,0,1)

	draw_north(mc, nps, block.OBSIDIAN)
	time.sleep(2)
	draw_north(mc, nps, block.AIR)

	

def setup_test_area(mc=None):
	if mc is None:
		mc = minecraft.Minecraft.create()

	pl = mc.player
	ps = pl.getTilePos()
	sw = ps + Vec3(-20, 0, -20)
	ne = ps + Vec3(20, 0, 20)
	
	# from bottom up set 2 layers of stone & 2 layers of dirt
	mc.setBlocks(sw + Vec3(0,-4,0), ne + Vec3(0,-4,0), block.STONE)
	mc.setBlocks(sw + Vec3(0,-3,0), ne + Vec3(0,-3,0), block.STONE)
	mc.setBlocks(sw + Vec3(0,-2,0), ne + Vec3(0,-2,0), block.DIRT)
	mc.setBlocks(sw + Vec3(0,-1,0), ne + Vec3(0,-1,0), block.DIRT)

	# clear air down from level 3
	for i in xrange(3, 0, -1):
		mc.setBlocks(sw + Vec3(0,i,0), ne + Vec3(0,i,0), block.AIR)

	draw_north(mc, ps + Vec3(0,0,15), block.OBSIDIAN)