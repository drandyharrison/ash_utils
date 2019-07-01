import unittest
from GarminHandler import GarminHandler
import datetime

class testGarminHandler(unittest.TestCase):
    def SetUp(self):
        """set-up code, which is called before each test, to avoid repetition"""
        pass

    def tearDown(self):
        """code to tidy up after each test"""
        pass

    def test_creator_non_string(self):
        """Test that creator throws a TypeError for a non-string url"""
        # arrange
        url_int = 25
        # act
        # assert
        self.assertRaises(TypeError, GarminHandler, url_int)

    def test_str2bool_not_str(self):
        """Test str2bool throws a TypeError when passed a non-string"""
        # arrange
        bool_int = 25
        # act
        # assert
        self.assertRaises(TypeError, GarminHandler.str2bool, bool_int)

    def test_str2bool_str_not_bool(self):
        """Test str2bool returns false when passed a non-boolean string"""
        # arrange
        non_bool_str = "GarminHandler"
        # act
        gh = GarminHandler("gcf55_config.yml")
        # assert
        self.assertFalse(gh.str2bool(non_bool_str))

    def test_str2bool_str_true_bool(self):
        """Test str2bool returns true when passed a string that represents a true value"""
        # arrange
        true_bool_str1 = "yes"
        true_bool_str2 = "true"
        true_bool_str3 = "t"
        true_bool_str4 = "1"
        true_bool_str5 = "YES"
        true_bool_str6 = "TrUe"
        true_bool_str7 = "T"
        # act
        gh = GarminHandler("gcf55_config.yml")
        # assert
        self.assertTrue(gh.str2bool(true_bool_str1))
        self.assertTrue(gh.str2bool(true_bool_str2))
        self.assertTrue(gh.str2bool(true_bool_str3))
        self.assertTrue(gh.str2bool(true_bool_str4))
        self.assertTrue(gh.str2bool(true_bool_str5))
        self.assertTrue(gh.str2bool(true_bool_str6))
        self.assertTrue(gh.str2bool(true_bool_str7))

    def test_str2bool_str_false_bool(self):
        """Test str2bool returns true when passed a string that represents a false value"""
        # arrange
        false_bool_str1 = "no"
        false_bool_str2 = "false"
        false_bool_str3 = "f"
        false_bool_str4 = "0"
        false_bool_str5 = "YENOS"
        false_bool_str6 = "False"
        false_bool_str7 = "F"
        # act
        gh = GarminHandler("gcf55_config.yml")
        # assert
        self.assertFalse(gh.str2bool(false_bool_str1))
        self.assertFalse(gh.str2bool(false_bool_str2))
        self.assertFalse(gh.str2bool(false_bool_str3))
        self.assertFalse(gh.str2bool(false_bool_str4))
        self.assertFalse(gh.str2bool(false_bool_str5))
        self.assertFalse(gh.str2bool(false_bool_str6))
        self.assertFalse(gh.str2bool(false_bool_str7))

    def test_parse_yyyy_mm_dd_not_str(self):
        """Test parse_yyyy_mm_dd throws a TypeError when passed a non-string"""
        # arrange
        not_str = 25
        # act
        # assert
        self.assertRaises(TypeError, GarminHandler.parse_yyyy_mm_dd, not_str)

    def test_parse_yyyy_mm_dd_valid_date(self):
        """Test parse_yyyy_mm_dd returns the correct datetime if passed a valid date string"""
        # arrange
        date_str = "2019-07-01"
        # act
        gh = GarminHandler("gcf55_config.yml")
        dt = gh.parse_yyyy_mm_dd(date_str)
        # assert
        self.assertTrue(isinstance(dt, datetime.datetime))

    # TODO check Throws error if passed a valid date string but not in the correct format

    def test_parse_yyyy_mm_dd_not_valid_date(self):
        """Test parse_yyyy_mm_dd returns None when passed a string that is not a valid data"""
        # arrange
        gibberish = "gibberish"
        # act
        gh = GarminHandler("gcf55_config.yml")
        # assert
        self.assertIsNone(gh.parse_yyyy_mm_dd(gibberish))

    # TODO test check_args

# run tests
if __name__ == '__main__':
    unittest.main(verbosity=2)
