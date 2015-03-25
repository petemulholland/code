from mcpi import minecraft
from village.tests.tester_base import TesterBase
from village.building import SLEEP_SECS
from village.lamppost import LampPost

class LampPostTester(TesterBase):
	def __init__(self, *args, **kwargs):
		super(LampPostTester, self).__init__(sut_name = "LampPost", *args, **kwargs)

	def _create_lamppost(self, orientation):
		return LampPost(self.default_offset, orientation, self.pos)

	def run(self, *args, **kwargs):
		super(LampPostTester, self).run(self._create_lamppost, *args, **kwargs)

		