import sys
import xlrd
import pandas as pd
from urllib.request import urlopen
import requests
from URLhandler import URLhandler

class XLSXhandler:
    """Class for handling Excel files"""

    # creator methods
    def __init__(self):
        pass

    def __init__(self, fname):
        if (isinstance(fname, str)):
            # check whether string is empty or blank
            if not(fname and fname.strip()):
                raise ValueError("@XLSXhandler creator: {} is blank".format(fname))
            else:
                # the name of the Excel file to be processed - can be a filename, full path, url etc.
                self.fname = fname
        else:
            raise ValueError("@XLSXhandler creator: {} is not a string".format(fname))

    # Read an Excel workbook from a url and returns whether the url is valid and points to a valid Excel workbook
    # contents of the workbook are loaded into the panda dataframe self.xlsx_data
    def get_xlsx_from_url(self):
        try:
            # create URLhandler
            urlhndlr = URLhandler(self.fname)
        except ValueError as e:
            print("@XLSXhandler: ValueError - {}".format(e))
            return False
        # is the url valid?
        if urlhndlr.check_url():
            del urlhndlr    # delete as soon as no longer needed
            # open url
            try:
                socket = urlopen(self.fname)
            except requests.exceptions.ConnectionError as e:
                print("@XLSXhandler.get_xlsx_from_url() Connection error for {}".format(self.fname))
                self.xlsx_data = None
                return False
            except:
                print("@XLSXhandler.get_xlsx_from_url() Unexpected error:", sys.exc_info()[0])
                self.xlsx_data = None
                return False
            # get Excel workbook
            try:
                self.xlsx_data = pd.ExcelFile(socket)
            except xlrd.biffh.XLRDError as e:
                print("@XLSXhandler.get_xlsx_from_url() Not an xlsx file: {}".format(self.fname))
                self.xlsx_data = None
                return False
            else:
                return True
        else:
            del urlhndlr
            print("@XLSXhandler.get_xlsx_from_url() URL doesn't exist: {}".format(self.fname))
            self.xlsx_data = None
            return False

    def get_sheet_names(self):
        """Return the sheet names"""
        return self.xlsx_data.sheet_names

    def extract_worksheet_data(self, worksheet, hdr_row, total_row, start_row, end_row, num_cols):
        """Return the data contents of the worksheet as a ndarray

        worksheet -- name of the worksheet to process
        hdr_row - row comtainer the data header/field names
        total_row -- row with totals, -1 if no totals row
        start_row -- first row containing data
        end_row -- last row containing data
        num_col -- number of data columns, column zero is assumed to contain row labels"""
        if isinstance(worksheet, str):
            # check xlsx_data exists
            try:
                # check the worksheet exists
                if worksheet in self.xlsx_data.sheet_names:
                    self.raw_data = self.xlsx_data.parse(worksheet)
                    # rename the columns to contiguous integers, makes access easier
                    for idx, col in enumerate(self.raw_data.columns):
                        self.raw_data.rename(columns={col: idx}, inplace=True)
                    # check row id parameters: hdr_row, total_row, start_row, end_row
                    attr_vals = [hdr_row, total_row, start_row, end_row, num_cols]
                    attr_names = ["hdr_row", "total_row", "start_row", "end_row", "num_cols"]
                    # check all the attributes are integer and positive
                    for idx, val in enumerate(attr_vals):
                        if not isinstance(attr_vals[idx], int):
                            raise ValueError("@extract_worksheet_data(): {} {} is not integer".format(attr_names[idx], attr_vals[idx]))
                        if attr_vals[idx] <= 0:  # check hdr_row is positive
                            raise ValueError("@extract_worksheet_data(): {} {} is not positive".format(attr_names[idx], attr_vals[idx]))
                    if start_row > end_row:             # check start_row is before end_row
                        raise ValueError("@extract_worksheet_data(): end_row {} is before start_row {}".format(end_row, start_row))
                    if hdr_row == total_row:            # check hdr_row and total_row are not the same
                        raise ValueError("@extract_worksheet_data(): hdr_row {} matches total_row {}".format(hdr_row, total_row))
                    # check hdr_row does not lie in the range [start_row, end_row] are not the same
                    if hdr_row >= start_row and hdr_row <= end_row:
                        raise ValueError("@extract_worksheet_data(): hdr_row {} in range [start_row {}, end_row {}]".format(hdr_row, start_row. end_row))
                    if total_row == start_row:          # check total_row and start_row are not the same
                        raise ValueError("@extract_worksheet_data(): total_row {} matches start_row {}".format(total_row, start_row))
                    if total_row == end_row:            # check total_row and end_row are not the same
                        raise ValueError("@extract_worksheet_data(): total_row {} matches end_row {}".format(total_row, end_row))
                    # get data, labels and totals
                    self.hdr_labels = self.raw_data.loc[hdr_row, 1:num_cols]
                    if total_row > 0:
                        self.totals = self.raw_data.loc[total_row, 1:num_cols].values
                    self.row_labels = self.raw_data.loc[start_row:end_row, 0]
                    # self.data is a numpy.ndarray
                    self.data = self.raw_data.loc[start_row:end_row, 1:num_cols].values
                    # print(type(self.totals))
                else:
                    print("@XLSXhandler.extract_worksheet_data: worksheet {} is not in workbook".format(worksheet))
                    raise ValueError("@XLSXhandler.extract_worksheet_data: worksheet {} is not in workbook".format(worksheet))
            except AttributeError:
                print("@XLSXhandler.extract_worksheet_data(): attribute xlsx_data not defined")
                raise ValueError("@XLSXhandler.extract_worksheet_data(): attribute xlsx_data not defined")
        else:
            print("@XLSXhandler.extract_worksheet_data: {} is not a string".format(worksheet))
            raise ValueError("@XLSXhandler.extract_worksheet_data: {} is not a string".format(worksheet))
