import re


ISBN10_DIGIT_GROUPS = r'(\d{2})(\d{3})(\d{4})([0-9X])'
ISBN10_FORMAT = r'\g<1>-\g<2>-\g<3>-\g<4>'
VALID_ISBN10_FORMAT = r'^\d{9}[0-9X]$'


class InvalidIsbn10Error(Exception):
    pass


class Isbn10:
    def __init__(self, value):
        if type(value) != str:
            raise InvalidIsbn10Error('Invalid ISBN-10 type.')

        if self.__has_invalid_format(value):
            raise InvalidIsbn10Error('Invalid ISBN-10 format.')

        if self.__is_not_valid_isbn10(value):
            raise InvalidIsbn10Error('Invalid ISBN-10 value.')

        self.__value = value

    def __str__(self):
        return re.match(ISBN10_DIGIT_GROUPS, self.__value).expand(ISBN10_FORMAT)

    def __has_invalid_format(self, value):
        return re.match(VALID_ISBN10_FORMAT, value) is None

    def __is_not_valid_isbn10(self, value):
        return self.__get_isbn10_checksum(value) % 11 != 0

    def __get_isbn10_checksum(self, value):
        result = 0
        for index, digit_as_text in enumerate(value):
            digit = 10 if digit_as_text == 'X' else int(digit_as_text)
            coefficient = 10 - index
            result += coefficient * digit
        return result
