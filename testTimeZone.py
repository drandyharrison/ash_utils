import unittest
from TimeZone import TimeZone


class testTimeZone(unittest.TestCase):
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
        tz_class = TimeZone()
        # assert
        self.assertRaises(TypeError, tz_class.is_tz_valid, tz)

    def test_is_tz_valid_invalid_tz(self):
        """Checks that is_tz_valid returns False for invalid timezone"""
        print("@test_is_tz_valid_invalid_tz")
        # arrange
        tz = "invalid tz"
        # act
        tz_class = TimeZone()
        # assert
        self.assertFalse(tz_class.is_tz_valid(tz))
        print("done")

    def test_is_tz_valid_valid_tz(self):
        """Checks that is_tz_valid returns True for valid timezone"""
        print("@test_is_tz_valid_valid_tz")
        # arrange
        tz = "Europe/London"
        # act
        tz_class = TimeZone()
        # assert
        self.assertTrue(tz_class.is_tz_valid(tz))

    def test_is_singleton(self):
        """Checks TimeZone is a singleton"""
        print("@test_is_singleton")
        # arrange
        tz_class1 = TimeZone()
        tz_class2 = TimeZone()
        # act
        # assert
        self.assertEquals(id(tz_class1), id(tz_class2))


# run tests
if __name__ == '__main__':
    unittest.main(verbosity=2)
