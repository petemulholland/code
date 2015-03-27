from mcpi.vec3 import Vec3
from village.tests.tester_base import TesterBase
from village.large_house import LargeHouse

class LargeHouseTester(TesterBase):
	def __init__(self, *args, **kwargs):
		super(LargeHouseTester, self).__init__(sut_name = "LargeHouse", *args, **kwargs)
		self.default_offset = Vec3(0,0-5)

	def _create_large_house(self, orientation):
		return LargeHouse(self.pos, orientation, self.default_offset)

	def run(self, *args, **kwargs):
		super(LargeHouseTester, self).run(self._create_large_house, *args, **kwargs)

