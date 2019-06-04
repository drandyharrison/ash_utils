import os
import ast
import JSONhandler
from datetime import datetime
from pygce.models.bot import GarminConnectBot

class GarminHandler:
    """Class for connecting to Garmin Forerunner API"""
    # members
    AVAILABLE_OUTPUT_FORMATS = ["json", "csv"]
    user = None
    password = None
    chromedriver = None
    days = None
    url = "https://connect.garmin.com/signin/"
    out_dir = None
    format_out = None
    download_gpx = False

    # constructor methods
    def __init__(self, gcf55_config: str):
        # read config from a JSON
        jsonhndlr = ash_utils.JSONhandler(gcf55_config)
        if jsonhndlr.read_json():
            # read key values from config file (and cast as necessary)
            self.user = jsonhndlr.get_val('user')
            self.password = jsonhndlr.get_val('password')
            self.chromedriver = jsonhndlr.get_val('chromedriver')
            # ast.literal_eval() converts a string representation of a list into a list
            self.days = ast.literal_eval(jsonhndlr.get_val('days'))
            assert (2 == len(days))
            self.days = list(map(parse_yyyy_mm_dd, days))
            self.url = jsonhndlr.get_val('url')
            self.out_dir = jsonhndlr.get_val('out_dir')
            self.format_out = jsonhndlr.get_val('format_out')
            # convert to bool
            self.download_gpx = str2bool(jsonhndlr.get_val('download_gpx'))

    # destructor method
    def __del__(self):
        print("{} [{}] died".format(self.__class__.__name__, self.fname))

    def str2bool(v: str):
        """
        :param v: str
            boolean value
        :return: bool
            True if string holds a true value; otherwise False
        """
        assert(isinstance(v, str))
        return v.lower() in ("yes", "true", "t", "1")


    def parse_yyyy_mm_dd(d):
        """
        :param d: str
            Date in the form yyyy-mm-dd to parse
        :return: datetime
            Date parsed
        """

        d = str(d).strip()  # discard jibberish
        return datetime.strptime(d, "%Y-%m-%d")


    def check_args(user, password, url, chromedriver, days, out_dir):
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


    def get_gc_data():
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

        if check_args(self.user, self.password, self.url, self.chromedriver, self.days, self.out_dir):
            bot = GarminConnectBot(self.user, self.password, self.download_gpx, self.chromedriver, url=self.url)

            arg_tuple = self.user, self.password, self.url, self.chromedriver, self.days, self.download_gpx, self.out_dir
            try:
                if self.format_out == "json":
                    bot.save_json_days(self.days[0], self.days[1], arg_tuple)
                elif self.format_out == "csv":
                    bot.save_csv_days(self.days[0], self.days[1], arg_tuple)

            except Exception as e:
                raise e
            finally:
                bot.close()
        else:
            print("Error while parsing args.")