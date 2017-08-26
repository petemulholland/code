from mcpi import minecraft
from mcpi.vec3 import Vec3
from mcpi import block
import time

def get_block_data(mc, pos, xrange, yrange, zrange):
	print "        ",
	for z in range(-(zrange - 1), zrange + 1):
		print "     %d"%(z + pos.z), 
	print
	
	for x in range(-(xrange - 1), xrange + 1):
		for y in range(yrange, -1, -1):
			print "%d - %d"%(pos.x + x, pos.y + y), 
			for z in range(-(zrange - 1), zrange + 1):
				print str(mc.getBlockWithData(pos.x + x, pos.y + y, pos.z + z)),
	
			print
			
def draw_north(mc, pos, block_type):
	arrow_long = (pos + Vec3(0,1,0), pos + Vec3(0,6,0))
	arrow_x1 = (pos + Vec3(-1,5,0), pos + Vec3(1,5,0))
	arrow_x2 = (pos + Vec3(-2,4,0), pos + Vec3(2,4,0))
	
	mc.setBlocks(arrow_long[0], arrow_long[1], block_type)
	mc.setBlocks(arrow_x1[0], arrow_x1[1], block_type)
	mc.setBlocks(arrow_x2[0], arrow_x2[1], block_type)

	n_extent = (pos + Vec3(4,1,0), pos + Vec3(8,6,0))

	n_blanks = [(pos + Vec3(5,1,0), pos + Vec3(5,4,0)), 
				(pos + Vec3(6,1,0), pos + Vec3(6,2,0)),
				(pos + Vec3(6,5,0), pos + Vec3(6,6,0)),
				(pos + Vec3(7,3,0), pos + Vec3(7,6,0))]
	mc.setBlocks(n_extent[0], n_extent[1], block_type)

	for coords in n_blanks:
		mc.setBlocks(coords[0], coords[1], block.AIR)

def embed_north(mc, pos, block_type):
	""" embed north facing arrow in ground at player pos """
	arrow_long = (pos + Vec3(0,-1,-1), pos + Vec3(0,-1,-6))
	arrow_x1 = (pos + Vec3(-1,-1,-5), pos + Vec3(1,-1,-5))
	arrow_x2 = (pos + Vec3(-2,-1,-4), pos + Vec3(2,-1,-4))
	
	mc.setBlocks(arrow_long[0], arrow_long[1], block_type)
	mc.setBlocks(arrow_x1[0], arrow_x1[1], block_type)
	mc.setBlocks(arrow_x2[0], arrow_x2[1], block_type)

def find_north(mc=None):
	if mc is None:
		mc = minecraft.Minecraft.create()

	pl = mc.player
	ps = pl.getTilePos()
	nps = ps + Vec3(0,0,-1)

	draw_north(mc, nps, block.OBSIDIAN)
	time.sleep(2)
	draw_north(mc, nps, block.AIR)

def move_to_origin(mc):
	y = mc.getHeight(0,0)
	mc.player.setTilePos(0,y,0)


TEST_EXTENT = 60
CLEAR_HEIGHT = 16
def setup_test_area(mc=None):
	if mc is None:
		mc = minecraft.Minecraft.create()

	pl = mc.player
	ps = pl.getTilePos()
	sw = ps + Vec3(-TEST_EXTENT, 0, TEST_EXTENT)
	ne = ps + Vec3(TEST_EXTENT, 0, -TEST_EXTENT)
	
	# from bottom up set 2 layers of stone & 2 layers of dirt
	mc.setBlocks(sw + Vec3(0,-8,0), ne + Vec3(0,-3,0), block.STONE)
	mc.setBlocks(sw + Vec3(0,-2,0), ne + Vec3(0,-2,0), block.DIRT)
	mc.setBlocks(sw + Vec3(0,-1,0), ne + Vec3(0,-1,0), block.GRASS)

	# clear air down from level 3
	mc.setBlocks(sw + Vec3(0,0,0), ne + Vec3(0,16,0), block.AIR)

	for i in range(1, (TEST_EXTENT/10)+1, 1):
		mc.setBlock(ps + Vec3(i*10,0,0), block.TORCH.withData(5))
		mc.setBlock(ps + Vec3(i*10,0,i*10), block.TORCH.withData(5))
		mc.setBlock(ps + Vec3(0,0,i*10), block.TORCH.withData(5))
		mc.setBlock(ps + Vec3(i*-10,0,i*10), block.TORCH.withData(5))
		mc.setBlock(ps + Vec3(i*-10,0,0), block.TORCH.withData(5))
		mc.setBlock(ps + Vec3(i*-10,0,i*-10), block.TORCH.withData(5))
		mc.setBlock(ps + Vec3(0,0,i*-10), block.TORCH.withData(5))
		mc.setBlock(ps + Vec3(i*10,0,i*-10), block.TORCH.withData(5))


	embed_north(mc, ps, block.OBSIDIAN)