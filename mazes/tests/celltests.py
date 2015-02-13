from cell import Cell

class CellTests:
	def test_cell_create(self):
		c = Cell(0, 0)
		
		#print("testing Cell was created.")
		assert c, "Failed to create cell"
		#print("testing row was set correctly")
		assert c.row == 0, "Incorrect row value on cell {0}".format(c.row)
		#print("testing column was set correctly")
		assert c.column == 0, "Incorrect column value on cell {0}".format(c.column)
		
		#print("testing that an empty list for links was created")
		assert len(c._links) == 0, "cell links is not an empty list"
		
		#print("testing north is accessible and  has value None.")
		assert not c.north, "cell north neighbor is not None"
		#print("testing east is accessible and  has value None.")
		assert not c.east, "cell east neighbor is not None"
		#print("testing south is accessible and  has value None.")
		assert not c.south, "cell south neighbor is not None"
		#print("testing west is accessible and  has value None.")
		assert not c.west, "cell west neighbor is not None"
		
		print("All cell creation tests passed")
		
	def test_cell_neighbors(self):
		c1 = Cell(1, 1)
		assert c1, "failed to create Cell(1, 1)"
		c2 = Cell(1, 2)
		assert c2, "failed to create Cell(1, 2)"
		
		#print("setting c1 and c2 as neighbors")
		c1.east = c2
		c2.west = c1
		
		#print("testing that neighbor fields have been set correctly")
		assert c1.east == c2, "c1.east does not return c2 as expected"
		assert not c1.north, "c1.north has been set unexpectedly"
		assert not c1.south, "c1.south has been set unexpectedly"
		assert not c1.west, "c1.west has been set unexpectedly"
		assert c2.west == c1, "c2.west does not return c1 as expected"
		assert not c2.north, "c2.north has been set unexpectedly"
		assert not c2.east, "c2.east has been set unexpectedly"
		assert not c2.south, "c2.south has been set unexpectedly"
		
		#print ("testing that both cells return a list of neighbors with length of 1")
		assert len(c1.neighbors()) == 1, "list returned but c1.neighbors() does not have a length of 1"
		assert len(c2.neighbors()) == 1, "list returned but c2.neighbors() does not have a length of 1"

		#print("testing that neither cell has links.")
		assert len(c1._links) == 0, "cell c1 links is not an empty list"
		assert len(c2._links) == 0, "cell c1 links is not an empty list"

		print("All cell neighbor tests passed")
		
	def test_cell_links(self):
		c1 = Cell(1, 1)
		assert c1, "failed to create Cell(1, 1)"
		c2 = Cell(1, 2)
		assert c2, "failed to create Cell(1, 2)"

		assert not c1.is_linked(c2), "c1 is already linked to c2 and should not be"
		assert not c2.is_linked(c1), "c2 is already linked to c1 and should not be"
		
		c1.link(c2)
		assert c1.is_linked(c2), "c1 did not link to c2 correctly"
		assert c2.is_linked(c1), "c2 did not link to c1 correctly"
		
		c2.unlink(c1)
		assert not c2.is_linked(c1), "c2 did not unlink from c1 correctly"
		assert not c1.is_linked(c2), "c1 did not unlink from c2 correctly"
		
		print("All cell links tests passed")
		
	def run(self):
		self.test_cell_create()
		self.test_cell_neighbors()
		self.test_cell_links()

if __name__ == "__main__":
	CellTests().run()
		