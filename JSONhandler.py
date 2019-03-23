import pandas
import os

class JSONhandler:
    """Class for handling JSON"""
    fname = None    # name of the JSON file
    jsondf = None   # data frame for JSON file

    # creator methods
    def __init__(self):
        pass

    def __init__(self, fname:str):
        if isinstance(fname, str):
            # the name of the URL to be processed
            self.fname = fname
        else:
            raise ValueError("@URLhandler creator: {} is not a string".format(fname))

    # method to read JSON file
    def read_json(self):
        # check JSON file (fname) exists and is a file
        if not os.path.isfile(self.fname):
            raise FileNotFoundError
        if os.path.isdir(self.fname):
            raise FileNotFoundError
        self.jsondf = pandas.read_json(self.fname)
        # TODO check data frame contains data
        return True

    # get the value for a given key
    def get_val(self, key:str):
        if not isinstance(key, str):
            raise ValueError("@JSONhandler.get_val({}) key is not a string".format(key))
        try:
            value = self.jsondf[key][0]
        except KeyError as e:
            raise ValueError("@JSONhandler.get_val({}) key is not in JSON".format(key))
        return value