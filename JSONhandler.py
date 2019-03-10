import pandas

class JSONhandler:
    """Class for handling JSON"""
    fname = None    # name of the JSON file

    # creator methods
    def __init__(self):
        pass

    def __init__(self, fname):
        if isinstance(fname, str):
            # the name of the URL to be processed
            self.fname = fname
        else:
            raise ValueError("@URLhandler creator: {} is not a string".format(fname))
