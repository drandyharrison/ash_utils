import numpy

def are_replace_nonnumeric_params_valid(nonnumeric=numpy.nan, cast=False):
    """Check parameters for replace_nonnumeric are valid
    :param nonumeric: numeric (int or float)
        replace non-numeric values with this value
    :param cast: bool
        attempt to cast non-numeric values; e.g. a string like '123'
    :raises TypeError: when a parameter has an invalid type or value
    :return: bool
        are the parameters all valid?
    """
    if not (isinstance(nonnumeric, int) or isinstance(nonnumeric, float)):
        raise TypeError("@replace_nonnumeric: nonnumeric is not numeric")
    if not isinstance(cast, bool):
        raise TypeError("@replace_nonnumeric: cast is not boolean")
    return True

def replace_nonnumeric(data, nonnumeric=numpy.nan, cast=False):
    """Given an iterable object, replace any non-numeric objects
    :param data: numeric iterable
        the iterable object to be modified
    :param nonumeric: numeric (int or float)
        replace non-numeric values with this value
    :param cast: bool
        attempt to cast non-numeric values; e.g. a string like '123'
    :raises TypeError: when a parameter has an invalid type or value
    """
    if are_replace_nonnumeric_params_valid(nonnumeric, cast):
        try:
            iterator = iter(data)
        except TypeError:
            raise TypeError("@replace_nonnumeric: data is not iterable")
        # replace non-numeric values
        for idx, val in enumerate(data):
            if not (isinstance(val, int) or isinstance(val, float)):
                if cast:
                    if isinstance(val, str):
                        try:
                            new_val = float(val)
                        except ValueError:
                            new_val = nonnumeric
                else:
                    new_val = nonnumeric
                data[idx] = new_val
