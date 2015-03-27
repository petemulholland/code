from mcpi.vec3 import Vec3
from village.tests.tester_base import TesterBase
from village.butcher import Butcher

class ButcherTester(TesterBase):
	def __init__(self, *args, **kwargs):
		super(ButcherTester, self).__init__(sut_name = "Butcher", *args, **kwargs)
		self.default_offset = Vec3(0,0-5)

	def _create_building(self, orientation):
		return Butcher(self.pos, orientation, self.default_offset)

	def run(self, *args, **kwargs):
		super(ButcherTester, self).run(self._create_building, *args, **kwargs)

