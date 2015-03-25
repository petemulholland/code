from mcpi import minecraft
from village.tests.tester_base import TesterBase
from village.building import SLEEP_SECS
from village.well import Well

class WellTester(TesterBase):
	def __init__(self, *args, **kwargs):
		super(WellTester, self).__init__(sut_name = "Well", *args, **kwargs)

	def _create_well(self, orientation):
		return Well(self.default_offset, orientation, self.pos)

	def run(self):
		super(WellTester, self).run(self._create_well)

		
