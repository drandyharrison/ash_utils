import unittest
import numpy
from create_barchart import create_barchart
from create_barchart import are_create_barchart_params_valid

class testCreateBarchart(unittest.TestCase):
    def SetUp(self):
        """set-up code, which is called before each test, to avoid repetition"""
        pass

    def tearDown(self):
        """code to tidy up after each test"""
        pass

    def test_create_barchart_x_data_not_ndarray(self):
        """Check create_barchart throws a TypeError if x_data is not a numpy.ndarray"""
        print("@test_create_barchart_x_data_not_ndarray")
        # arrange
        x_data = []
        y_data = numpy.array([], dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_create_barchart_y_data_not_ndarray(self):
        """Check create_barchart throws a TypeError if y_data is not a numpy.ndarray"""
        print("@test_create_barchart_y_data_not_ndarray")
        # arrange
        x_data = numpy.array([], dtype=numpy.float64)
        y_data = []
        width = 1/1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_create_barchart_x_data_and_y_data_not_equal_len_1d(self):
        """Check create_barchart throws a ValueError if x_data and y_data are different lengths (when y is 1-d)"""
        print("@test_create_barchart_x_data_and_y_data_not_equal_len_1d")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(5, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_create_barchart_x_data_and_y_data_not_equal_len_2d(self):
        """Check create_barchart throws a ValueError if x_data and y_data are different lengths (when y is 2-d)"""
        print("@test_create_barchart_x_data_and_y_data_not_equal_len_2d")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones((3, 5), dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_create_barchart_colour_not_list(self):
        """Check create_barchart throws a TypeError if colour is not a list"""
        print("@test_create_barchart_colour_not_list")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = 'red'
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_create_barchart_colour_not_str(self):
        """Check create_barchart throws a TypeError if colour contains a non-string"""
        print("@test_create_barchart_colour_not_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["red", 3]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_create_barchart_colour_blank_str(self):
        """Check create_barchart throws a ValueError if colour is a blank string"""
        print("@test_create_barchart_colour_blank_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = [""]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_create_barchart_colour_empty_str(self):
        """Check create_barchart throws a ValueError if colour is an empty string"""
        print("@test_create_barchart_colour_empty_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["   "]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_create_barchart_width_is_str(self):
        """Check create_barchart throws a TypeError if test width is string"""
        print("@test_create_barchart_width_is_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = "3"
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_create_barchart_width_is_int(self):
        """Check create_barchart throws a TypeError if test width is an integer"""
        print("@test_create_barchart_width_is_int")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 3
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_create_barchart_xlabel_not_str(self):
        """Check create_barchart throws a TypeError if xlabel is not a string"""
        print("@test_create_barchart_xlabel_not_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = 3
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_create_barchart_xlabel_blank_str(self):
        """Check create_barchart throws a ValueError if xlabel is a blank string"""
        print("@test_create_barchart_xlabel_blank_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = "  "
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_create_barchart_xlabel_empty_str(self):
        """Check create_barchart throws a ValueError if xlabel is an empty string"""
        print("@test_create_barchart_xlabel_empty_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = ""
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_create_barchart_title_not_str(self):
        """Check create_barchart throws a TypeError if title is not a string"""
        print("@test_create_barchart_title_not_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = "Years"
        title = 3
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_create_barchart_fig_id_not_int(self):
        """Check create_barchart throws a TypeError if fig_id is not integer"""
        print("@test_create_barchart_fig_id_not_int")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = "x"
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_create_barchart_fig_id_not_pos(self):
        """Check create_barchart throws a ValueError if fig_id is not positive"""
        print("@test_create_barchart_fig_id_not_pos")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 0
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_create_barchart_sub_id_not_int(self):
        """Check create_barchart throws a TypeError if sub_id is not integer"""
        print("@test_create_barchart_sub_id_not_int")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = "111"
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_create_barchart_show_not_bool(self):
        """Check create_barchart throws a TypeError if show is not boolean"""
        print("@test_create_barchart_show_not_bool")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = 3
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_create_barchart_invalid_subplot_id(self):
        """Check create_barchart throws a warning if sub_id is not a valid subplot reference"""
        print("@test_create_barchart_fig_id_not_int")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 227
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = False
        type_of_bar = 's'
        # act
        # assert
        self.assertWarns(UserWarning, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                         ylabel, series_name, show, type_of_bar)

    def test_create_barchart_default_type_of_bar(self):
        """Check create_barchart runs ok using default value for type_of_bar"""
        print("@test_create_barchart_default_type_of_bar")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 223
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = False
        #type_of_bar = 's'
        # act
        # assert
        # confirm no exceptions (or warnings?) are raised
        create_barchart(x_data, y_data, width, colour, xlabel, title, fig_id, sub_id, ylabel, series_name, show)

    def test_create_barchart_default_type_of_bar_not_str(self):
        """Check create_barchart throws a TypeError if type_of_bar is not a string"""
        print("@test_create_barchart_default_type_of_bar_not_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 223
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = False
        type_of_bar = 3
        # act
        # assert
        # confirm no exceptions (or warnings?) are raised
        self.assertRaises(TypeError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show=show, type_of_bar=type_of_bar)

    def test_create_barchart_default_unknown_type_of_bar(self):
        """Check create_barchart throws a ValueError if type_of_bar is not known"""
        print("@test_create_barchart_default_unknown_type_of_bar")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 223
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = False
        type_of_bar = "x"
        # act
        # assert
        # confirm no exceptions (or warnings?) are raised
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show=show, type_of_bar=type_of_bar)

    def test_create_barchart_default_show(self):
        """Check create_barchart runs ok using default value for show"""
        print("@test_create_barchart_default_show")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 223
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        #show = False
        type_of_bar = 's'
        # act
        # assert
        # confirm no exceptions (or warnings?) are raised
        create_barchart(x_data, y_data, width, colour, xlabel, title, fig_id, sub_id, ylabel, series_name, type_of_bar=type_of_bar)

    def test_create_barchart_not_enough_colours(self):
        """Check create_barchart fails if there aren't enough colours for the data"""
        print("@test_create_barchart_not_enough_colours")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(shape=(2, 3), dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 223
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = False
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show=show, type_of_bar=type_of_bar)

    def test_create_barchart_3d_y_data(self):
        """Check create_barchart fails if y_data has more than 2 dimensions"""
        print("@test_create_barchart_3d_y_data")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(shape=(2, 3, 3), dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 223
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = False
        type_of_bar = 'h'
        # act
        # assert
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show=show, type_of_bar=type_of_bar)

    def test_create_barchart_ylabel_not_str(self):
        """Check create_barchart throws a TypeError if ylabel is not a string"""
        print("@test_create_barchart_ylabel_not_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = 3
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_create_barchart_ylabel_blank_str(self):
        """Check create_barchart throws a ValueError if ylabel is a blank string"""
        print("@test_create_barchart_ylabel_blank_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "   "
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_create_barchart_ylabel_empty_str(self):
        """Check create_barchart throws a ValueError if ylabel is an empty string"""
        print("@test_create_barchart_ylabel_empty_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = ""
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_create_barchart_series_name_not_list(self):
        """Check create_barchart throws a TypeError if series_name is not a list"""
        print("@test_create_barchart_series_name_not_list")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = '2012/12'
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_create_barchart_series_name_not_tuple_of_str(self):
        """Check create_barchart throws a TypeError if series_name is not a tuple pf strings"""
        print("@test_create_barchart_series_name_not_tuple_of_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', 2]
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_create_barchart_series_name_blank_str(self):
        """Check create_barchart throws a ValueError if series_name is not a list pf strings"""
        print("@test_create_barchart_series_name_blank_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', "  "]
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_create_barchart_series_name_empty_str(self):
        """Check create_barchart throws a ValueError if series_name is not a list of strings"""
        print("@test_create_barchart_series_name_blank_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', ""]
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_create_barchart_fewer_series_name(self):
        """Check create_barchart throws a ValueError if fewer series names than series"""
        print("@test_create_barchart_fewer_series_name")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones((2, 3), dtype=numpy.float64)
        width = 1/1.5
        colour = ["red", "green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_create_barchart_more_series_name(self):
        """Check create_barchart throws a ValueError if more series names than series"""
        print("@test_create_barchart_more_series_name")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones((2, 3), dtype=numpy.float64)
        width = 1/1.5
        colour = ["red", "green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['a', 'b', 'c']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)


    def test_are_create_barchart_params_valid_x_data_not_ndarray(self):
        """Check are_create_barchart_params_valid throws a TypeError if x_data is not a numpy.ndarray"""
        print("@test_are_create_barchart_params_valid_x_data_not_ndarray")
        # arrange
        x_data = []
        y_data = numpy.array([], dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, are_create_barchart_params_valid, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_are_create_barchart_params_valid_y_data_not_ndarray(self):
        """Check are_create_barchart_params_valid throws a TypeError if y_data is not a numpy.ndarray"""
        print("@test_are_create_barchart_params_valid_y_data_not_ndarray")
        # arrange
        x_data = numpy.array([], dtype=numpy.float64)
        y_data = []
        width = 1/1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, are_create_barchart_params_valid, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_are_create_barchart_params_valid_x_data_and_y_data_not_equal_len_1d(self):
        """Check are_create_barchart_params_valid throws a ValueError if x_data and y_data are different lengths (when y is 1-d)"""
        print("@test_are_create_barchart_params_valid_x_data_and_y_data_not_equal_len_1d")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(5, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, are_create_barchart_params_valid, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_are_create_barchart_params_valid_x_data_and_y_data_not_equal_len_2d(self):
        """Check are_create_barchart_params_valid throws a ValueError if x_data and y_data are different lengths (when y is 2-d)"""
        print("@test_are_create_barchart_params_valid_x_data_and_y_data_not_equal_len_2d")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones((3, 5), dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, are_create_barchart_params_valid, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_are_create_barchart_params_valid_colour_not_list(self):
        """Check are_create_barchart_params_valid throws a TypeError if colour is not a list"""
        print("@test_are_create_barchart_params_valid_colour_not_list")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = 'red'
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, are_create_barchart_params_valid, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_are_create_barchart_params_valid_colour_not_str(self):
        """Check are_create_barchart_params_valid throws a TypeError if colour contains a non-string"""
        print("@test_are_create_barchart_params_valid_colour_not_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["red", 3]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, are_create_barchart_params_valid, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_are_create_barchart_params_valid_colour_blank_str(self):
        """Check are_create_barchart_params_valid throws a ValueError if colour is a blank string"""
        print("@test_are_create_barchart_params_valid_colour_blank_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = [""]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, are_create_barchart_params_valid, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_are_create_barchart_params_valid_colour_empty_str(self):
        """Check are_create_barchart_params_valid throws a ValueError if colour is an empty string"""
        print("@test_are_create_barchart_params_valid_colour_empty_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["   "]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, are_create_barchart_params_valid, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_are_create_barchart_params_valid_width_is_str(self):
        """Check are_create_barchart_params_valid throws a TypeError if test width is string"""
        print("@test_are_create_barchart_params_valid_width_is_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = "3"
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, are_create_barchart_params_valid, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_are_create_barchart_params_valid_width_is_int(self):
        """Check are_create_barchart_params_valid throws a TypeError if test width is an integer"""
        print("@test_are_create_barchart_params_valid_width_is_int")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 3
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, are_create_barchart_params_valid, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_are_create_barchart_params_valid_xlabel_not_str(self):
        """Check are_create_barchart_params_valid throws a TypeError if xlabel is not a string"""
        print("@test_are_create_barchart_params_valid_xlabel_not_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = 3
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, are_create_barchart_params_valid, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_are_create_barchart_params_valid_xlabel_blank_str(self):
        """Check are_create_barchart_params_valid throws a ValueError if xlabel is a blank string"""
        print("@test_are_create_barchart_params_valid_xlabel_blank_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = "  "
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, are_create_barchart_params_valid, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_are_create_barchart_params_valid_xlabel_empty_str(self):
        """Check are_create_barchart_params_valid throws a ValueError if xlabel is an empty string"""
        print("@test_are_create_barchart_params_valid_xlabel_empty_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = ""
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, are_create_barchart_params_valid, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_are_create_barchart_params_valid_title_not_str(self):
        """Check are_create_barchart_params_valid throws a TypeError if title is not a string"""
        print("@test_are_create_barchart_params_valid_title_not_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = "Years"
        title = 3
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, are_create_barchart_params_valid, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_are_create_barchart_params_valid_fig_id_not_int(self):
        """Check are_create_barchart_params_valid throws a TypeError if fig_id is not integer"""
        print("@test_are_create_barchart_params_valid_fig_id_not_int")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = "x"
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, are_create_barchart_params_valid, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_are_create_barchart_params_valid_fig_id_not_pos(self):
        """Check are_create_barchart_params_valid throws a ValueError if fig_id is not positive"""
        print("@test_are_create_barchart_params_valid_fig_id_not_pos")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 0
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, are_create_barchart_params_valid, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_are_create_barchart_params_valid_sub_id_not_int(self):
        """Check are_create_barchart_params_valid throws a TypeError if sub_id is not integer"""
        print("@test_are_create_barchart_params_valid_sub_id_not_int")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = "111"
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, are_create_barchart_params_valid, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_are_create_barchart_params_valid_show_not_bool(self):
        """Check are_create_barchart_params_valid throws a TypeError if show is not boolean"""
        print("@test_are_create_barchart_params_valid_show_not_bool")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = 3
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, are_create_barchart_params_valid, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_are_create_barchart_params_valid_default_type_of_bar(self):
        """Check are_create_barchart_params_valid runs ok using default value for type_of_bar"""
        print("@test_are_create_barchart_params_valid_default_type_of_bar")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 223
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = False
        #type_of_bar = 's'
        # act
        # assert
        # confirm no exceptions (or warnings?) are raised
        are_create_barchart_params_valid(x_data, y_data, width, colour, xlabel, title, fig_id, sub_id, ylabel, series_name, show)

    def test_are_create_barchart_params_valid_default_type_of_bar_not_str(self):
        """Check are_create_barchart_params_valid throws a TypeError if type_of_bar is not a string"""
        print("@test_are_create_barchart_params_valid_default_type_of_bar_not_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 223
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = False
        type_of_bar = 3
        # act
        # assert
        # confirm no exceptions (or warnings?) are raised
        self.assertRaises(TypeError, are_create_barchart_params_valid, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show=show, type_of_bar=type_of_bar)

    def test_are_create_barchart_params_valid_default_show(self):
        """Check are_create_barchart_params_valid runs ok using default value for show"""
        print("@test_are_create_barchart_params_valid_default_show")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 223
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        #show = False
        type_of_bar = 's'
        # act
        # assert
        # confirm no exceptions (or warnings?) are raised
        are_create_barchart_params_valid(x_data, y_data, width, colour, xlabel, title, fig_id, sub_id, ylabel, series_name, type_of_bar=type_of_bar)

    def test_are_create_barchart_params_valid_not_enough_colours(self):
        """Check are_create_barchart_params_valid fails if there aren't enough colours for the data"""
        print("@test_are_create_barchart_params_valid_not_enough_colours")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(shape=(2, 3), dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 223
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = False
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, are_create_barchart_params_valid, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show=show, type_of_bar=type_of_bar)

    def test_are_create_barchart_params_valid_3d_y_data(self):
        """Check are_create_barchart_params_valid fails if y_data has more than 2 dimensions"""
        print("@test_are_create_barchart_params_valid_3d_y_data")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(shape=(2, 3, 3), dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 223
        ylabel = "Number (000s)"
        series_name = ['2012/12', '2016/17']
        show = False
        type_of_bar = 'h'
        # act
        # assert
        self.assertRaises(ValueError, are_create_barchart_params_valid, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show=show, type_of_bar=type_of_bar)

    def test_are_create_barchart_params_valid_ylabel_not_str(self):
        """Check are_create_barchart_params_valid throws a TypeError if ylabel is not a string"""
        print("@test_are_create_barchart_params_valid_ylabel_not_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = 3
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, are_create_barchart_params_valid, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_are_create_barchart_params_valid_ylabel_blank_str(self):
        """Check are_create_barchart_params_valid throws a ValueError if ylabel is a blank string"""
        print("@test_are_create_barchart_params_valid_ylabel_blank_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "   "
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, are_create_barchart_params_valid, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_are_create_barchart_params_valid_ylabel_empty_str(self):
        """Check are_create_barchart_params_valid throws a ValueError if ylabel is an empty string"""
        print("@test_are_create_barchart_params_valid_ylabel_empty_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = ""
        series_name = ['2012/12', '2016/17']
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, are_create_barchart_params_valid, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_are_create_barchart_params_valid_series_name_not_list(self):
        """Check are_create_barchart_params_valid throws a TypeError if series_name is not a list"""
        print("@test_are_create_barchart_params_valid_series_name_not_list")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = '2012/12'
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, are_create_barchart_params_valid, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_are_create_barchart_params_valid_series_name_not_tuple_of_str(self):
        """Check are_create_barchart_params_valid throws a TypeError if series_name is not a tuple pf strings"""
        print("@test_are_create_barchart_params_valid_series_name_not_tuple_of_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', 2]
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, are_create_barchart_params_valid, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_are_create_barchart_params_valid_series_name_blank_str(self):
        """Check are_create_barchart_params_valid throws a ValueError if series_name is not a list pf strings"""
        print("@test_are_create_barchart_params_valid_series_name_blank_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', "  "]
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, are_create_barchart_params_valid, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

    def test_are_create_barchart_params_valid_series_name_empty_str(self):
        """Check are_create_barchart_params_valid throws a ValueError if series_name is not a list of strings"""
        print("@test_are_create_barchart_params_valid_series_name_blank_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        ylabel = "Number (000s)"
        series_name = ['2012/12', ""]
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, are_create_barchart_params_valid, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                          ylabel, series_name, show, type_of_bar)

# TODO ensure unit tests cover all branches in code
# run tests
if __name__ == '__main__':
    unittest.main(verbosity=2)
