from mcpi.vec3 import Vec3
from village.tests.tester_base import BuildingTesterBase
from village.small_house import SmallHouseV1, SmallHouseV2, SmallHouseV3

###########################################
## SmallHouseV1 tests
###########################################
class SmallHouseV1Tester(BuildingTesterBase):
	def __init__(self, *args, **kwargs):
		super(SmallHouseV1Tester, self).__init__(SmallHouseV1, sut_name="Small House V1", *args, **kwargs)

	def run(self, *args, **kwargs):
		super(SmallHouseV1Tester, self).run(*args, **kwargs)

		
###########################################
## SmallHouseV2 tests
###########################################
class SmallHouseV2Tester(BuildingTesterBase):
	def __init__(self, *args, **kwargs):
		super(SmallHouseV2Tester, self).__init__(SmallHouseV2, sut_name="Small House V2", *args, **kwargs)

	def run(self, *args, **kwargs):
		super(SmallHouseV2Tester, self).run(*args, **kwargs)

		
###########################################
## SmallHouseV3 tests
###########################################
class SmallHouseV3Tester(BuildingTesterBase):
	def __init__(self, *args, **kwargs):
		super(SmallHouseV3Tester, self).__init__(SmallHouseV3, sut_name="Small House V3", *args, **kwargs)

	def run(self, *args, **kwargs):
		super(SmallHouseV3Tester, self).run(*args, **kwargs)

		
if __name__ == "__main__":
	SmallHouseV1Tester.run_tests(mc)
	SmallHouseV2Tester.run_tests(mc)
	SmallHouseV3Tester.run_tests(mc)
