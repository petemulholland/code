import mcpi.minecraft as minecraft
from mcpi import block
from mcpi.vec3 import Vec3

mc = minecraft.Minecraft.create()
pl = mc.player
cm = mc.camera


def debug_blocks(x1, y1, z1, x2, y2, z2):
	global mc
	ps = mc.player.getTilePos()

	xd = 1
	if x1 > x2:
		xd = -1
	print "DBG x: %d -> %d, delta: %d  \trange: %s"%(x1, x2, xd, range(x1, x2 + xd, xd))
	
	yd = 1
	if y1 > y2:
		yd = -1
	print "DBG y: %d -> %d, delta: %d  \trange: %s"%(y1, y2, yd, range(y1, y2 + yd, yd))

	zd = 1
	if z1 > z2:
		zd = -1
	print "DBG z: %d -> %d, delta: %d  \trange: %s"%(z1, z2, zd, range(z1, z2 + zd, zd))
	#print "DBG: player pos: " + str(ps)
	
	print "z:  y x",
	for x in range(x1, x2 + xd, xd):
		print "      %03d"%(ps.x + x),
	
	print ""
	#print "DBG: x header printed, printing z & y data"
	
	for z in range(z1, z2 + zd, zd):
		#print "DBG: in z loop z:%d"%(z)
		for y in range(y1, y2 + yd, yd):
			#print "DBG: in y loop y:%d"%(y)
			print "%03d - %d "%(ps.z + z, ps.y + y),
			for x in range(x1, x2 + xd, xd):
				#print "DBG: in x loop x:%d"%(x)
				print "  " + str(mc.getBlockWithData(ps.x + x, ps.y + y, ps.z + z)),
			
			print ""	
	
