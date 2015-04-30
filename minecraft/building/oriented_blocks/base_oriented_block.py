from building import BuildingBlock
import mcpi.block as block
from mcpi.block import Block

# NOTE: oriented block data appears to always indicate the direction the item is "facing"
class OrientedBlock(BuildingBlock):
	def __init__(self, compass_points, *args, **kwargs):
		super(OrientedBlock, self).__init__(*args, **kwargs)
		self.compass_points = compass_points

		self.left_rotation = { self.compass_points['EAST']: self.compass_points['NORTH'], 
							   self.compass_points['SOUTH'] : self.compass_points['EAST'],
							   self.compass_points['WEST'] : self.compass_points['SOUTH'],
							   self.compass_points['NORTH'] : self.compass_points['WEST']
							 }
		self.right_rotation = { self.compass_points['EAST']: self.compass_points['SOUTH'], 
							    self.compass_points['SOUTH'] : self.compass_points['WEST'],
							    self.compass_points['WEST'] : self.compass_points['NORTH'],
							    self.compass_points['NORTH'] : self.compass_points['EAST']
							  }

	
	def rotateLeft(self):  
		super(OrientedBlock, self).rotateLeft()
		
		if self.block.data not in self.left_rotation:
			print "Invalid data on block: ({0})".format(str(self.block))
		else:
			self.block.data = self.left_rotation[self.block.data]
	
	def rotateRight(self, ct=1): 
		for i in range(ct):	
			super(OrientedBlock, self).rotateRight()
			if self.block.data not in self.right_rotation:
				print "Invalid data on block: ({0})".format(str(self.block))
			else:
				self.block.data = self.right_rotation[self.block.data]

