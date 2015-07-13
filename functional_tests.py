from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):

		#user has heard about new to-do app.  Checks out homepage
		self.browser.get('http://localhost:8000')

		#notices page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		#invited to enter a to-do item straight away

		#types 'buy peacock feathers' into text box. 

		#when she hits enter, page updates and page lists first item as entered

		#text box persists for her to add another item. 
		#she enters 'use peacock feathers to make a fly'

		#page updates again and now shows both items on her list

		#user wonders whether site will remember her list.  She sees
		#website has generated a unique URL for her.  -- explanatory
		#text to that effect.  

		#she visits that URL - her to do list is still there. 


if __name__ == '__main__':
	unittest.main(warnings='ignore')

