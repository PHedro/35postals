THREE_STR = "Three"
FIVE_STR = "Five"
THREE_FIVE_STR = "ThreeFive"


def three_five(lower=1, upper=101):
    result = []

    # we need to remember that the upper
    # limit from the range isn't included
    for _num in range(lower, upper):
        three = not _num % 3
        five = not _num % 5
        three_and_five = three and five

        if three_and_five:
            _value = THREE_FIVE_STR
        elif five:
            _value = FIVE_STR
        elif three:
            _value = THREE_STR
        else:
            _value = _num

        result.append(_value)

    return result


def print_three_five(flavor=three_five, lower=1, upper=101):
    for _item in flavor(lower=lower, upper=upper):
        print(_item)
