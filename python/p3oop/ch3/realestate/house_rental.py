from realestate.house import House
from realestate.rental import Rental

class HouseRental(Rental, House):
	def prompt_init():
		init = House.prompt_init()
		init.update(Rental.prompt_init())
		return init
		#return House.prompt_init().update(Rental.prompt_init()) # update doesn't return the dict
	prompt_init = staticmethod(prompt_init)
