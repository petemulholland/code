from mcpi.vec3 import Vec3
from village.tests.tester_base import TesterBase
from village.lamppost import LampPost

class LampPostTester(TesterBase):
	def __init__(self, *args, **kwargs):
		super(LampPostTester, self).__init__(sut_name = "LampPost", *args, **kwargs)
		self.default_offset = Vec3(0,0-3)

	# TODO: keep creator to handle Building, layer & block tests 
	# or rip out & figure something else out for those tests

	def _create_building(self, orientation):
		return LampPost(self.pos, orientation, self.default_offset)

	def run(self, *args, **kwargs):
		super(LampPostTester, self).run(self._create_building, *args, **kwargs)

		