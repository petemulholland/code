class Supplier(Contact):
	def order(self, order):
		print("If this were a real system we would sned {} order to {}".format(order, self.name))