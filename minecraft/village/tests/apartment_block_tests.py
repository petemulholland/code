from village.tests.tester_base import BuildingTesterBase
from village.apartment_block import ApartmentBlock

class ApartmentBlockTester(BuildingTesterBase):
	def __init__(self, *args, **kwargs):
		super(ApartmentBlockTester, self).__init__(ApartmentBlock, sut_name="ApartmentBlock", *args, **kwargs)

	def run(self, *args, **kwargs):
		super(ApartmentBlockTester, self).run(*args, **kwargs)


