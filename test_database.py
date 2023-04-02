"""A small database to test out api call functions"""

def test_books_list_raw():
     """ This function returns a list of the raw json text of three books from
     making an api call. Example: 
     https://openlibrary.org/books/OL46060039M.json """

     raw_list = [
               {"type": {"key": "/type/edition"}, "title": "Kindness is My Superpower", "authors": [{"key": "/authors/OL9144752A"}], "publish_date": "Jul 27, 2020", "source_records": ["amazon:1735974102", "bwb:9781735974101"], "number_of_pages": 40, "publishers": ["Alicia Ortego"], "physical_format": "hardcover", "full_title": "Kindness is My Superpower : A children's Book About Empathy, Kindness and Compassion", "subtitle": "A children's Book About Empathy, Kindness and Compassion", "notes": "Source title: Kindness is My Superpower: A children's Book About Empathy, Kindness and Compassion", "covers": [12101562], "works": [{"key": "/works/OL26145046W"}], "key": "/books/OL35289538M", "identifiers": {}, "classifications": {}, "isbn_10": ["1735974102"], "isbn_13": ["9781735974101"], "description": {"type": "/type/text", "value": "Throughout the story, little superhero Lucas will learn what kindness means and understand what it is like to be kind, sensitive, caring, and generous."}, "latest_revision": 4, "revision": 4, "created": {"type": "/type/datetime", "value": "2021-10-17T07:12:14.282645"}, "last_modified": {"type": "/type/datetime", "value": "2023-01-27T15:54:23.543805"}},
               {"subjects": ["Children's fiction", "Sisters, fiction", "First day of school, fiction", "Muslims, fiction", "nyt:picture-books=2019-09-29", "New York Times bestseller", "Schools, fiction", "Clothing and dress, fiction"], "key": "/works/OL20128080W", "title": "The Proudest Blue", "authors": [{"author": {"key": "/authors/OL7895701A"}, "type": {"key": "/type/author_role"}}, {"author": {"key": "/authors/OL7615569A"}, "type": {"key": "/type/author_role"}}, {"author": {"key": "/authors/OL7895702A"}, "type": {"key": "/type/author_role"}}], "type": {"key": "/type/work"}, "covers": [12705548, 8780455, 10219291], "description": {"type": "/type/text", "value": "With her new backpack and light-up shoes, Faizah knows the first day of school is going to be special. It's the start of a brand new year and, best of all, it's her older sister Asiya's first day of hijab--a hijab of beautiful blue fabric, like the ocean waving to the sky. But not everyone sees hijab as beautiful, and in the face of hurtful, confusing words, Faizah will find new ways to be strong."}, "latest_revision": 9, "revision": 9, "created": {"type": "/type/datetime", "value": "2019-09-11T17:04:54.300918"}, "last_modified": {"type": "/type/datetime", "value": "2023-01-26T01:13:20.222898"}},
               {"type": {"key": "/type/edition"}, "authors": [{"key": "/authors/OL12310763A"}], "languages": [{"key": "/languages/eng"}], "publish_date": "2022", "publishers": ["Bumble Bee Books"], "source_records": ["bwb:9781839345777"], "title": "Kairavs Colorful Feelings", "works": [{"key": "/works/OL34025494W"}], "key": "/books/OL46060039M", "identifiers": {}, "isbn_13": ["9781839345777"], "classifications": {}, "covers": [13260645], "latest_revision": 3, "revision": 3, "created": {"type": "/type/datetime", "value": "2023-01-17T05:03:45.212091"}, "last_modified": {"type": "/type/datetime", "value": "2023-02-09T00:59:49.800321"}}  
               ]
     return raw_list


def test_books_list_dicts():
     """ This functions returns a list of dictionaries that show a correct
     dictionary of each book """
     
     book_list_of_dicts = [
          {"title": "Kindness is My Superpower",
          "year_published": "2020",
          "Cover Path": "https://covers.openlibrary.org/b/id/12101562-L.jpg",
          "isbn_13": "9781735974101",
          "author_name": ["Alicia Ortego"],
          "overview": "Throughout the story, little superhero Lucas will learn what kindness means and understand what it is like to be kind, sensitive, caring, and generous.",
          "gender_identity": "",
          "racial_identity": ""
          },

          {"title": "The Proudest Blue",
          "year_published": "0",
          "Cover Path": "https://covers.openlibrary.org/b/id/12705548-L.jpg",
          "isbn_13": "9781783449729",
          "author_name": ["Ibtihaj Muhammad", "S. K. Ali", "Hatem Aly"],
          "overview": "With her new backpack and light-up shoes, Faizah knows the first day of school is going to be special. It's the start of a brand new year and, best of all, it's her older sister Asiya's first day of hijab--a hijab of beautiful blue fabric, like the ocean waving to the sky. But not everyone sees hijab as beautiful, and in the face of hurtful, confusing words, Faizah will find new ways to be strong.",
          "gender_identity": "",
          "racial_identity": ""
          }, 

          {
          "title": "Kairavs Colorful Feelings",
          "year_published": "2022",
          "Cover Path": "https://covers.openlibrary.org/b/id/13260645-L.jpg",
          "isbn_13": "9781839345777",
          "author_name": ["Launika Arya Raykar"],
          "overview": "No overview for this book",
          "gender_identity": "",
          "racial_identity": ""
          }
     ]

     return book_list_of_dicts