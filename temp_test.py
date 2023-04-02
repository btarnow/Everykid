"""Practice creating unit tests for the temp.py file which mostly mirrors the 
book_info_from_API.py"""

import unittest
from temp import get_title, get_publish_date, get_cover_url_path, get_overview


class TempTests(unittest.TestCase):

  def test_get_title_works(self):
      """Test that get_title can find a title entry in a dictionary."""

      expected_title = "Kindness is My Superpower"
      test_title_dict = {"title": expected_title}

      self.assertEqual(expected_title, get_title(test_title_dict))

  
  def test_get_title_not_found(self):
      """Test that if a title is not found it returns 'No title found' """

      test_data_without_title = {}
      expected_not_found_msg = "No title found"

      self.assertEqual(expected_not_found_msg, get_title(test_data_without_title))


  def test_get_publish_date_returns_year(self):
    """Test that get_publish_date only returns the published year"""
    
    test_dates_in_dict = [{"publish_date": "Jul 27, 2020"}, 
                          {"publish_date": "2022"}, {}]
    expected_dates= ["2020", "2022", "0"]

    for index, date in enumerate(test_dates_in_dict): 
        with self.subTest():
            expected_date = expected_dates[index]

        self.assertEqual(expected_date, get_publish_date(date), 
                     f"Expected date is {expected_date}")

  
  def test_get_cover_url_path(self):
    """"""
    # TODO: 

  
  def test_get_overview(self):
    """"""
    # TODO: 


unittest.main()