import re

from uk_post_codes.validate import (
    _validate_base_cases,
    _validate_bermuda,
    _validate_cayman_islands,
    _validate_montserrat,
    _validate_regions_that_have_up_to_four_post_codes,
)


def format_post_code(raw_data):
    """
    :param raw_data: non formatted and possibly with invalid characters
    to be formatted as postal code
    :return: formatted and valid postal code
    """
    formatted_data = ""
    if isinstance(raw_data, str) and len(raw_data) > 3:
        data = "".join(_char for _char in raw_data if _char.isalnum()).upper()
        for validator, formatter in VALIDATORS_FORMATTER:
            if validator(data):
                formatted_data = formatter(data)
                break
    return formatted_data


def _bermuda_formatter(data):
    return "{} {}".format(data[:2], data[-2:])


def _cayman_formatter(data):
    return "{}-{}".format(data[:3], data[-4:])


def _montserrat_formatter(data):
    return "{}-{}".format(data[:3], data[-4:])


def _up_to_four_formatter(data):
    formatted_data = ""
    if data.startswith("AI"):
        formatted_data = "{}-{}".format(data[:2], data[-4:])
    elif data.startswith("VG"):
        formatted_data = "{}-{}".format(data[:2], data[-4:])
    elif data.endswith("1ZZ"):
        formatted_data = "{}-{}".format(data[:4], data[-3:])
    elif data.startswith("BFPO"):
        formatted_data = "{}-{}".format(data[:4], data[-2:])
    elif data.startswith("BF1"):
        formatted_data = "{}-{}".format(data[:3], data[-3:])
    return formatted_data


def _base_formatter(data):
    return "{} {}".format(data[:-3], data[-3:])


VALIDATORS_FORMATTER = (
    (_validate_bermuda, _bermuda_formatter),
    (_validate_cayman_islands, _cayman_formatter),
    (_validate_montserrat, _montserrat_formatter),
    (_validate_regions_that_have_up_to_four_post_codes, _up_to_four_formatter),
    (_validate_base_cases, _base_formatter),
)
