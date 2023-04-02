"""Practice creating unit tests for the temp.py file which mostly mirrors the 
book_info_from_API.py"""

import unittest
from temp import get_title, get_publish_date, get_cover_url_path, get_overview
from test_database import test_books_list_dicts, test_books_list_raw


test_books_raw = test_books_list_raw()
test_books_list_of_dicts = test_books_list_dicts()


class TempTests(unittest.TestCase):

  def test_get_title_works(self):
      """Tests that get_title can find a title entry in a dictionary."""

      for index, raw_book in enumerate(test_books_raw):
          expected_book_dict = test_books_list_of_dicts[index]
          expected_title = expected_book_dict["title"]
          
          with self.subTest():
              self.assertEqual(expected_title, get_title(raw_book), 
                               f"{expected_title} was expected")
  

  def test_get_publish_date_returns_year(self):
      """Test that get_publish_date only returns the published year"""
      
      for index, raw_book in enumerate(test_books_raw):
          expected_book_dict = test_books_list_of_dicts[index]
          expected_year_published = expected_book_dict["year_published"]

          with self.subTest():
              self.assertEqual(expected_year_published, get_publish_date(raw_book), 
                               f"{expected_year_published} was expected")
              

  def test_get_cover_url_path(self):
      """"""
      # TODO: 

  
  def test_get_overview(self):
      """"""
      # TODO: 


unittest.main()