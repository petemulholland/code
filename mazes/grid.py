from .cell import Cell
import random

class Grid:
	def __init__(self, rows, columns):
		self._rows = rows
		self._columns = columns
		self._grid = self._prepare_grid()
		self._configure_cells()
		
	def _prepare_grid(self):
		return [[Cell(r, c) for c in range(self.columns)] for r in range(self.rows)] 
		
	def _configure_cells(self):
		# for row in self._grid:
		#	for cell in row:
		for row in range(self.rows):
			for col in range(self.columns):
				cell = self._grid[row][col]
				cell.north = self._get_cell(row - 1, col)
				cell.south = self._get_cell(row + 1, col)
				cell.west = self._get_cell(row, col - 1)
				cell.east = self._get_cell(row, col + 1)
				
	# TODO: figure out if this can be done with a custom accessor method?
	def _get_cell(self, row, col):
		if row < 0 or row >= self.rows:
			return None
		if col < 0 or col >= self.columns:
			return None
			
		return self._grid[row][col]
		
	@property 
	def rows(self): 
		'''Read-only rows attribute'''
		return self._rows
		
	@property 
	def columns(self): 
		'''Read-only columns attribute'''
		return self._columns
		
	
	def random_cell(self):
		random.seed() 
		row = random.randint(0, self.rows - 1) # random.randrange(self.rows - 1)?
		col = random.randint(0, self.columns - 1) # random.randrange(self.columns - 1)?
		return self._grid[row][col]
	
	def size(self):
		return self.rows * self.columns

	def each_row(self):
		for row in self._grid:
			yield row

	def each_cell(self):
		for row in self._grid:
			for cell in row:
				if cell:
					yield cell

	def __str__(self):
		'''Render the grid using ascii art'''
		output = "+" + ("---+" * self.columns) + "\n"
		for row in self.each_row():
			top = "|"
			bottom = "+"
			for cell in row:
				# "Displaying Maze on Terminal" loc 621 says:
				# Some cells may eventually be None, so handle that here
				if not cell:
				 	cell = Cell(-1, -1)
				
				body = "   "
				east_boundary = " " if cell.is_linked(cell.east) else "|"
				top += body + east_boundary
				
				south_boundary = "   " if cell.is_linked(cell.south) else "---"
				corner = "+"
				bottom += south_boundary + corner
				
			output += top + "\n"
			output += bottom + "\n"
		
		return output
