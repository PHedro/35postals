import re
from copy import copy

from uk_post_codes.constants import (
    LIMITED_POST_CODES_CHUNKS,
    WITH_SPECIAL_CASES_PATTERN,
)


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

        # in the case the base cases don't validate the code let's give the
        # special cases a try
        if not result:
            result = _validate_special_cases(copy_post_code)

    return result


def _validate_special_cases(post_code):
    result = False
    for _validation in SPECIAL_CASES_VALIDATION_FUNCTIONS:
        # making a copy of the data instead of reference in case we need to original
        # later on so we do not make changes to it and that way in the validation
        # function we're able to make inplace transformations without the concerns
        result = _validation(post_code=re.sub("-", "", re.sub(" ", "", post_code)))
        if result:
            break
    return result


def _validate_regions_that_have_up_to_four_post_codes(post_code):
    result = False
    for outward, inward in LIMITED_POST_CODES_CHUNKS:
        result = post_code == outward + inward
        if result:
            break
    return result


def _validate_montserrat(post_code):
    try:
        inward = int(post_code[3:])
    except ValueError:
        return False

    return post_code.startswith("MSR") and -1 < inward < 10000


def _validate_cayman_islands(post_code):
    result = False
    if 6 < len(post_code) < 9 and post_code.startswith("KY"):
        first_number = post_code[2]
        inward = post_code[3:]
        try:
            first_number = int(first_number)
            inward = int(inward)
        except ValueError:
            return False
        result = first_number in {1, 2, 3} and 1000 < inward < 2502

    return result


def _validate_bermuda(post_code):
    result = len(post_code) == 4
    if result:
        try:
            result = -1 < int(post_code[-2:]) < 100 and re.match(
                "[A-Z]{2}", post_code[:2]
            )
        except ValueError:
            result = False
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


SPECIAL_CASES_VALIDATION_FUNCTIONS = (
    _validate_regions_that_have_up_to_four_post_codes,
    _validate_cayman_islands,
    _validate_montserrat,
    _validate_bermuda,
)
