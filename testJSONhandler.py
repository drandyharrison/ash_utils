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

# run tests
if __name__ == '__main__':
    unittest.main(verbosity=2)
