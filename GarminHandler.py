import os
import ast
import yaml
#import JSONhandler
from datetime import datetime
from pygce.models.bot import GarminConnectBot

class GarminHandler:
    """Class for connecting to Garmin Forerunner API"""
    # constants
    __AVAILABLE_OUTPUT_FORMATS = ["json", "csv"]
    # members
    __user = None
    __password = None
    __chromedriver = None
    __days = None
    __url = "https://connect.garmin.com/signin/"
    __out_dir = None
    __format_out = None
    __download_gpx = False

    # constructor methods
    def __init__(self, gcf55_config: str):
        if not(isinstance(gcf55_config, str)):
            raise TypeError("@creator: {} is not a string".format(gcf55_config))
        # read config from YAML
        with open(gcf55_config, 'r') as fstream:
            yaml_config = yaml.safe_load(fstream)
        # read key values from config file (and cast as necessary)
        self.__user = yaml_config['user']
        self.__password = yaml_config['password']
        self.__chromedriver = yaml_config['chromedriver']
        # ast.literal_eval() converts a string representation of a list into a list
        self.__days = ast.literal_eval(yaml_config['days'])
        assert (2 == len(self.__days))
        self.__days = [self.parse_yyyy_mm_dd(d) for d in self.__days]
        self.__url = yaml_config['url']
        self.__out_dir = yaml_config['out_dir']
        self.__format_out = yaml_config['format_out']
        self.__download_gpx = self.str2bool(yaml_config['download_gpx'])

    # destructor method
    def __del__(self):
        print("{} [{}] died".format(self.__class__.__name__, self.__user))

    def str2bool(self, v: str):
        """
        :param v: str
            boolean value
        :return: bool
            True if string holds a true value; otherwise False
        """
        if not(isinstance(v, str)):
            raise TypeError("@str2bool() {} is not a string".format(v))
        return v.lower() in ("yes", "true", "t", "1")


    def parse_yyyy_mm_dd(self, d):
        """
        :param d: str
            Date in the form yyyy-mm-dd to parse
        :return: datetime
            Date parsed
        """
        assert (isinstance(d, str))
        d = str(d).strip()  # discard jibberish
        return datetime.strptime(d, "%Y-%m-%d")

    # TODO remove clash between argument names and class members
    def check_args(self, user, password, url, chromedriver, days, out_dir):
        """
        :param user: str
            User to use
        :param password: str
            Password to use
        :param url: str
            Url to connect to
        :param chromedriver: str
            Path to chromedriver to use
        :param days: [] of datetime.date
            Days to save
        :param out_dir: str
            Directory to write to with output
        :return: bool
            True iff args are correct
        """
        assert (isinstance(user, str))
        assert (isinstance(password, str))
        assert (isinstance(url, str))
        assert (isinstance(chromedriver, str))
        assert (isinstance(out_dir, str))
        assert (len(user) > 1)
        assert (len(password) > 1)
        assert ("https" in url and "garmin" in url)
        assert (os.path.exists(chromedriver))
        assert (2 == len(days))
        assert (isinstance(days[0], datetime))
        assert (days[0] <= days[1])  # start day <= end day

        if not os.path.exists(out_dir):
            os.makedirs(out_dir)  # create necessary dir for output file

        return True

    def get_gc_data(self):
        """
        Read data from API
        :param user: str
            User to use
        :param password: str
            Password to use
        :param chromedriver: str
            Path to chromedriver to use
        :param days: [] of datetime.date
            Days to save
        :param url: str
            Url to connect to
        :param out_dir: str
            Directory to write to with output
        :param format_out: str
            Output format: JSON or CSV
        :param download_gpx: bool
            download GPX activities
        :return: bool
            True iff args are correct
        """

        if self.check_args(self.__user, self.__password, self.__url, self.__chromedriver, self.__days, self.__out_dir):
            bot = GarminConnectBot(self.__user, self.__password, self.__download_gpx, self.__chromedriver,
                                   url=self.__url)

            arg_tuple = self.__user, self.__password, self.__url, self.__chromedriver, self.__days, self.__download_gpx,\
                        self.__out_dir
            try:
                if self.__format_out == "json":
                    bot.save_json_days(self.__days[0], self.__days[1], arg_tuple)
                elif self.__format_out == "csv":
                    bot.save_csv_days(self.__days[0], self.__days[1], arg_tuple)

            except Exception as e:
                raise e
            finally:
                bot.close()
        else:
            print("Error while parsing args.")