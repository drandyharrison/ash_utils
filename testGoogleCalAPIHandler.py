import unittest
from GoogleCalAPIHandler import GoogleCalAPIHandler


class testGoogleCalAPIHandler(unittest.TestCase):
    def SetUp(self):
        """set-up code, which is called before each test, to avoid repetition"""
        pass

    def tearDown(self):
        """code to tidy up after each test"""
        pass

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
        """Checks that add_event raises ValueError for invalid email address"""
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

    def test_add_event_email_valid(self):
        """Checks that add_event returns True for valid email address and valid event"""
        print("@test_add_event_email_invalid")
        # arrange
        email = "iam.andyharrison@gmail.com"
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
        self.assertTrue(calhndlr.add_event(email, event))

    def test_add_event_start_tz_invalid(self):
        """Checks that add_event returns False for invalid start tz"""
        print("@test_add_event_start_tz_invalid")
        # arrange
        email = "iam.andyharrison@gmail.com"
        event = {
            'summary': 'Skittles test',
            'location': 'Venue',
            'description': 'Home/Away (Opposition)',
            'start': {
                'dateTime': '2019-03-28T20:00:00',
                'timeZone': 'invalid',
            },
            'end': {
                'dateTime': '2019-03-28T23:00:00',
                'timeZone': 'Europe/London',
            },
        }
        # act
        calhndlr = GoogleCalAPIHandler()
        # assert
        self.assertFalse(calhndlr.add_event(email, event))

    def test_add_event_end_tz_invalid(self):
        """Checks that add_event returns False for invalid end tz"""
        print("@test_add_event_end_tz_invalid")
        # arrange
        email = "iam.andyharrison@gmail.com"
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
                'timeZone': 'invalid',
            },
        }
        # act
        calhndlr = GoogleCalAPIHandler()
        # assert
        self.assertFalse(calhndlr.add_event(email, event))

    def test_add_event_end_event_invalid(self):
        """Checks that add_event returns False for invalid event"""
        print("@test_add_event_end_event_invalid")
        # arrange
        email = "iam.andyharrison@gmail.com"
        event = {
            'summary': 'Skittles test',
            'location': 'Venue',
            'description': 'Home/Away (Opposition)',
            'start': {
                'dateTime': '2019-03-28T20:00:00',
                'timeZone': 'Europe/London',
            },
            'udder': {
                'dateTime': '2019-03-28T23:00:00',
                'timeZone': 'Europe/London',
            },
        }
        # act
        calhndlr = GoogleCalAPIHandler()
        # assert
        self.assertFalse(calhndlr.add_event(email, event))

    def test_are_add_event_params_valid_email_not_str(self):
        """Checks that are_add_event_params_valid raises TypeError for non-string email address"""
        print("@test_are_add_event_params_valid_email_not_str")
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
        self.assertRaises(TypeError, calhndlr.are_add_event_params_valid, email, event)

    def test_are_add_event_params_valid_email_invalid(self):
        """Checks that are_add_event_params_valid raises ValueError for invalid email address"""
        print("@test_are_add_event_params_valid_email_invalid")
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
        self.assertRaises(ValueError, calhndlr.are_add_event_params_valid, email, event)

    def test_are_add_event_params_valid_email_valid(self):
        """Checks that are_add_event_params_valid returns True for valid email address and valid event"""
        print("@test_are_add_event_params_valid_email_invalid")
        # arrange
        email = "iam.andyharrison@gmail.com"
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
        self.assertTrue(calhndlr.are_add_event_params_valid(email, event))

# run tests
if __name__ == '__main__':
    unittest.main(verbosity=2)
