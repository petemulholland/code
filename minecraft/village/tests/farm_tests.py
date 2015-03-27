from mcpi.vec3 import Vec3
from village.tests.tester_base import TesterBase
from village.farm import Farm

class FarmTester(TesterBase):
	def __init__(self, *args, **kwargs):
		super(FarmTester, self).__init__(sut_name = "Farm", *args, **kwargs)
		self.default_offset = Vec3(0,0-5)

	def _create_building(self, orientation):
		return Farm(self.pos, orientation, self.default_offset)

	def run(self, *args, **kwargs):
		super(FarmTester, self).run(self._create_building, *args, **kwargs)


