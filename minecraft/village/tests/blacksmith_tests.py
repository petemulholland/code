from village.tests.tester_base import BuildingTesterBase
from village.blacksmith import Blacksmith

class BlacksmithTester(BuildingTesterBase):
	def __init__(self, *args, **kwargs):
		super(BlacksmithTester, self).__init__(Blacksmith, sut_name="Blacksmith", *args, **kwargs)

	def run(self, *args, **kwargs):
		super(BlacksmithTester, self).run(*args, **kwargs)


