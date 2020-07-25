from three_five.constants import FIVE_STR, THREE_FIVE_STR, THREE_STR


def three_five(lower=1, upper=101):
    """
    :param lower: start value for desired range
    :param upper: upper - 1 indicates the last value on the range as python
        range excludes the last number
    :return: list containing the int, "Three", "Five" or "ThreeFive"
    """
    result = []

    if _check_if_range_boundaries_are_valid(lower=lower, upper=upper):
        result = [_three_five_threefive_or_value(_num) for _num in range(lower, upper)]

    return result


def three_five_print(lower=1, upper=101):
    """
    :param lower: start value for desired range
    :param upper: upper - 1 indicates the last value on the range as python
        range excludes the last number
    result => prints the int, "Three", "Five" or "ThreeFive"
    """
    if _check_if_range_boundaries_are_valid(lower=lower, upper=upper):
        for _num in range(lower, upper):
            print(_three_five_threefive_or_value(_num))


def three_five_generator(lower=1, upper=101, print_output=True):
    """
    :param lower: start value for desired range
    :param upper: upper - 1 indicates the last value on the range as python
        range excludes the last number
    :param print_output: flag to indicate if the user wishes to print to output
    :return: generator containing the int, "Three", "Five" or "ThreeFive"
    """

    if _check_if_range_boundaries_are_valid(lower=lower, upper=upper):
        for _num in range(lower, upper):
            _value = _three_five_threefive_or_value(_num)

            if print_output:
                print(_value)
            yield _value


def _three_five_threefive_or_value(_num):
    three, five, three_and_five = _is_three_and_five_multiple(_num)
    if three_and_five:
        _value = THREE_FIVE_STR
    elif five:
        _value = FIVE_STR
    elif three:
        _value = THREE_STR
    else:
        _value = _num
    return _value


def _is_three_and_five_multiple(_num):
    three, five, three_and_five = False, False, False
    if _num and isinstance(_num, int):
        three = not _num % 3
        five = not _num % 5
        three_and_five = three and five
    return three, five, three_and_five


def _check_if_range_boundaries_are_valid(lower, upper):
    return isinstance(lower, int) and (isinstance(upper, int) and upper > lower)
