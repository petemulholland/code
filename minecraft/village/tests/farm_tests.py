from village.tests.tester_base import BuildingTesterBase
from village.farm import Farm

class FarmTester(BuildingTesterBase):
	def __init__(self, *args, **kwargs):
		super(FarmTester, self).__init__(Farm, sut_name="Farm", *args, **kwargs)

	# TODO: any need to override run anymore?
	# could throw all Building tester cllasses in 1 file if it's just the init on each.
	def run(self, *args, **kwargs):
		super(FarmTester, self).run(*args, **kwargs)


class LargeFarmTester(BuildingTesterBase):
	def __init__(self, *args, **kwargs):
		super(LargeFarmTester, self).__init__(LargeFarm, sut_name="Farm", *args, **kwargs)

	# TODO: any need to override run anymore?
	# could throw all Building tester cllasses in 1 file if it's just the init on each.
	def run(self, *args, **kwargs):
		super(LargeFarmTester, self).run(*args, **kwargs)


