from __future__ import print_function
import datetime
import dateutil.parser
import pickle
import os.path
import sys
import csv
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from validate_email import validate_email
from TimeZone import TimeZone

# define singleton decorator
def singleton(cls):
    """Singleton decorator"""
    instance = [None]
    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]
    return wrapper

# add decorator to make a singleton class
@singleton
class GoogleCalAPIHandler:
    """Class for handling the Google Calendar API"""
    # members
    # If modifying these scopes, delete the file token.pickle.
    #SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    creds = None
    service = None
    tzReader = TimeZone()

    # constructor methods
    def __init__(self, readonly : bool = True):
        """creator for read-only access"""
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                self.creds = flow.run_local_server()
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)
        self.service = build('calendar', 'v3', credentials=self.creds)

    # destructor method
    def __del__(self):
        print("{} died".format(self.__class__.__name__))

    # intro see https://developers.google.com/calendar/quickstart/python
    def get_next_n_appts(self, n : int):
        """Get the next n appointments from the calendar
        :param n: number of appointments to read from the calendar
        """
        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        print('Getting the upcoming {} events'.format(n))
        events_result = self.service.events().list(calendarId='primary', timeMin=now,
                                            maxResults=n, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
        for event in events:
            # extract the date string
            start_str = event['start'].get('dateTime', event['start'].get('date'))
            start_datetime = dateutil.parser.parse(start_str)
            start_date = start_datetime.date()
            print("[{}]: {}".format(start_date, event['summary']))

    # add event https://developers.google.com/calendar/create-events
    def add_event(self, email:str, event):
        """Add event to calendar
        :param email: email address for the calendar
        :param event: event to add to the calendar
        :returns: whether writing the appointment was successful
        """
        if not isinstance(email, str):
            raise TypeError("@add_event({}) email is not a string".format(email))
        if not validate_email(email):
            raise ValueError("@add_event({}) email is not a string".format(email))
        # no check as to whether email exists
        try:
            success = self.tzReader.is_tz_valid(event['start']['timeZone']) and\
                      self.tzReader.is_tz_valid(event['end']['timeZone'])
            if not success:
                print("Time zone invalid\n\tstart: {}\nend: {}".format(event['start']['timeZone'], event['end']['timeZone']))
        except:
            print("@GoogleCalAPIHandler Unexpected error:", sys.exc_info()[0])
            success = False
        if success:
            try:
                event = self.service.events().insert(calendarId=email, body=event).execute()
            except:
                print("@GoogleCalAPIHandler Unexpected error:", sys.exc_info()[0])
                success = False
            else:
                # print('Event created: {}'.format((event.get('htmlLink'))))
                success = True
        return success

