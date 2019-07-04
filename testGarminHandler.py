import unittest
from GarminHandler import GarminHandler
import datetime
import ast

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
        # # TODO
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
        # assert
        self.assertTrue(isinstance(gh.parse_yyyy_mm_dd(date_str), datetime.datetime))

    def test_parse_yyyy_mm_dd_invalid_date_format(self):
        """Test parse_yyyy_mm_dd returns None if passed a valid date string but not in the expected format"""
        # arrange
        date_str = "01/07/2019"
        # act
        gh = GarminHandler("gcf55_config.yml")
        # assert
        self.assertIsNone(gh.parse_yyyy_mm_dd(date_str))

    def test_parse_yyyy_mm_dd_not_valid_date(self):
        """Test parse_yyyy_mm_dd returns None when passed a string that is not a valid data"""
        # arrange
        gibberish = "gibberish"
        # act
        gh = GarminHandler("gcf55_config.yml")
        # assert
        self.assertIsNone(gh.parse_yyyy_mm_dd(gibberish))

    def test_check_args_user_not_str(self):
        """Test check_args throws AssertionError when argument user is not a string"""
        # arrange
        user = 25.6
        password = "password"
        chromedriver = "C:/Users/iaman/AppData/Local/Programs/Python/Python37/chromedriver-Windows"
        days = ast.literal_eval("['2019-04-14', '2019-04-14']")
        url = "https://connect.garmin.com/signin/"
        out_dir = "./mygarmin//"
        format_out = "csv"
        download_gpx = False
        # act
        gh = GarminHandler("gcf55_config.yml")
        days = [gh.parse_yyyy_mm_dd(d) for d in days]
        # assert
        self.assertRaises(AssertionError, gh.check_args, user, password, url, chromedriver, days, out_dir)

    def test_check_args_password_not_str(self):
        """Test check_args throws AssertionError when argument password is not a string"""
        # arrange
        user = "name@domain.com"
        password = 12.3
        chromedriver = "C:/Users/iaman/AppData/Local/Programs/Python/Python37/chromedriver-Windows"
        days = ast.literal_eval("['2019-04-14', '2019-04-14']")
        url = "https://connect.garmin.com/signin/"
        out_dir = "./mygarmin//"
        format_out = "csv"
        download_gpx = False
        # act
        gh = GarminHandler("gcf55_config.yml")
        days = [gh.parse_yyyy_mm_dd(d) for d in days]
        # assert
        self.assertRaises(AssertionError, gh.check_args, user, password, url, chromedriver, days, out_dir)

    def test_check_args_url_not_str(self):
        """Test check_args throws AssertionError when argument url is not a string"""
        # arrange
        user = "name@domain.com"
        password = "password"
        chromedriver = "C:/Users/iaman/AppData/Local/Programs/Python/Python37/chromedriver-Windows"
        days = ast.literal_eval("['2019-04-14', '2019-04-14']")
        url = 35
        out_dir = "./mygarmin//"
        format_out = "csv"
        download_gpx = False
        # act
        gh = GarminHandler("gcf55_config.yml")
        days = [gh.parse_yyyy_mm_dd(d) for d in days]
        # assert
        self.assertRaises(AssertionError, gh.check_args, user, password, url, chromedriver, days, out_dir)

    def test_check_args_chromedriver_not_str(self):
        """Test check_args throws AssertionError when argument chromedriver is not a string"""
        # arrange
        user = "name@domain.com"
        password = "password"
        chromedriver = 35
        days = ast.literal_eval("['2019-04-14', '2019-04-14']")
        url = "https://connect.garmin.com/signin/"
        out_dir = "./mygarmin//"
        format_out = "csv"
        download_gpx = False
        # act
        gh = GarminHandler("gcf55_config.yml")
        days = [gh.parse_yyyy_mm_dd(d) for d in days]
        # assert
        self.assertRaises(AssertionError, gh.check_args, user, password, url, chromedriver, days, out_dir)

    def test_check_args_out_dir_not_str(self):
        """Test check_args throws AssertionError when argument out_dir is not a string"""
        # arrange
        user = "name@domain.com"
        password = "password"
        chromedriver = "C:/Users/iaman/AppData/Local/Programs/Python/Python37/chromedriver-Windows"
        days = ast.literal_eval("['2019-04-14', '2019-04-14']")
        url = "https://connect.garmin.com/signin/"
        out_dir = 84.235
        format_out = "csv"
        download_gpx = False
        # act
        gh = GarminHandler("gcf55_config.yml")
        days = [gh.parse_yyyy_mm_dd(d) for d in days]
        # assert
        self.assertRaises(AssertionError, gh.check_args, user, password, url, chromedriver, days, out_dir)

    def test_check_args_user_empty(self):
        """Test check_args throws AssertionError when argument user is empty"""
        # arrange
        user = ""
        password = "password"
        chromedriver = "C:/Users/iaman/AppData/Local/Programs/Python/Python37/chromedriver-Windows"
        days = ast.literal_eval("['2019-04-14', '2019-04-14']")
        url = "https://connect.garmin.com/signin/"
        out_dir = "./mygarmin//"
        format_out = "csv"
        download_gpx = False
        # act
        gh = GarminHandler("gcf55_config.yml")
        days = [gh.parse_yyyy_mm_dd(d) for d in days]
        # assert
        self.assertRaises(AssertionError, gh.check_args, user, password, url, chromedriver, days, out_dir)

    def test_check_args_password_empty(self):
        """Test check_args throws AssertionError when argument password is empty"""
        # arrange
        user = "name@domain.com"
        password = ""
        chromedriver = "C:/Users/iaman/AppData/Local/Programs/Python/Python37/chromedriver-Windows"
        days = ast.literal_eval("['2019-04-14', '2019-04-14']")
        url = "https://connect.garmin.com/signin/"
        out_dir = "./mygarmin//"
        format_out = "csv"
        download_gpx = False
        # act
        gh = GarminHandler("gcf55_config.yml")
        days = [gh.parse_yyyy_mm_dd(d) for d in days]
        # assert
        self.assertRaises(AssertionError, gh.check_args, user, password, url, chromedriver, days, out_dir)

    def test_check_args_url_invalid(self):
        """Test check_args throws AssertionError when argument url is invalid"""
        # arrange
        user = "name@domain.com"
        password = "password"
        chromedriver = "C:/Users/iaman/AppData/Local/Programs/Python/Python37/chromedriver-Windows"
        days = ast.literal_eval("['2019-04-14', '2019-04-14']")
        # "https" not in url and "garmin" not in url
        url1 = "http://connect.xxx.com/signin/"
        # "https" not in url and "garmin" in url
        url2 = "http://connect.garmin.com/signin/"
        # "https" in url and "garmin" not in url
        url3 = "https://connect.xxx.com/signin/"
        # TODO invalid url; e.g "htp:/ccc.dd.ee/"
        out_dir = "./mygarmin//"
        format_out = "csv"
        download_gpx = False
        # act
        gh = GarminHandler("gcf55_config.yml")
        days = [gh.parse_yyyy_mm_dd(d) for d in days]
        # assert
        self.assertRaises(AssertionError, gh.check_args, user, password, url1, chromedriver, days, out_dir)
        self.assertRaises(AssertionError, gh.check_args, user, password, url2, chromedriver, days, out_dir)
        self.assertRaises(AssertionError, gh.check_args, user, password, url3, chromedriver, days, out_dir)

    # TODO chromedriver path does not exist
    def test_check_args_chromedriver_path_invalid(self):
        """Test check_args throws AssertionError when argument chromedriver is an invalid"""
        # arrange
        user = "name@domain.com"
        password = "password"
        chromedriver = "C:/Users/me/AppData/Local/Programs/Python/Python37/chromedriver-Windows"
        days = ast.literal_eval("['2019-04-14', '2019-04-14']")
        url = "https://connect.garmin.com/signin/"
        out_dir = "./mygarmin//"
        format_out = "csv"
        download_gpx = False
        # act
        gh = GarminHandler("gcf55_config.yml")
        days = [gh.parse_yyyy_mm_dd(d) for d in days]
        # assert
        self.assertRaises(AssertionError, gh.check_args, user, password, url, chromedriver, days, out_dir)

    def test_check_args_not_two_days(self):
        """Test check_args throws AssertionError when argument days has more than two days"""
        # arrange
        user = "name@domain.com"
        password = "password"
        chromedriver = "C:/Users/iaman/AppData/Local/Programs/Python/Python37/chromedriver-Windows"
        days = ast.literal_eval("['2019-04-14', '2019-04-14', '2019-05-12']")
        url = "https://connect.garmin.com/signin/"
        out_dir = "./mygarmin//"
        format_out = "csv"
        download_gpx = False
        # act
        gh = GarminHandler("gcf55_config.yml")
        days = [gh.parse_yyyy_mm_dd(d) for d in days]
        # assert
        self.assertRaises(AssertionError, gh.check_args, user, password, url, chromedriver, days, out_dir)

    def test_check_args_days_not_datetime(self):
        """Test check_args throws AssertionError when argument days is not a list of valid datetime value strings"""
        # arrange
        user = "name@domain.com"
        password = "password"
        chromedriver = "C:/Users/iaman/AppData/Local/Programs/Python/Python37/chromedriver-Windows"
        days1 = ast.literal_eval("['19-04-14', '2019-04-14']")
        days2 = ast.literal_eval("['2019-04-14', '2019-04-34']")
        url = "https://connect.garmin.com/signin/"
        out_dir = "./mygarmin//"
        format_out = "csv"
        download_gpx = False
        # act
        gh = GarminHandler("gcf55_config.yml")
        days1 = [gh.parse_yyyy_mm_dd(d) for d in days1]
        days2 = [gh.parse_yyyy_mm_dd(d) for d in days2]
        # assert
        self.assertRaises(AssertionError, gh.check_args, user, password, url, chromedriver, days1, out_dir)
        self.assertRaises(AssertionError, gh.check_args, user, password, url, chromedriver, days2, out_dir)

    def test_check_args_days_not_seq(self):
        """Test check_args XXX"""
        # arrange
        user = "name@domain.com"
        password = "password"
        chromedriver = "C:/Users/iaman/AppData/Local/Programs/Python/Python37/chromedriver-Windows"
        days = ast.literal_eval("['2019-04-24', '2019-04-14']")
        url = "https://connect.garmin.com/signin/"
        out_dir = "./mygarmin//"
        format_out = "csv"
        download_gpx = False
        # act
        gh = GarminHandler("gcf55_config.yml")
        days = [gh.parse_yyyy_mm_dd(d) for d in days]
        # assert
        self.assertRaises(AssertionError, gh.check_args, user, password, url, chromedriver, days, out_dir)

    def test_check_args_all_valid(self):
        """Test check_args returns true when all arguments are valid"""
        # arrange
        user = "name@domain.com"
        password = "password"
        chromedriver = "C:/Users/iaman/AppData/Local/Programs/Python/Python37/chromedriver-Windows"
        days = ast.literal_eval("['2019-04-14', '2019-04-14']")
        url = "https://connect.garmin.com/signin/"
        out_dir = "./mygarmin//"
        format_out = "csv"
        download_gpx = False
        # act
        gh = GarminHandler("gcf55_config.yml")
        days = [gh.parse_yyyy_mm_dd(d) for d in days]
        # assert
        self.assertTrue(gh.check_args(user, password, url, chromedriver, days, out_dir))

# run tests
if __name__ == '__main__':
    unittest.main(verbosity=2)
