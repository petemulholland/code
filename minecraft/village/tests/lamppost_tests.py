from mcpi.vec3 import Vec3
from village.tests.tester_base import BuildingTesterBase
from village.lamppost import LampPost

class LampPostTester(BuildingTesterBase):
	def __init__(self, *args, **kwargs):
		super(LampPostTester, self).__init__(LampPost, sut_name="LampPost", *args, **kwargs)

	def run(self, *args, **kwargs):
		super(LampPostTester, self).run(*args, **kwargs)

		