import unittest
from JSONhandler import JSONhandler

class testURLhandler(unittest.TestCase):
    def SetUp(self):
        """set-up code, which is called before each test, to avoid repetition"""
        pass

    def tearDown(self):
        """code to tidy up after each test"""
        pass

    def test_creator(self):
        """Test that creator throws a ValueError for a non-string JSON filename"""
        print("@test_creator")
        # arrange
        json_fname = 10
        # act
        # assert
        self.assertRaises(ValueError, JSONhandler, json_fname)

    def test_read_json_not_exist_fname(self):
        """Checks that a JSON file that doesn't exist throws a FileNotFoundError"""
        print("@test_read_json_not_exist_fname")
        # arrange
        json_fname = "nonexist.json"
        # act
        jsonhndlr = JSONhandler(json_fname)
        # assert
        self.assertRaises(FileNotFoundError, jsonhndlr.read_json)

    def test_read_json_fname_directory(self):
        """Checks that a JSON file that is a directory throws a FileNotFoundError"""
        print("@test_read_json_fname_directory")
        # arrange
        json_fname = "D:/Document/"
        # act
        jsonhndlr = JSONhandler(json_fname)
        # assert
        self.assertRaises(FileNotFoundError, jsonhndlr.read_json)

    # TODO check when fname exists but is empty

    def test_read_json_exist_json(self):
        """Checks that a valid JSON file returns True when read"""
        print("@test_read_json_exist_json")
        # arrange
        json_fname = "skittles_config.json"
        # act
        jsonhndlr = JSONhandler(json_fname)
        # assert
        self.assertTrue(jsonhndlr.read_json())

    def test_read_json_key_not_str(self):
        """Checks that a non-string key raises a ValueError"""
        print("@test_read_json_key_not_str")
        # arrange
        json_fname = "skittles_config.json"
        key = 25
        # act
        jsonhndlr = JSONhandler(json_fname)
        # assert
        self.assertTrue(jsonhndlr.read_json())
        self.assertRaises(ValueError, jsonhndlr.get_val, key)

# run tests
if __name__ == '__main__':
    unittest.main(verbosity=2)
