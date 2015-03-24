from mcpi import minecraft
from village.tests.building_tests import BuildingTestsBase, SLEEP_SECS
from village.well import Well

class WellTests(BuildingTestsBase):
	def __init__(self, *args, **kwargs):
		super(WellTests, self).__init__(sut_name = "Well", *args, **kwargs)

	def _create_well(self, orientation):
		return Well(self.default_offset, orientation)

	def run(self):
		super(WellTests, self).run(self._create_well)

		
def create_well_tester():
	mc = minecraft.Minecraft.create()
	return WellTests(mc, SLEEP_SECS)

def run_well_tests():
	tester = create_well_tester()
	tester.run()

