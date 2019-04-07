import pandas
import os

class JSONhandler:
    """Class for handling JSON"""
    fname = None    # name of the JSON file
    jsondf = None   # data frame for JSON file

    # constructor methods
    def __init__(self):
        pass

    def __init__(self, fname:str):
        """Constructor
        :param fname: file name of the JSON file to be handled
        :raises ValueError: if fname is not a string
        """
        if isinstance(fname, str):
            # the name of the URL to be processed
            self.fname = fname
        else:
            raise ValueError("@URLhandler creator: {} is not a string".format(fname))

    # destructor method
    def __del__(self):
        print("{} [{}] died".format(self.__class__.__name__, self.fname))

    def read_json(self):
        """method to read JSON file
        :returns: whether fname is a valid JSON file
        :raises FileNotFoundError: if fname is not a valid or existing file
        """
        # check JSON file (fname) exists and is a file
        if not os.path.isfile(self.fname):
            raise FileNotFoundError
        if os.path.isdir(self.fname):
            raise FileNotFoundError
        self.jsondf = pandas.read_json(self.fname)
        # TODO check data frame contains data
        return True

    def get_val(self, key:str):
        """"get the value for a given key
        :param key: key to be matched
        :raises ValueError: if key is not a string or is not valid
        """
        if not isinstance(key, str):
            raise ValueError("@JSONhandler.get_val({}) key is not a string".format(key))
        try:
            value = self.jsondf[key][0]
        except KeyError as e:
            raise ValueError("@JSONhandler.get_val({}) key is not in JSON".format(key))
        return value