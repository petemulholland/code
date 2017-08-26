from village.tests.tester_base import BuildingTesterBase
from village.library import Library

class LibraryTester(BuildingTesterBase):
	def __init__(self, *args, **kwargs):
		super(LibraryTester, self).__init__(Library, sut_name="Library", *args, **kwargs)

	def run(self, *args, **kwargs):
		super(LibraryTester, self).run(*args, **kwargs)

