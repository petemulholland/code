from mcpi import minecraft
from village.tests.tester_base import TesterBase
from village.building import SLEEP_SECS
from village.well import Well

class WellTester(TesterBase):
	def __init__(self, *args, **kwargs):
		super(WellTester, self).__init__(sut_name = "Well", *args, **kwargs)

	def _create_well(self, orientation):
		return Well(self.pos, orientation, self.default_offset)

	def run(self, *args, **kwargs):
		super(WellTester, self).run(self._create_well, *args, **kwargs)

		
