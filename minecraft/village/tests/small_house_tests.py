from mcpi import minecraft
from village.tests.tester_base import TesterBase
from village.building import SLEEP_SECS
from village.small_house import SmallHouseV1, SmallHouseV2, SmallHouseV3

###########################################
## SmallHouseV1 tests
###########################################
class SmallHouseV1Tester(TesterBase):
	def __init__(self, *args, **kwargs):
		super(SmallHouseV1Tester, self).__init__(sut_name = "Small House V1", *args, **kwargs)

	def _create_small_house(self, orientation):
		return SmallHouseV1(self.default_offset, orientation, self.pos)

	def run(self, *args, **kwargs):
		super(SmallHouseV1Tester, self).run(self._create_small_house, *args, **kwargs)

		
###########################################
## SmallHouseV2 tests
###########################################
class SmallHouseV2Tester(TesterBase):
	def __init__(self, *args, **kwargs):
		super(SmallHouseV2Tester, self).__init__(sut_name = "Small House V2", *args, **kwargs)

	def _create_small_house(self, orientation):
		return SmallHouseV2(self.default_offset, orientation, self.pos)

	def run(self, *args, **kwargs):
		super(SmallHouseV2Tester, self).run(self._create_small_house, *args, **kwargs)

		
###########################################
## SmallHouseV3 tests
###########################################
class SmallHouseV3Tester(TesterBase):
	def __init__(self, *args, **kwargs):
		super(SmallHouseV3Tester, self).__init__(sut_name = "Small House V3", *args, **kwargs)

	def _create_small_house(self, orientation):
		return SmallHouseV3(self.default_offset, orientation, self.pos)

	def run(self, *args, **kwargs):
		super(SmallHouseV3Tester, self).run(self._create_small_house, *args, **kwargs)

		
if __name__ == "__main__":
	SmallHouseV1Tester.run_tests(mc)
	SmallHouseV2Tester.run_tests(mc)
	SmallHouseV3Tester.run_tests(mc)
