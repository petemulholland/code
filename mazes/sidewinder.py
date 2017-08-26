from .cell import Cell
from .grid import Grid
import random

class Sidewinder:
	def __init__(self):
		random.seed()
		
	def on (self, grid):
		for row in grid.each_row():
			run = []
			
			for cell in row:
				run.append(cell)
				
				at_east_boundary = cell.east == None
				at_north_boundary = cell.north == None
				
				should_close_out = (at_east_boundary or 
							((not at_north_boundary) and 
							random.randrange(2) == 0))
				if should_close_out:
					member = random.choice(run)
					if member.north:
						member.link(member.north)
						
					del run[:]
				else:
					cell.link(cell.east)
		
		return grid
