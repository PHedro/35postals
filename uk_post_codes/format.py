import re

from uk_post_codes.validate import (
    validate_base_cases,
    validate_bermuda,
    validate_cayman_islands,
    validate_montserrat,
    validate_regions_that_have_up_to_four_post_codes,
)


def format_post_code(raw_data):
    formatted_data = ""
    if isinstance(raw_data, str) and len(raw_data) > 3:
        data = "".join(_char for _char in raw_data if _char.isalnum()).upper()
        for validator, formatter in VALIDATORS_FORMATTER:
            if validator(data):
                formatted_data = formatter(data)
                break
    return formatted_data


def bermuda_formatter(data):
    return "{} {}".format(data[:2], data[-2:])


def cayman_formatter(data):
    return "{}-{}".format(data[:3], data[-4:])


def montserrat_formatter(data):
    return "{}-{}".format(data[:3], data[-4:])


def up_to_four_formatter(data):
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


def base_formatter(data):
    return "{} {}".format(data[:-3], data[-3:])


VALIDATORS_FORMATTER = (
    (validate_bermuda, bermuda_formatter),
    (validate_cayman_islands, cayman_formatter),
    (validate_montserrat, montserrat_formatter),
    (validate_regions_that_have_up_to_four_post_codes, up_to_four_formatter),
    (validate_base_cases, base_formatter),
)
