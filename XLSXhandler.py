import sys
import os
import xlrd
import pandas as pd
import urllib.request
import requests
from URLhandler import URLhandler

class XLSXhandler:
    """Class for handling Excel files"""
    # members
    __fname = None        # name of the 'file' containing the Excel document
    __xlsx_data = None    # holds the Excel worksheets
    __raw_data = None     # raw data from Excel worksheet being processed
    __data = None         # data from worksheet to be processed
    __hdr_labels = None
    __totals = None
    __row_labels = None

    # constructor methods
    def __init__(self):
        pass

    def __init__(self, fname:str):
        """Constructor
        :param fanme: str
            name of the Excel file to be handled
        :raises ValueError: if fname is not a string or blank
        """
        if (isinstance(fname, str)):
            # check whether string is empty or blank
            if not(fname and fname.strip()):
                raise ValueError("@XLSXhandler creator: {} is blank".format(fname))
            else:
                # the name of the Excel file to be processed - can be a filename, full path, url etc.
                self.__fname = fname
        else:
            raise ValueError("@XLSXhandler creator: {} is not a string".format(fname))

    # destructor method
    def __del__(self):
        print("{} [{}] died".format(self.__class__.__name__, self.__fname))

    def get_xlsx_from_url(self):
        """Read an Excel workbook from a url and points to a valid Excel workbook
        contents of the workbook are loaded into the panda dataframe self.xlsx_data
        :return: bool
            is url is valid?
        """
        try:
            # create URLhandler
            urlhndlr = URLhandler(self.__fname)
        except ValueError as e:
            print("@XLSXhandler: ValueError - {}".format(e))
            return False
        # is the url valid?
        if urlhndlr.check_url():
            del urlhndlr    # delete as soon as no longer needed
            # open url
            try:
                socket = urllib.request.urlopen(self.__fname)
            except requests.exceptions.ConnectionError as e:
                print("@XLSXhandler.get_xlsx_from_url() Connection error for {}".format(self.__fname))
                self.__xlsx_data = None
                return False
            except:
                print("@XLSXhandler.get_xlsx_from_url() Unexpected error:", sys.exc_info()[0])
                self.__xlsx_data = None
                return False
            # get Excel workbook
            try:
                self.__xlsx_data = pd.ExcelFile(socket)
            except xlrd.biffh.XLRDError as e:
                print("@XLSXhandler.get_xlsx_from_url() Not an xlsx file: {}".format(self.__fname))
                self.__xlsx_data = None
                return False
            else:
                return True
        else:
            del urlhndlr
            print("@XLSXhandler.get_xlsx_from_url() URL doesn't exist: {}".format(self.__fname))
            self.__xlsx_data = None
            return False

    def get_xlsx_from_file(self):
        """Read an Excel workbook from a file and points to a valid Excel workbook
        contents of the workbook are loaded into the panda dataframe self.__xlsx_data
        :return: bool
            is file is valid?
        """
        if os.path.isdir(self.__fname):
            print("@XLSXhandler.get_xlsx_from_file() file is a directory: {}".format(self.__fname))
            return False
        try:
            self.__xlsx_data = pd.ExcelFile(self.__fname)
        except FileNotFoundError as e:
            print("@XLSXhandler.get_xlsx_from_file() file not found: {}".format(self.__fname))
            self.__xlsx_data = None
            return False
        except xlrd.biffh.XLRDError as e:
            print("@XLSXhandler.get_xlsx_from_file() Not an xlsx file: {}".format(self.__fname))
            self.__xlsx_data = None
            return False
        else:
            return True

    def get_sheet_names(self):
        """Return the sheet names
        :return: list
            list of sheet names
        """
        return self.__xlsx_data.sheet_names

    def are_extract_worksheet_data_params_valid(self, worksheet:str, hdr_row:int, total_row:int, start_row:int,
                                                end_row:int, num_cols:int):
        """Are the parameters for extract_worksheet_data() valid?
        :param worksheet: str
            name of the worksheet to process
        :param hdr_row: int
            row comtainer the data header/field names
        :param total_row: int
            row with totals, -1 if no totals row
        :param start_row: int
            first row containing data
        :param end_row: int
            last row containing data
        :param num_col: int
            number of data columns, column zero is assumed to contain row labels
        :raises ValueError: when a parameter has an invalid value
        :return: bool
            are all the parameters valid
        """
        if isinstance(worksheet, str):
            # check row id parameters: hdr_row, total_row, start_row, end_row
            attr_vals = [hdr_row, total_row, start_row, end_row, num_cols]
            attr_names = ["hdr_row", "total_row", "start_row", "end_row", "num_cols"]
            # check all the attributes are integer and positive (except total_row, which can be -1]
            for idx, val in enumerate(attr_vals):
                if not isinstance(attr_vals[idx], int):
                    raise ValueError(
                        "@extract_worksheet_data(): {} {} is not integer".format(attr_names[idx], attr_vals[idx]))
                if idx != 1 and attr_vals[idx] < 0:  # check values are non-negative
                    raise ValueError(
                        "@extract_worksheet_data(): {} {} is not positive".format(attr_names[idx], attr_vals[idx]))
                if idx == 1 and (attr_vals[idx] < -1 or attr_vals[idx] == 0):
                    raise ValueError(
                        "@extract_worksheet_data(): {} {} is an invalid value".format(attr_names[idx], attr_vals[idx]))
            if start_row > end_row:  # check start_row is before end_row
                raise ValueError(
                    "@extract_worksheet_data(): end_row {} is before start_row {}".format(end_row, start_row))
            if hdr_row == total_row:  # check hdr_row and total_row are not the same
                raise ValueError(
                    "@extract_worksheet_data(): hdr_row {} matches total_row {}".format(hdr_row, total_row))
            # check hdr_row does not lie in the range [start_row, end_row] are not the same
            if hdr_row >= start_row and hdr_row <= end_row:
                raise ValueError(
                    "@extract_worksheet_data(): hdr_row {} in range [start_row {}, end_row {}]".format(hdr_row,
                                                                                                       start_row,
                                                                                                       end_row))
            if total_row == start_row:  # check total_row and start_row are not the same
                raise ValueError(
                    "@extract_worksheet_data(): total_row {} matches start_row {}".format(total_row, start_row))
            if total_row == end_row:  # check total_row and end_row are not the same
                raise ValueError(
                    "@extract_worksheet_data(): total_row {} matches end_row {}".format(total_row, end_row))
        else:
            print("@XLSXhandler.extract_worksheet_data: {} is not a string".format(worksheet))
            raise ValueError("@XLSXhandler.extract_worksheet_data: {} is not a string".format(worksheet))
        return True

    def extract_worksheet_data(self, worksheet:str, hdr_row:int, total_row:int, start_row:int, end_row:int, num_cols:int):
        """Return the data contents of the worksheet as a ndarray
        :param worksheet: str
            name of the worksheet to process
        :param hdr_row: int
            row comtainer the data header/field names
        :param total_row: int
            row with totals, -1 if no totals row
        :param start_row: int
            first row containing data
        :param end_row: int
            last row containing data
        :param num_col: int
            number of data columns, column zero is assumed to contain row labels
        :raises ValueError: when a parameter has an invalid value
        """
        if self.are_extract_worksheet_data_params_valid(worksheet, hdr_row, total_row, start_row, end_row, num_cols):
            try:
                # check the worksheet exists
                if worksheet in self.__xlsx_data.sheet_names:
                    self.__raw_data = self.__xlsx_data.parse(worksheet, header=0, skiprows=hdr_row-1, index_col=0,
                                                             na_values='*', parse_cols=num_cols)
                    # account for skipped rows in row indices
                    hdr_row += 1    # +1 as row after the header row becomes row 0
                    [total_row, start_row, end_row] = map(lambda x: x - hdr_row, [total_row, start_row, end_row])
                    self.__hdr_labels = self.__raw_data.columns
                    # only read total row if one is defined
                    if total_row >= 0:
                        self.__totals = self.__raw_data.iloc[total_row, :].values
                    self.__row_labels = self.__raw_data.index.values[start_row:end_row]
                    self.__data = self.__raw_data.iloc[start_row:end_row, :].values
                else:
                    print("@XLSXhandler.extract_worksheet_data: worksheet {} is not in workbook".format(worksheet))
                    raise ValueError("@XLSXhandler.extract_worksheet_data: worksheet {} is not in workbook".format(worksheet))
            except AttributeError:
                print("@XLSXhandler.extract_worksheet_data(): attribute xlsx_data not defined")
                raise ValueError("@XLSXhandler.extract_worksheet_data(): attribute xlsx_data not defined")


    def get_row_labels(self):
        """Access method to value of __row_labels
        :return: list of str
            contents of __row_labels
        """
        return self.__row_labels

    def get_num_cols(self):
        """Access method to get number of columns in data
        :return: int
            number of columns in data"""
        return self.__data.shape[1]

    def get_num_rows(self):
        """Access method to get number of rows in data
        :return: int
            number of rows in data"""
        return self.__data.shape[0]

    def get_col_val(self, col_index:int):
        """Access method to column of data
        :param col_index : int
            index of column of data to return
        :return: list of float
            defined coliumn
        """
        # TODO check column index is valid
        assert(0 <= col_index <= self.get_num_cols())
        return self.__data[:, col_index]
