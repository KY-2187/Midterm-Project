from django.test import TestCase


class IngredientsListTest(TestCase):

	def test_ingredients_list_returns_correct_html(self):
		response = self.client.get('ingredients_list')
		self.assertTemplateUsed(response, 'ingredients_list.html')


class IngredientsDetailTest(TestCase):

	def test_ingredients_detail_returns_correct_html(self):
		response = self.client.get('ingredients_detail')
		self.assertTemplateUsed(response, 'ingredients_detail.html')


class IngredientsUpdateTest(TestCase):

	def test_ingredients_update_returns_correct_html(self):
		response = self.client.get('ingredients_update')
		self.assertTemplateUsed(response, 'ingredients_update_form.html')


class IngredientsCreateTest(TestCase):

	def test_ingredients_create_returns_correct_html(self):
		response = self.client.get('ingredients_create')
		self.assertTemplateUsed(response, 'ingredients_create_form.html')


class RecipesDetailTest(TestCase):

	def test_recipes_detailt_returns_correct_html(self):
		response = self.client.get('recipes_detail')
		self.assertTemplateUsed(response, 'recipes_detail.html')


class RecipesUpdateTest(TestCase):

	def test_recipes_update_returns_correct_html(self):
		response = self.client.get('recipes_update')
		self.assertTemplateUsed(response, 'recipes_update_form.html')


class RecipesCreateTest(TestCase):

	def test_recipes_create_returns_correct_html(self):
		response = self.client.get('recipes_create')
		self.assertTemplateUsed(response, 'recipes_create_form.html')


class OrdersListTest(TestCase):

	def test_orders_list_returns_correct_html(self):
		response = self.client.get('orders_list')
		self.assertTemplateUsed(response, 'orders_list.html')


class OrdersDetailTest(TestCase):

	def test_orders_detail_returns_correct_html(self):
		response = self.client.get('orders_detail')
		self.assertTemplateUsed(response, 'orders_detail.html')


class OrdersUpdateTest(TestCase):

	def test_orders_update_returns_correct_html(self):
		response = self.client.get('orders_update')
		self.assertTemplateUsed(response, 'orders_update_form.html')


class OrdersCreateTest(TestCase):

	def test_orders_list_returns_correct_html(self):
		response = self.client.get('orders_create')
		self.assertTemplateUsed(response, 'orders_create_form.html')