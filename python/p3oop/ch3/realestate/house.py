from property import Property

class House(Property):
	valid_garage = ("attached", "detached", "none")
	valid_fenced = ("yes", "no")

	def __init__(self, num_stories='', garage='', fenced='', **kwargs):
		super().__init__(**kwargs)
		self.num_stories = num_stories
		self.garage = garage
		self.fenced = fenced
		
	def display(self):
		super().display()
		print("HOUSE DETAILS")
		print("# of stories: {}".format(self.num_stories))
		print("garage: {}".format(self.garage))
		print("fenced yard: {}".format(self.fenced))
		
	def prompt_init():
		parent_init = Property.prompt_init()
		fenced = get_valid_input("Is the yard fenced?  ",
								  House.valid_fenced)
		garage = get_valid_input("Is there a garage? ",
								  House.valid_garage)
		num_stories = input("How many stories? ")
		
		parent_init.update({
			"garage": garage,
			"fenced": fenced,
			"num_stories": num_stories
		})
		return parent_init
	prompt_init = staticmethod(prompt_init)
