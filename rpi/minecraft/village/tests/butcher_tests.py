from village.tests.tester_base import BuildingTesterBase
from village.butcher import Butcher

class ButcherTester(BuildingTesterBase):
	def __init__(self, *args, **kwargs):
		super(ButcherTester, self).__init__(Butcher, sut_name="Butcher", *args, **kwargs)
	
	def run(self, *args, **kwargs):
		super(ButcherTester, self).run(*args, **kwargs)

