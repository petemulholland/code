from mcpi.vec3 import Vec3
from village.tests.tester_base import BuildingTesterBase
from village.well import Well

class WellTester(BuildingTesterBase):
	def __init__(self, *args, **kwargs):
		super(WellTester, self).__init__(Well, sut_name = "Well", *args, **kwargs)

	def run(self, *args, **kwargs):
		super(WellTester, self).run(*args, **kwargs)

		
