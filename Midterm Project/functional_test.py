import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def somethingsomething(self):


if __name__ == '__main__':
	unittest.main(warnings = 'ignore')