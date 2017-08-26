from village.tests.tester_base import BuildingTesterBase
from village.large_house import LargeHouse

class LargeHouseTester(BuildingTesterBase):
	def __init__(self, *args, **kwargs):
		super(LargeHouseTester, self).__init__(LargeHouse, sut_name = "LargeHouse", *args, **kwargs)

	def run(self, *args, **kwargs):
		super(LargeHouseTester, self).run(*args, **kwargs)

