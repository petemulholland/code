from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page
from lists.models import Item

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        #print('Running test_root_url_resolves_to_home_page_view')
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_correct_html(self):
        #print('Running test_home_page_returns_correct_html')
        request = HttpRequest()
        response = home_page(request)

        expected_html = render_to_string('home.html')
        self.assertTrue(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        #print('Running test_home_page_can_save_a_POST_request')
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string(
                            'home.html', 
                            {'new_item_text': 'A new list item' }
        )

        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Item.objects.count(), 0)


class ItemModelTest(TestCase):
    
    def test_saving_and_retrieving_items(self):
        #print('Running test_home_page_can_save_a_POST_request')
        first_item = Item()
        first_item.text = 'The First (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The First (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')



