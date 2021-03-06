import pandas
import os

class JSONhandler:
    """Class for handling JSON"""
    __fname = None    # name of the JSON file
    __jsondf = None   # data frame for JSON file

    # constructor methods
    def __init__(self):
        pass

    def __init__(self, fname:str):
        """Constructor
        :param fname: str
            file name of the JSON file to be handled
        :raises ValueError: if fname is not a string
        """
        if isinstance(fname, str):
            self.__fname = fname
        else:
            raise ValueError("@URLhandler creator: {} is not a string".format(fname))

    # destructor method
    def __del__(self):
        print("{} [{}] died".format(self.__class__.__name__, self.__fname))

    def read_json(self):
        """method to read JSON file
        :return: bool
            is fname is a valid JSON file?
        :raises FileNotFoundError: if fname is not a valid or existing file
        """
        # check JSON file (fname) exists and is a file
        if not os.path.isfile(self.__fname):
            raise FileNotFoundError
        if os.path.isdir(self.__fname):
            raise FileNotFoundError
        self.__jsondf = pandas.read_json(self.__fname)
        # TODO check data frame contains data
        return True

    def get_val(self, key:str):
        """"get the value for a given key
        :param key: str
            key to be matched
        :raises ValueError: if key is not a string or is not valid
        :return: [type]
            the value for tha given key, type can vary
        """
        if not isinstance(key, str):
            raise ValueError("@JSONhandler.get_val({}) key is not a string".format(key))
        try:
            value = self.__jsondf[key][0]
        except KeyError as e:
            raise ValueError("@JSONhandler.get_val({}) key is not in JSON".format(key))
        return value