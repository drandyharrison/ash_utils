import sys
import validators
from http.client import OK, FOUND, MOVED_PERMANENTLY
import requests

class URLhandler:
    """Class for handling urls"""
    url = None  # URL to be handled
    good_codes = [OK, FOUND, MOVED_PERMANENTLY]

    # constructor methods
    def __init__(self):
        pass

    def __init__(self, url:str):
        """Constructor
        :param url: url of the Excel workbook
        :raises ValueError: if url is not a string
        """
        if isinstance(url, str):
            # the name of the URL to be processed
            self.url = url
        else:
            raise ValueError("@URLhandler creator: {} is not a string".format(url))

    # destructor method
    def __del__(self):
        print("{} [{}] died".format(self.__class__.__name__, self.url))

    def check_url(self):
        """check if a URL exists without downloading the whole file. It only checks the URL header.
        :returne: whether url is valid
        """
        # check it's a valid url string
        if validators.url(self.url):
            # check url exists
            try:
                request = requests.get(self.url)
                if request.status_code in self.good_codes:
                    return True
                else:
                    print("@URLhanmdler.check_url() Website returned response code: {code}".format(code=request.status_code))
                    return False
            except requests.exceptions.ConnectionError as e:
                print('@URLhanmdler.check_url() Connection error for {}'.format(self.url))
                return False
            except:
                print("@URLhanmdler.check_url() Unexpected error:", sys.exc_info()[0])
                return False
        else:
            print("@URLhanmdler.check_url() Invalid url: {}".format(self.url))
            return False
