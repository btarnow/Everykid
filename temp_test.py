"""Practice creating unit tests for the temp.py file which mostly mirrors the 
book_info_from_API.py"""

import unittest
from temp import get_title, get_publish_date, get_cover_url_path, get_overview

class TempTests(unittest.TestCase):

  def test_get_title(self):
    """Test that get_title can find a title entry in a dictionary."""

    expected_title = "Kindness is My Superpower"

    test_data_with_title = { "title": expected_title }

    self.assertEqual(expected_title, get_title(test_data_with_title))

    test_data_without_title = {}

    expected_not_found_msg = "No title found"
    self.assertEqual(expected_not_found_msg, get_title(test_data_without_title))


  def test_get_publish_date_works(self):
    """Test that get_publish_date can find a publish date entry in a dictionary"""
    # TODO

  def test_get_publish_date_returns_year(self):
    """Test that get_publish_date only returns the published year"""
    # TODO

  def test_get_cover_url_path(self):
    """"""
    # TODO

  def test_get_overview(self):
    """"""
    # TODO

unittest.main()