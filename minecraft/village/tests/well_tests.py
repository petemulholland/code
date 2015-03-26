from mcpi.vec3 import Vec3
from village.tests.tester_base import TesterBase
from village.well import Well

class WellTester(TesterBase):
	def __init__(self, *args, **kwargs):
		super(WellTester, self).__init__(sut_name = "Well", *args, **kwargs)
		self.default_offset = Vec3(0,0-5)

	def _create_well(self, orientation):
		return Well(self.pos, orientation, self.default_offset)

	def run(self, *args, **kwargs):
		super(WellTester, self).run(self._create_well, *args, **kwargs)

		
