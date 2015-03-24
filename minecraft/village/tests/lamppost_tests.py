from mcpi import minecraft
from village.tests.building_tests import BuildingTestsBase, SLEEP_SECS
from village.lamppost import LampPost

class LampPostTests(BuildingTestsBase):
	def __init__(self, *args, **kwargs):
		super(LampPostTests, self).__init__(sut_name = "LampPost", *args, **kwargs)

	def _create_lamppost(self, orientation):
		return LampPost(self.default_offset, orientation, self.pos)

	def run(self):
		super(LampPostTests, self).run(self._create_lamppost)

		
def create_lamppost_tester():
	mc = minecraft.Minecraft.create()
	return LampPostTests(mc, SLEEP_SECS)

def run_lamppost_tests():
	tester = create_lamppost_tester()
	tester.run()
