import re
from copy import copy

from uk_post_codes.constants import BASE_PATTERN, WITH_SPECIAL_CASES_PATTERN


"""
POSTCODE
Outward code        Inward code
Area    District    Sector  Unit
SW      1W          0       NY
"""


def validate_post_code_regex(post_code):
    base_pattern = re.compile(WITH_SPECIAL_CASES_PATTERN)
    return base_pattern.match(post_code)


def validate_post_code(post_code):
    result = False

    # as the smaller special case is valid containing 4 characters LL99
    # for Bermudas and all other cases have a 8 characters limit including the
    # space or dash (-) character
    if post_code and isinstance(post_code, str) and 3 < len(post_code.strip()) < 9:
        copy_post_code = copy(post_code)
        copy_post_code = copy_post_code.strip()

        result = _validate_base_cases(copy_post_code)
    return result


def _validate_base_cases(post_code):
    result = False

    chunks = post_code.split(" ")
    qtt_chunks = len(chunks)
    if qtt_chunks == 2:
        result = _validate_outward_code_base(chunks[0]) and _validate_inward_code_base(
            chunks[1]
        )

    if qtt_chunks == 1 and 4 < len(chunks[0]) < 8:
        result = _validate_outward_code_base(
            chunks[0][:-3]
        ) and _validate_inward_code_base(chunks[0][-3:])

    return result


def _validate_inward_code_base(inward):
    return re.match("^[0-9][A-Z]{2}$", inward)


def _validate_outward_code_base(outward):
    return re.match("^[A-Z]{1,2}[0-9][A-Z0-9]?$", outward)
