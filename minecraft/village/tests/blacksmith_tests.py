from mcpi.vec3 import Vec3
from village.tests.tester_base import TesterBase
from village.blacksmith import Blacksmith

class BlacksmithTester(TesterBase):
	def __init__(self, *args, **kwargs):
		super(BlacksmithTester, self).__init__(sut_name = "Blacksmith", *args, **kwargs)
		self.default_offset = Vec3(-2,0-5)

	def _create_blacksmith(self, orientation):
		return Blacksmith(self.pos, orientation, self.default_offset)

	def run(self, *args, **kwargs):
		super(BlacksmithTester, self).run(self._create_blacksmith, *args, **kwargs)


