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

    def test_add_event_email_not_str(self):
        """Checks that add_event raises TypeError for non-string email address"""
        print("@test_add_event_email_not_str")
        # arrange
        email = 25
        event = {
            'summary': 'Skittles test',
            'location': 'Venue',
            'description': 'Home/Away (Opposition)',
            'start': {
                'dateTime': '2019-03-28T20:00:00',
                'timeZone': 'Europe/London',
            },
            'end': {
                'dateTime': '2019-03-28T23:00:00',
                'timeZone': 'Europe/London',
            },
        }
        # act
        calhndlr = GoogleCalAPIHandler()
        # assert
        self.assertRaises(TypeError, calhndlr.add_event, email, event)

    def test_add_event_email_invalid(self):
        """Checks that add_event raises TypeError for invalid email address"""
        print("@test_add_event_email_invalid")
        # arrange
        email = "invalid email"
        event = {
            'summary': 'Skittles test',
            'location': 'Venue',
            'description': 'Home/Away (Opposition)',
            'start': {
                'dateTime': '2019-03-28T20:00:00',
                'timeZone': 'Europe/London',
            },
            'end': {
                'dateTime': '2019-03-28T23:00:00',
                'timeZone': 'Europe/London',
            },
        }
        # act
        calhndlr = GoogleCalAPIHandler()
        # assert
        self.assertRaises(ValueError, calhndlr.add_event, email, event)

# run tests
if __name__ == '__main__':
    unittest.main(verbosity=2)
