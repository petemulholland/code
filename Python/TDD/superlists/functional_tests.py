#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. she foes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # she notices the page title and header mention to-do- lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # she is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do item')
        
        new_todo_text = 'Buy peacock feathers'
        expected_list_text = '1: ' + new_todo_text
        # she types "Buy peacock feathers" into a tests box <insert humour>
        inputbox.send_keys(new_todo_text)

        # when she hits enter the page updates, and now the page lists 
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        # Debugging:
        #import time
        #time.sleep(5)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        
        self.assertIn(expected_list_text, [row.text for row in rows])

        # there is still a text box inviting her to add another item.
        # she enters "Use peackock feathers to make a fly"
        
        # the page updates again, an now shows both items on her list

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisified, she goes back to sleep.

        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')

