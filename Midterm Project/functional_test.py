import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_displays_ingredients_list(self):
		self.browser.get('http://localhost:8000/ingredients_list')

		self.assertIn('Ingredients - List', self.browser.title)

		self.assertIn(self.browser.current_url,'http://localhost:8000/ingredients_list')

	def test_displays_ingredients_detail(self):
		self.browser.get('http://localhost:8000/ingredients_detail')

		self.assertIn('Ingredients - Detail', self.browser.title)

		self.assertIn(self.browser.current_url,'http://localhost:8000/ingredients_detail')

	def test_displays_ingredients_update(self):
		self.browser.get('http://localhost:8000/ingredients_update')

		self.assertIn('Ingredients - Update', self.browser.title)

		self.assertIn(self.browser.current_url,'http://localhost:8000/ingredients_update')

	def test_displays_ingredients_create(self):
		self.browser.get('http://localhost:8000/ingredients_create')

		self.assertIn('Ingredients - Create', self.browser.title)

		self.assertIn(self.browser.current_url,'http://localhost:8000/ingredients_create')

	def test_displays_recipes_list(self):
		self.browser.get('http://localhost:8000/recipes_list')

		self.assertIn('Recipes - List', self.browser.title)

		self.assertIn(self.browser.current_url,'http://localhost:8000/recipes_list')

	def test_displays_recipes_detail(self):
		self.browser.get('http://localhost:8000/recipes_detail')

		self.assertIn('Recipes - Detail', self.browser.title)

		self.assertIn(self.browser.current_url,'http://localhost:8000/recipes_detail')

	def test_displays_recipes_update(self):
		self.browser.get('http://localhost:8000/recipes_update')

		self.assertIn('Recipes - Update', self.browser.title)

		self.assertIn(self.browser.current_url,'http://localhost:8000/recipes_update')

	def test_displays_recipes_create(self):
		self.browser.get('http://localhost:8000/recipes_create')

		self.assertIn('Recipes - Create', self.browser.title)

		self.assertIn(self.browser.current_url,'http://localhost:8000/recipes_create')

	def test_displays_orders_list(self):
		self.browser.get('http://localhost:8000/orders_list')

		self.assertIn('Orders - List', self.browser.title)

		self.assertIn(self.browser.current_url,'http://localhost:8000/orders_list')

	def test_displays_orders_detail(self):
		self.browser.get('http://localhost:8000/orders_detail')

		self.assertIn('Orders - Detail', self.browser.title)

		self.assertIn(self.browser.current_url,'http://localhost:8000/orders_detail')

	def test_displays_orders_update(self):
		self.browser.get('http://localhost:8000/orders_update')

		self.assertIn('Orders - Update', self.browser.title)

		self.assertIn(self.browser.current_url,'http://localhost:8000/orders_update')

	def test_displays_orders_create(self):
		self.browser.get('http://localhost:8000/orders_create')

		self.assertIn('Orders - Create', self.browser.title)

		self.assertIn(self.browser.current_url,'http://localhost:8000/orders_create')


		self.fail('Finish the test!')



if __name__ == '__main__':
	unittest.main(warnings = 'ignore')