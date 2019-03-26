import unittest
from GoogleCalAPIHandler import GoogleCalAPIHandler


class testGoogleCalAPIHandler(unittest.TestCase):
    def SetUp(self):
        """set-up code, which is called before each test, to avoid repetition"""
        pass

    def tearDown(self):
        """code to tidy up after each test"""
        pass

    def test_is_tz_valid_tz_not_string(self):
        """Checks that is_tz_valid throws a TypeError for a non-string tz"""
        print("@test_is_tz_valid_tz_not_string")
        # arrange
        tz = 25
        # act
        calhndlr = GoogleCalAPIHandler()
        # assert
        self.assertRaises(TypeError, calhndlr.is_tz_valid, tz)

    def test_is_tz_valid_invalid_tz(self):
        """Checks that is_tz_valid returns False for invalid timezone"""
        print("@test_is_tz_valid_invalid_tz")
        # arrange
        tz = "invalid tz"
        # act
        calhndlr = GoogleCalAPIHandler()
        # assert
        self.assertFalse(calhndlr.is_tz_valid(tz))
        print("done")

    def test_is_tz_valid_valid_tz(self):
        """Checks that is_tz_valid returns True for valid timezone"""
        print("@test_is_tz_valid_valid_tz")
        # arrange
        tz = "Europe/London"
        # act
        calhndlr = GoogleCalAPIHandler()
        # assert
        self.assertTrue(calhndlr.is_tz_valid(tz))

# run tests
if __name__ == '__main__':
    unittest.main(verbosity=2)
