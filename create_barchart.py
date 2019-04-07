import numpy
import matplotlib.pyplot as plt
import warnings


# TODO turn positional parameters into keyword parameters - update unit tests and call
def create_barchart(x_data, y_data, width, colour, xlabel, title, fig_id, sub_id, ylabel, series_name, show=True,
                    type_of_bar='s'):
    """Create a bar chart
    :param x_data: the x coordinates of the bars (the categories, don't have to be numeric)
    :param y_data: the height of the bars
    :param width: width of the bars
    :param colour: the colour of the bars
    :param xlabel: label for the x-axis
    :param title: title for the bar chart
    :param fig_id: figure id
    :param sub_id: subplot id
    :param ylabel: label for the y-axis
    :param series_name: the names of the series to be plotted (mainly used for the legend)
    :param show: boolean flag to indicate whether to show figure
    :param type_of_bar: type of bar chart: 'b' - basic, 'h' - horizontal
    :raises ValueError: when parameter has an invalid value
    """
    # validate parameters
    # TODO is there scope to simplify with asserts or validators?
    if not isinstance(x_data, numpy.ndarray):
        raise TypeError("@create_barchart: x_data {} is not a numpy.ndarray".format(type(x_data)))
    if not isinstance(y_data, numpy.ndarray):
        raise TypeError("@create_barchart: y_data {} is not a numpy.ndarray".format(type(y_data)))
    if y_data.ndim > 2:
        raise ValueError("@create_barchart: y_data can be at most 2-dimensional")
    if y_data.ndim == 1 and x_data.size != y_data.size:
        raise ValueError("@create_barchart: x_data [{}] and y_data [{}] are not the same length".format(x_data.size, y_data.size))
    if y_data.ndim == 2 and x_data.size != numpy.size(y_data, 1):
        raise ValueError("@create_barchart: x_data [{}] and y_data [{}] are not the same length".format(x_data.size, numpy.size(y_data, 1)))
    if not isinstance(width, float):
        raise TypeError("@create_barchart: width={} is not a float".format(width))
    if not isinstance(colour, list):
        raise TypeError("@create_barchart: colour={} is not a list".format(colour))
    for idx, c in enumerate(colour):
        if not isinstance(c, str):
            raise TypeError("@create_barchart: {}-th colour={} is not a string".format(idx, c))
        if not (c and c.strip()):
            raise ValueError("@create_barchart: colour is blank or empty")
    if (y_data.ndim == 1 and numpy.size(colour) < 1) or \
            (y_data.ndim == 2 and numpy.size(colour) < numpy.size(y_data, 0)):
        raise ValueError("@create_barchart: not enough colours")
    if not isinstance(xlabel, str):
        raise TypeError("@create_barchart: x_label={} is not a string".format(xlabel))
    if not (xlabel and xlabel.strip()):
        raise ValueError("@create_barchart: xlabel is blank or empty")
    if not isinstance(title, str):
        raise TypeError("@create_barchart: title={} is not a string".format(title))
    if not isinstance(fig_id, int):
        raise TypeError("@create_barchart: figure id {} is not an integer".format(fig_id))
    if fig_id <= 0:
        raise ValueError("@create_barchart: figure id {} is not positive".format(fig_id))
    if not isinstance(sub_id, int):
        raise TypeError("@create_barchart: subplot id {} is not an integer".format(sub_id))
    if not isinstance(ylabel, str):
        raise TypeError("@create_barchart: ylabel {} is not a string".format(ylabel))
    if not (ylabel and ylabel.strip()):
        raise ValueError("@create_barchart: ylabel is blank or empty")
    if not isinstance(series_name, list):
        raise TypeError("@create_barchart: series_name {} is not a list".format(series_name))
    for name in series_name:
        if not isinstance(name, str):
            raise TypeError("@create_barchart: series_name element {} is not a string".format(name))
        if not (name and name.strip()):
            raise ValueError("@create_barchart: series_name element is blank or empty")
    if not isinstance(show, bool):
        raise TypeError("@create_barchart: show {} is not a boolean".format(show))
    if not isinstance(type_of_bar, str):
        raise TypeError("@create_barchart: type_of_bar {} is not a string".format(type_of_bar))
    # check sub-plot id is valid (assumes 3 digit integer)
    a = int(sub_id/100)
    b = int(sub_id/10)%10
    c = sub_id%10
    num_subplots = a * b
    # TODO is there scope to refactor?
    # only plot the sub-plot if sub_id is valid
    if 1 <= c <= num_subplots:
        # create bar chart
        fig = plt.figure(fig_id)      # if figure id doesn't already exist, matplotlib.pyplot will create one
        # python doesn't have a switch-case
        if type_of_bar == 's':
            if y_data.ndim == 1:
                plt.subplot(sub_id)  # if subplot not consistent with figure, new sub-plots added
                plt.bar(x_data, y_data, width, color=colour[0])
                plt.xlabel(xlabel)
                plt.ylabel(ylabel)
            else:
                ax = fig.add_subplot(sub_id)
                num_rows = numpy.size(y_data, 0)
                x_index = numpy.arange(numpy.size(y_data, 1))
                width = width / num_rows
                rects = []
                for row_idx in range(num_rows):
                    rects.append(ax.bar(x_index + (row_idx * width), y_data[row_idx, :], width, color=colour[row_idx],
                            align='center'))
                plt.xticks(x_index + ((num_rows / 2) * width), x_data, rotation='vertical')
                plt.margins(0.2)                    # pad margins, so markers don't get clipped by the axes
                plt.subplots_adjust(bottom=0.15)    # tweak spacing to prevent clipping of tick labels
                # ax.set_xticklabels(x_data)
                if num_rows != len(series_name):
                    raise ValueError("@create_barchart: the number of series names doesn't match the number of series {} <> {}".format(num_rows, len(series_name)))
                # create legend
                leg_colour = []
                for i in range(num_rows):
                    leg_colour.append(rects[i][0])
                # TODO confirm legend works with 1 and 3 data series as well
                ax = fig.gca()
                ax.legend(leg_colour, series_name)
                # TODO plot values at the end of each bar (controlled by a flag) -
                #  see https://stackoverflow.com/questions/14270391/python-matplotlib-multiple-bars
                plt.xlabel(xlabel)
                plt.ylabel(ylabel)
        elif type_of_bar == 'h':
            if y_data.ndim == 1:
                plt.subplot(sub_id)  # if subplot not consistent with figure, new sub-plots added
                plt.barh(x_data, y_data, width, color=colour[0])
            else:
                ax = fig.add_subplot(sub_id)
                num_rows = numpy.size(y_data, 0)
                x_index = numpy.arange(numpy.size(y_data, 1))
                width = width/num_rows
                for row_idx in range(num_rows):
                    ax.barh(x_index + (row_idx * width), y_data[row_idx, :], width, color=colour[row_idx], align='center')
                ax.set_yticks(x_index + ((num_rows/2) * width))
                ax.set_yticklabels(x_data)
                # TODO add padding etc. to the horizontal bar chart as well
                # TODO legend working for horizontal bar chart as well
                # TODO plot values at the end of each bar (controlled by a flag) -
                #  see https://stackoverflow.com/questions/14270391/python-matplotlib-multiple-bars
                plt.ylabel(xlabel)
                plt.xlabel(ylabel)
        else:
            raise ValueError("@create_barchart unknown type_of_bar {}".format(type_of_bar))
        # only give sub-plot a title if title is a non-empty string
        if title:
            plt.title(title)
        if show:
            plt.show()
    else:
        warnings.warn("@create_barchart(): invalid subplot reference {}".format(sub_id))
