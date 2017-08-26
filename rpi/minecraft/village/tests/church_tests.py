from village.tests.tester_base import BuildingTesterBase
from village.church import Church

class ChurchTester(BuildingTesterBase):
	def __init__(self, *args, **kwargs):
		super(ChurchTester, self).__init__(Church, sut_name="Church", *args, **kwargs)

	def run(self, *args, **kwargs):
		super(ChurchTester, self).run(*args, **kwargs)


