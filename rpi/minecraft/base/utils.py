import mcpi.minecraft as minecraft
from mcpi.block import *

mc = minecraft.Minecraft.create()
pl = mc.player
cm = mc.camera

abortive_block_ids = [STONE.id, DIRT.id, GRASS.id, GRAVEL.id, AIR.id, LEAVES.id]

def search_at(block_types, x, z, abort_blocks):
	''' search down from getHeight for block type, break on leaves, dirt or stone.'''
	print "Searching ({0},{1})".format(x,z)
	y = mc.getHeight(x, z)
	while True:
		id = mc.getBlock(x, y, z)

		if id in abortive_block_ids:
			return False
		elif data.id == type.id:
			return True 

		y -= 1
		

def search_chunk_for(block_type, x, z, search_func, end_search_blocks):
	for i in reversed(range(2,17,2)): # chunk size
		print "---------------"
		for zd in range(i-1):
			z += 1
			if search_func(block_type, x, z, end_search_blocks):
				return x,z

		for xd in range(i-1):
			x += 1
			if search_func(block_type, x, z, end_search_blocks):
				return x,z

		for zd in range(i-1):
			z -= 1
			if search_func(block_type, x, z, end_search_blocks):
				return x,z

		for xd in range(i-1):
			x -= 1
			if search_func(block_type, x, z, end_search_blocks):
				return x,z

		x += 1
		z += 1

	return None


if __name__ == "__main__":
	x, z = search_chunk_for(DOOR_WOOD, 0, 0, search_at)

	