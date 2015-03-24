from mcpi import minecraft
from village.tests.building_tests import BuildingTestsBase, SLEEP_SECS
from village.small_house import SmallHouseV1

class SmallHouseV1Tests(BuildingTestsBase):
	def __init__(self, *args, **kwargs):
		super(SmallHouseV1Tests, self).__init__(sut_name = "Small House V1", *args, **kwargs)

	def _create_small_house(self, orientation):
		return SmallHouseV1(self.default_offset, orientation)

	def run(self):
		super(SmallHouseV1Tests, self).run(self._create_small_house)

		
def create_small_house_v1_tester():
	mc = minecraft.Minecraft.create()
	return SmallHouseV1Tests(mc, SLEEP_SECS)

def run_small_house_v1_tests():
	tester = create_small_house_v1_tester()
	tester.run()

if __name__ == "__main__":
	run_small_house_v1_tests()
