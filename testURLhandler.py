import unittest
from URLhandler import URLhandler


class testURLhandler(unittest.TestCase):
    def SetUp(self):
        """set-up code, which is called before each test, to avoid repetition"""
        pass

    def tearDown(self):
        """code to tidy up after each test"""
        pass

    def test_creator(self):
        """Test that creator throws a ValueError for a non-string url"""
        print("@test_creator")
        # arrange
        url_int = 25
        # act
        # assert
        self.assertRaises(ValueError, URLhandler, url_int)

    def test_invalid_url(self):
        """Checks that a badly url returns False when checked"""
        print("@test_invalid_url")
        # arrange
        url_str = "google"
        # act
        urlhndlr = URLhandler(url_str)
        # assert
        self.assertFalse(urlhndlr.check_url())

    def test_non_exist_url(self):
        """Checks that a well formed url that doesn't exist returns False when checked"""
        print("@test_non_exist_url")
        # arrange
        url_str = "https://www.shddf.xx.xx"
        # act
        urlhndlr = URLhandler(url_str)
        # assert
        self.assertFalse(urlhndlr.check_url())

    def test_exist_url(self):
        """Checks that a valid url returns True when checked"""
        print("@test_exist_url")
        # arrange
        url_str = "https://www.google.co.uk"
        # act
        urlhndlr = URLhandler(url_str)
        # assert
        self.assertTrue(urlhndlr.check_url())


# run tests
if __name__ == '__main__':
    unittest.main(verbosity=2)
