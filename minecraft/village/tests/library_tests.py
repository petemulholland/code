from mcpi.vec3 import Vec3
from village.tests.tester_base import TesterBase
from village.library import Library

class LibraryTester(TesterBase):
	def __init__(self, *args, **kwargs):
		super(LibraryTester, self).__init__(sut_name = "Library", *args, **kwargs)
		self.default_offset = Vec3(0,0-5)

	def _create_building(self, orientation):
		return Library(self.pos, orientation, self.default_offset)

	def run(self, *args, **kwargs):
		super(LibraryTester, self).run(self._create_building, *args, **kwargs)

