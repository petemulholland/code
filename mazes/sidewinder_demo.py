from mazes.grid import Grid
from mazes.sidewinder import Sidewinder

if __name__ == "__main__":
	grid = Grid(16, 16)
	#print(grid)
	sw = Sidewinder()
	grid = sw.on(grid)
	print(grid)
	
