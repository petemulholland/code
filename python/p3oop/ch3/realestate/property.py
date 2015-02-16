class Property:
	def __init__(self, square_feet='', beds='', baths='', **kwargs):
		super().__init__(**kwargs)
		self.square_feet = square_feet 
		self.num_bedrooms = beds
		self.num_bathrooms = baths
		
	def display(sef):
		print("PROPERTY DETAILS")
		print("================")
		print("square footage: {}".format(self.square_feet))
		print("bedrooms: {}".format(self.num_bedrooms))
		print("bathrooms: {}".format(self.num_bathrooms))
		
		
	def prompt_init(): # no self here?
		return dict(square_feet=input("Enter the square feet: "),
					beds=input("Enter number of bedrooms: "),
					baths=input("Enter number of bathrooms: "))
	prompt_init = staticmethod(prompt_init)