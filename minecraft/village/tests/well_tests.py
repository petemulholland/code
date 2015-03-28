from mcpi.vec3 import Vec3
from village.tests.tester_base import TesterBase
from village.well import Well

class WellTester(TesterBase):
	def __init__(self, *args, **kwargs):
		super(WellTester, self).__init__(sut_name = "Well", klass=Well, *args, **kwargs)

	def run(self, *args, **kwargs):
		super(WellTester, self).run(*args, **kwargs)

		
