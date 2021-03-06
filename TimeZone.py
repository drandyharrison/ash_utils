import csv
from ash_singleton import singleton

# add decorator to make a singleton class
@singleton
class TimeZone:
    """Class for storing and querying a list of time zones"""
    # TODO need to include a reference to the source
    # members
    __tzdata = "./zone1970.tab"   # file containing the list of time zones
    __zones = None                # list of valid time zones

    # constructor methods
    def __init__(self):
        """creator for read-only access"""
        # read in timezone database
        self.__zones = []
        try:
            for x in csv.reader(open(self.__tzdata, 'r'), delimiter='\t'):
                # skip the rows that start #
                if not x[0].startswith("#"):
                    if len(x) > 2:
                        self.__zones.append(x[2])
        except FileNotFoundError:
            print("@TimeZone: {} not found".format(self.__tzdata))
        except:
                print("@TimeZone Unexpected error:", sys.exc_info()[0])
        print("Read list of valid time zones: {}".format(len(self.__zones)))

    # destructor method
    def __del__(self):
        print("{} died".format(self.__class__.__name__))

    def is_tz_valid(self, tz : str):
        """Is the timezone valid
        :param tz: str
            timezone
        :raises TypeError: if timezone is not a string
        """
        # check tz is a string
        if not isinstance(tz, str):
            raise TypeError("@is_tz_valid({}) timezone is not a string".format(tz))
        # check the timezone is in the database
        return (tz in self.__zones)