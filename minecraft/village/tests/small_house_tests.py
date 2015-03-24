from mcpi import minecraft
from village.tests.building_tests import BuildingTestsBase, SLEEP_SECS
from village.small_house import SmallHouse

class SmallHouseTests(BuildingTestsBase):
	def __init__(self, *args, **kwargs):
		super(SmallHouseTests, self).__init__(sut_name = "Small House", *args, **kwargs)

	def _create_small_house(self, orientation):
		return SmallHouse(self.default_offset, orientation)

	def run(self):
		super(SmallHouseTests, self).run(self._create_small_house)

		
def create_small_house_tester():
	mc = minecraft.Minecraft.create()
	return SmallHouseTests(mc, SLEEP_SECS)

def run_small_house_tests():
	tester = create_small_house_tester()
	tester.run()

if __name__ == "__main__":
	run_small_house_tests()
