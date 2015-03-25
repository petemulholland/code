from mcpi import minecraft
from mcpi.vec3 import Vec3
from mcpi import block
import time

def draw_north(mc, pos, block_type):
	arrow_long = (nps + Vec3(0,1,1), nps + Vec3(0,1,6))
	arrow_short = (nps + Vec3(-1,1,5), nps + Vec3(1,1,5))
	
	# TODO: is there an easy way to extract x,y,z from Vec3?
	mc.setBlocks(arrow_long[0].x, arrow_long[0].y, arrow_long[0].z,
			     arrow_long[1].x, arrow_long[1].y, arrow_long[1].z, block_type)
	mc.setBlocks(arrow_short[0].x, arrow_short[0].y, arrow_short[0].z,
			     arrow_short[1].x, arrow_short[1].y, arrow_short[1].z, block_type)

	n_extent = (nps + Vec3(-1,3,6), nps + Vec3(-1,5,6))
	n_blanks = [(nps + Vec3(0,3,6), nps + Vec3(0,4,6)), 
			    (nps + Vec3(0,6,6), nps + Vec3(0,7,6)),
				(nps + Vec3(1,5,6), nps + Vec3(1,7,6))]
	mc.setBlocks(n_extent[0].x, n_extent[0].y, n_extent[0].z,
			     n_extent[1].x, n_extent[1].y, n_extent[1].z, block_type)

	for coords in n_blanks:
		mc.setBlocks(coords[0].x, coords[0].y, coords[0].z,
					 coords[1].x, coords[1].y, coords[1].z, block.AIR)


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

	draw_north(mc, ps + Vec3(0,0,15), block.OBSIDIAN)