from property import Property

class Apartment(Property):
	valid_laundries = ("coin", "ensuite", "none")
	valid_balconies = ("yes", "no", "solarium")
	
	def __init__(self, balcony='', laundry='', **kwargs):
		super().__init__(**kwargs)
		self.balcony = balcony
		slef.laundry = laundry
	
	def display(self):
		super().display()
		print("APARTMENT DETAILS")
		print("laundry: %s" % self.laundry)
		print("has balcony: %s" % self.balcony)
		
	def prompt_init():
		parent_init = Property.prompt_init()
		laundry = get_valid_input("What laundry facilities does "
								"the propery have? ", Apartment.valid_laundries)
		balcony = get_valid_input("Does the property have a balcony? ",
								  Apartment.valid_balconies)
		
		parent_init.update({"laundry": laundry,
							"balcony": balcony
		})
		return parent_init
	prompt_init = staticmethod(prompt_init)

		
		
		