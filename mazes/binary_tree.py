from cell import Cell
from grid import Grid
import random

class BinaryTree:
	def __init__(self):
		random.seed()

	def on (self, grid):
		for cell in grid.each_cell():
			neighbors = []
			if cell.north:
				neighbors.append(cell.north)
			if cell.east:
				neighbors.append(cell.east)

			neighbor = random.choice(neighbors)
		
			if neighbor:
				cell.link(neighbor)

	
