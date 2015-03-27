from mcpi.vec3 import Vec3
from village.tests.tester_base import TesterBase
from village.church import Church

class ChurchTester(TesterBase):
	def __init__(self, *args, **kwargs):
		super(ChurchTester, self).__init__(sut_name = "Church", *args, **kwargs)
		self.default_offset = Vec3(-2,0-5)

	def _create_building(self, orientation):
		return Church(self.pos, orientation, self.default_offset)

	def run(self, *args, **kwargs):
		super(ChurchTester, self).run(self._create_building, *args, **kwargs)


