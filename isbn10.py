import re


ISBN10_DIGIT_GROUPS = r'(\d{2})(\d{3})(\d{4})([0-9X])'
ISBN10_FORMAT = r'\g<1>-\g<2>-\g<3>-\g<4>'
VALID_ISBN10_FORMAT = r'^\d{9}[0-9X]$'


class InvalidISBN10Error(Exception):
    pass


class ISBN10:
    def __init__(self, value):
        if self.__hasInvalidType(value):
            raise InvalidISBN10Error('Invalid ISBN-10 type.')

        if re.match(VALID_ISBN10_FORMAT, value) is None:
            raise InvalidISBN10Error('Invalid ISBN-10 format.')

        if self.__is_not_valid_isbn10(value):
            raise InvalidISBN10Error('Invalid ISBN-10 value.')

        self.__value = value

    def __str__(self):
        return re.match(ISBN10_DIGIT_GROUPS, self.__value).expand(ISBN10_FORMAT)

    def __hasInvalidType(self, value):
        return type(value) != str

    def __is_not_valid_isbn10(self, value):
        return self.__get_isbn10_checksum(value) % 11 != 0

    def __get_isbn10_checksum(self, value):
        result = 0
        for index, digit_as_text in enumerate(value):
            digit = 10 if digit_as_text == 'X' else int(digit_as_text)
            coefficient = 10 - index
            result += coefficient * digit
        return result
