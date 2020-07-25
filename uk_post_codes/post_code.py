import re

from uk_post_codes.constants import BASE_PATTERN, WITH_SPECIAL_CASES_PATTERN


def validate_post_code_regex(post_code):
    base_pattern = re.compile(WITH_SPECIAL_CASES_PATTERN)
    return base_pattern.match(post_code)


def validate_post_code(post_code):
    pass
