import mcpi.minecraft as minecraft
from mcpi.block import *

mc = minecraft.Minecraft.create()
pl = mc.player
cm = mc.camera

def find_at(x, z, type):
	''' search down from getHeight for block type, break on leaves, dirt or stone.'''
	y = mc.getHeight(x, z)
	while True:
		y -= 1
		data = mc.getBlockWithData(x, y, z)

		if (data.id == STONE.id 
			or data.id == DIRT.id 
			or data.id == GRASS.id 
			or data.id == LEAVES.id):
			return False
		elif data.id == type.id:
			return True 



	