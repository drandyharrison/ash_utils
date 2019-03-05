import unittest
from XLSXhandler import XLSXhandler


class testXLSXhandler(unittest.TestCase):
    def SetUp(self):
        """set-up code, which is called before each test, to avoid repetition"""
        pass

    def tearDown(self):
        """code to tidy up after each test"""
        pass

    def test_creator_non_string(self):
        """Test that creator throws a ValueError for a non-string url"""
        print("@test_creator_non_string")
        # arrange
        url_int = 25
        # act
        # assert
        self.assertRaises(ValueError, XLSXhandler, url_int)

    def test_creator_blank(self):
        """check the creator throws expected error when passed a blank string"""
        print("@test_creator_blank")
        # arrange
        url_str = "   "
        # act
        # assert
        self.assertRaises(ValueError, XLSXhandler, url_str)

    def test_creator_empty(self):
        """check the creator throws expected error when passed an empty string"""
        print("@test_creator_empty")
        # arrange
        url_str = ""
        # act
        # assert
        self.assertRaises(ValueError, XLSXhandler, url_str)

    def test_get_xlsx_from_url_invalid_url(self):
        """Checks that a badly url returns False when checked"""
        print("@test_get_xlsx_from_url_invalid_url")
        # arrange
        url_str = "google"
        # act
        xlsx = XLSXhandler(url_str)
        # assert
        self.assertFalse(xlsx.get_xlsx_from_url())

    def test_get_xlsx_from_url_non_exist_url(self):
        """Checks that a well formed url that doesn't exist returns False when checked"""
        print("@test_get_xlsx_from_url_non_exist_url")
        # arrange
        url_str = "https://www.shddf.xx.xx"
        # act
        xlsx = XLSXhandler(url_str)
        # assert
        self.assertFalse(xlsx.get_xlsx_from_url())

    def test_get_xlsx_from_url_exist_not_xlsx(self):
        """Checks that a valid url that's not an Excel returns False when checked"""
        print("@test_get_xlsx_from_url_exist_not_xlsx")
        # arrange
        url_str = "https://www.google.co.uk"
        # act
        xlsx = XLSXhandler(url_str)
        # assert
        self.assertFalse(xlsx.get_xlsx_from_url())

    def test_get_xlsx_from_url_exist_is_xlsx(self):
        """Checks that a valid url that's an Excel returns True when checked"""
        print("@test_get_xlsx_from_url_exist_is_xlsx")
        # arrange
        url_str = "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx"
        # act
        xlsx = XLSXhandler(url_str)
        # assert
        self.assertTrue(xlsx.get_xlsx_from_url())

    def test_extract_worksheet_data_not_string(self):
        """Check extract_worksheet_data throws a ValueError for a non-string worksheet name"""
        print("@test_extract_worksheet_data_not_string")
        # arrange
        url_str = "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx"
        worksheet = 25
        hdr_row = 1
        total_row = 1
        start_row = 1
        end_row = 1
        num_cols = 5
        # act
        xlsx = XLSXhandler(url_str)
        # assert
        self.assertRaises(ValueError, xlsx.extract_worksheet_data, worksheet, hdr_row, total_row, start_row, end_row,
                          num_cols)

    def test_extract_worksheet_data_not_in_workbook(self):
        """Check extract_worksheet_data throws a ValueError if worksheet not in workbook"""
        print("@test_extract_worksheet_data_not_in_workbook")
        # arrange
        url_str = "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx"
        worksheet = "nil"
        hdr_row = 1
        total_row = 2
        start_row = 3
        end_row = 3
        num_cols = 5
        # act
        xlsx = XLSXhandler(url_str)
        xlsx.get_xlsx_from_url()
        # assert
        self.assertRaises(ValueError, xlsx.extract_worksheet_data, worksheet, hdr_row, total_row, start_row, end_row,
                          num_cols)

    def test_extract_worksheet_data_no_workbook(self):
        """Check extract_worksheet_data throws a ValueError if workbook hasn't been loaded"""
        print("@test_extract_worksheet_data_not_in_workbook")
        # arrange
        url_str = "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx"
        worksheet = "1A"
        hdr_row = 1
        total_row = 2
        start_row = 3
        end_row = 3
        num_cols = 5
        # act
        xlsx = XLSXhandler(url_str)
        # assert
        self.assertRaises(ValueError, xlsx.extract_worksheet_data, worksheet, hdr_row, total_row, start_row, end_row,
                          num_cols)

    def test_extract_worksheet_data_hdr_row_not_int(self):
        """Check extract_worksheet_data throws a ValueError if hdr_row is not an integer"""
        print("@test_extract_worksheet_data_hdr_row_not_int")
        # arrange
        url_str = "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx"
        worksheet = "1A"
        hdr_row = "X"
        total_row = 2
        start_row = 3
        end_row = 3
        num_cols = 5
        # act
        xlsx = XLSXhandler(url_str)
        xlsx.get_xlsx_from_url()
        # assert
        self.assertRaises(ValueError, xlsx.extract_worksheet_data, worksheet, hdr_row, total_row, start_row, end_row,
                          num_cols)

    def test_extract_worksheet_data_total_row_not_int(self):
        """Check extract_worksheet_data throws a ValueError if total_row is not an integer"""
        print("@test_extract_worksheet_data_total_row_not_int")
        # arrange
        url_str = "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx"
        worksheet = "1A"
        hdr_row = 1
        total_row = "X"
        start_row = 3
        end_row = 3
        num_cols = 5
        # act
        xlsx = XLSXhandler(url_str)
        xlsx.get_xlsx_from_url()
        # assert
        self.assertRaises(ValueError, xlsx.extract_worksheet_data, worksheet, hdr_row, total_row, start_row, end_row,
                          num_cols)

    def test_extract_worksheet_data_start_row_not_int(self):
        """Check extract_worksheet_data throws a ValueError if start_row is not an integer"""
        print("@test_extract_worksheet_data_start_row_not_int")
        # arrange
        url_str = "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx"
        worksheet = "1A"
        hdr_row = 1
        total_row = 2
        start_row = "X"
        end_row = 3
        num_cols = 5
        # act
        xlsx = XLSXhandler(url_str)
        xlsx.get_xlsx_from_url()
        # assert
        self.assertRaises(ValueError, xlsx.extract_worksheet_data, worksheet, hdr_row, total_row, start_row, end_row,
                          num_cols)

    def test_extract_worksheet_data_end_row_not_int(self):
        """Check extract_worksheet_data throws a ValueError if end_row is not an integer"""
        print("@test_extract_worksheet_data_end_row_not_int")
        # arrange
        url_str = "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx"
        worksheet = "1A"
        hdr_row = 1
        total_row = 2
        start_row = 3
        end_row = "X"
        num_cols = 5
        # act
        xlsx = XLSXhandler(url_str)
        xlsx.get_xlsx_from_url()
        # assert
        self.assertRaises(ValueError, xlsx.extract_worksheet_data, worksheet, hdr_row, total_row, start_row, end_row,
                          num_cols)

    def test_extract_worksheet_data_hdr_row_not_pos(self):
        """Check extract_worksheet_data throws a ValueError if hdr_row is not positive"""
        print("@test_extract_worksheet_data_hdr_row_not_pos")
        # arrange
        url_str = "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx"
        worksheet = "1A"
        hdr_row = 0
        total_row = 2
        start_row = 3
        end_row = 3
        num_cols = 5
        # act
        xlsx = XLSXhandler(url_str)
        xlsx.get_xlsx_from_url()
        # assert
        self.assertRaises(ValueError, xlsx.extract_worksheet_data, worksheet, hdr_row, total_row, start_row, end_row,
                          num_cols)

    def test_extract_worksheet_data_total_row_not_pos(self):
        """Check extract_worksheet_data throws a ValueError if total_row is not positive"""
        print("@test_extract_worksheet_data_total_row_not_pos")
        # arrange
        url_str = "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx"
        worksheet = "1A"
        hdr_row = 1
        total_row = 0
        start_row = 3
        end_row = 3
        num_cols = 5
        # act
        xlsx = XLSXhandler(url_str)
        xlsx.get_xlsx_from_url()
        # assert
        self.assertRaises(ValueError, xlsx.extract_worksheet_data, worksheet, hdr_row, total_row, start_row, end_row,
                          num_cols)

    def test_extract_worksheet_data_start_row_not_pos(self):
        """Check extract_worksheet_data throws a ValueError if start_row is not positive"""
        print("@test_extract_worksheet_data_start_row_not_pos")
        # arrange
        url_str = "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx"
        worksheet = "1A"
        hdr_row = 1
        total_row = 2
        start_row = 0
        end_row = 3
        num_cols = 5
        # act
        xlsx = XLSXhandler(url_str)
        xlsx.get_xlsx_from_url()
        # assert
        self.assertRaises(ValueError, xlsx.extract_worksheet_data, worksheet, hdr_row, total_row, start_row, end_row,
                          num_cols)

    def test_extract_worksheet_data_end_row_not_pos(self):
        """Check extract_worksheet_data throws a ValueError if end_row is not positive"""
        print("@test_extract_worksheet_data_end_row_not_pos")
        # arrange
        url_str = "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx"
        worksheet = "1A"
        hdr_row = 1
        total_row = 2
        start_row = 3
        end_row = 0
        num_cols = 5
        # act
        xlsx = XLSXhandler(url_str)
        xlsx.get_xlsx_from_url()
        # assert
        self.assertRaises(ValueError, xlsx.extract_worksheet_data, worksheet, hdr_row, total_row, start_row, end_row,
                          num_cols)

    def test_extract_worksheet_data_num_cols_not_pos(self):
        """Check extract_worksheet_data throws a ValueError if num_cols is not positive"""
        print("@test_extract_worksheet_data_end_row_not_pos")
        # arrange
        url_str = "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx"
        worksheet = "1A"
        hdr_row = 1
        total_row = 2
        start_row = 3
        end_row = 5
        num_cols = 0
        # act
        xlsx = XLSXhandler(url_str)
        xlsx.get_xlsx_from_url()
        # assert
        self.assertRaises(ValueError, xlsx.extract_worksheet_data, worksheet, hdr_row, total_row, start_row, end_row,
                          num_cols)

    def test_extract_worksheet_data_start_after_end_row(self):
        """Check extract_worksheet_data throws a ValueError if start_row is after end_row"""
        print("@test_extract_worksheet_data_start_after_end_row")
        # arrange
        url_str = "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx"
        worksheet = "1A"
        hdr_row = 1
        total_row = 2
        start_row = 4
        end_row = 3
        num_cols = 5
        # act
        xlsx = XLSXhandler(url_str)
        xlsx.get_xlsx_from_url()
        # assert
        self.assertRaises(ValueError, xlsx.extract_worksheet_data, worksheet, hdr_row, total_row, start_row, end_row,
                          num_cols)

    def test_extract_worksheet_data_hdr_equals_total_row(self):
        """Check extract_worksheet_data throws a ValueError if hdr_row equals total_row"""
        print("@test_extract_worksheet_data_hdr_equals_total_row")
        # arrange
        url_str = "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx"
        worksheet = "1A"
        hdr_row = 1
        total_row = 1
        start_row = 3
        end_row = 3
        num_cols = 5
        # act
        xlsx = XLSXhandler(url_str)
        xlsx.get_xlsx_from_url()
        # assert
        self.assertRaises(ValueError, xlsx.extract_worksheet_data, worksheet, hdr_row, total_row, start_row, end_row,
                          num_cols)

    def test_extract_worksheet_data_hdr_equals_start_row(self):
        """Check extract_worksheet_data throws a ValueError if hdr_row equals start_row"""
        print("@test_extract_worksheet_data_hdr_equals_start_row")
        # arrange
        url_str = "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx"
        worksheet = "1A"
        hdr_row = 1
        total_row = 2
        start_row = 1
        end_row = 3
        num_cols = 5
        # act
        xlsx = XLSXhandler(url_str)
        xlsx.get_xlsx_from_url()
        # assert
        self.assertRaises(ValueError, xlsx.extract_worksheet_data, worksheet, hdr_row, total_row, start_row, end_row,
                          num_cols)

    def test_extract_worksheet_data_hdr_equals_end_row(self):
        """Check extract_worksheet_data throws a ValueError if hdr_row equals end_row"""
        print("@test_extract_worksheet_data_hdr_equals_end_row")
        # arrange
        url_str = "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx"
        worksheet = "1A"
        hdr_row = 3
        total_row = 2
        start_row = 1
        end_row = 3
        num_cols = 5
        # act
        xlsx = XLSXhandler(url_str)
        xlsx.get_xlsx_from_url()
        # assert
        self.assertRaises(ValueError, xlsx.extract_worksheet_data, worksheet, hdr_row, total_row, start_row, end_row,
                          num_cols)

    def test_extract_worksheet_data_hdr_between_start_and_end_row(self):
        """Check extract_worksheet_data throws a ValueError if hdr_row is between start_row and end_row"""
        print("@test_extract_worksheet_data_hdr_equals_end_row")
        # arrange
        url_str = "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx"
        worksheet = "1A"
        hdr_row = 3
        total_row = 2
        start_row = 1
        end_row = 5
        num_cols = 5
        # act
        xlsx = XLSXhandler(url_str)
        xlsx.get_xlsx_from_url()
        # assert
        self.assertRaises(ValueError, xlsx.extract_worksheet_data, worksheet, hdr_row, total_row, start_row, end_row,
                          num_cols)

    def test_extract_worksheet_data_total_equals_start_row(self):
        """Check extract_worksheet_data throws a ValueError if total_row equals start_row"""
        print("@test_extract_worksheet_data_total_equals_start_row")
        # arrange
        url_str = "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx"
        worksheet = "1A"
        hdr_row = 1
        total_row = 2
        start_row = 2
        end_row = 3
        num_cols = 5
        # act
        xlsx = XLSXhandler(url_str)
        xlsx.get_xlsx_from_url()
        # assert
        self.assertRaises(ValueError, xlsx.extract_worksheet_data, worksheet, hdr_row, total_row, start_row, end_row,
                          num_cols)

    def test_extract_worksheet_data_total_equals_end_row(self):
        """Check extract_worksheet_data throws a ValueError if total_row equals end_row"""
        print("@test_extract_worksheet_data_total_equals_end_row")
        # arrange
        url_str = "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx"
        worksheet = "1A"
        hdr_row = 1
        total_row = 3
        start_row = 2
        end_row = 3
        num_cols = 5
        # act
        xlsx = XLSXhandler(url_str)
        xlsx.get_xlsx_from_url()
        # assert
        self.assertRaises(ValueError, xlsx.extract_worksheet_data, worksheet, hdr_row, total_row, start_row, end_row,
                          num_cols)

    def test_get_xlsx_from_file_not_file(self):
        """Checks that a non-file (e.g. directory) False when checked"""
        print("@test_get_xlsx_from_file_not_file")
        # arrange
        fname = "D:/Documents/"
        # act
        xlsx = XLSXhandler(fname)
        # assert
        self.assertFalse(xlsx.get_xlsx_from_file())

    def test_get_xlsx_from_file_not_exist(self):
        """Checks that a file that doesn't exist returns False when checked"""
        print("@test_get_xlsx_from_file_not_exist")
        # arrange
        fname = "./nofile.txt"
        # act
        xlsx = XLSXhandler(fname)
        # assert
        self.assertFalse(xlsx.get_xlsx_from_file())

    def test_get_xlsx_from_file_exist_not_xlsx(self):
        """Checks that a valid filename, which exists bit isn't an Excel returns False when checked"""
        print("@test_get_xlsx_from_file_exist_not_xlsx")
        # arrange
        fname = "./textfile.txt"
        # act
        xlsx = XLSXhandler(fname)
        # assert
        self.assertFalse(xlsx.get_xlsx_from_file())

    def test_get_xlsx_from_file_exist_is_xlsx(self):
        """Checks that a valid file that's an Excel returns True when checked"""
        print("@test_get_xlsx_from_file_exist_is_xlsx")
        # arrange
        fname = "./sample.xlsx"
        # act
        xlsx = XLSXhandler(fname)
        # assert
        self.assertTrue(xlsx.get_xlsx_from_file())

# run tests
if __name__ == '__main__':
    unittest.main(verbosity=2)
