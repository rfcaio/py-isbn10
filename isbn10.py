import re


ISBN10_DIGIT_GROUPS = r'(\d{2})(\d{3})(\d{4})([0-9X])'
ISBN10_FORMAT = r'\g<1>-\g<2>-\g<3>-\g<4>'
VALID_ISBN10_FORMAT = r'^\d{9}[0-9X]$'


class InvalidISBN10Error(Exception):
    pass


class ISBN10:
    def __init__(self, value):
        if type(value) != str:
            raise InvalidISBN10Error('Invalid ISBN-10 type.')

        if re.match(VALID_ISBN10_FORMAT, value) is None:
            raise InvalidISBN10Error('Invalid ISBN-10 format.')


def format_isbn10(isbn10):
    if not is_valid_isbn10(isbn10):
        raise InvalidISBN10Error('Invalid ISBN-10 code.')

    isbn10_match = re.match(ISBN10_DIGIT_GROUPS, isbn10)
    return isbn10_match.expand(ISBN10_FORMAT)


def is_valid_isbn10(isbn10):
    if not is_valid_isbn10_format(isbn10):
        return False

    isbn10_checksum = get_isbn10_checksum(isbn10)
    return isbn10_checksum % 11 == 0


def is_valid_isbn10_format(isbn10):
    return type(isbn10) == str and re.match(VALID_ISBN10_FORMAT, isbn10)


def get_isbn10_checksum(isbn10):
    result = 0
    for index, digit_string in enumerate(isbn10):
        digit = 10 if digit_string == 'X' else int(digit_string)
        coefficient = 10 - index
        result += coefficient * digit
    return result
