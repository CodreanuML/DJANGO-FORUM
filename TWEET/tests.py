from django.test import TestCase
from TWEET.models import Board
from django.urls import reverse
# Create your tests here.
from .forms import Board_Form




class View_test(TestCase):

	
	@classmethod
	def setUpTestData(cls):
        # SET UP TEST
		Board.objects.create(nume='Python', descriere='Python forum')

	def test_url_home(self):
		response = self.client.get('/tweet/home/')
		self.assertEqual(response.status_code, 200)
	def test_view_url_accessible_by_name_home(self):
		response= self.client.get(reverse('TWEET:home'))
		self.assertEqual(response.status_code, 200)

	def test_contains_form(self):
		url=reverse('TWEET:add_board')
		response=self.client.get(url)
		form=response.context.get('form')
		self.assertIsInstance(form,Board_Form)