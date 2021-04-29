def is_valid_isbn10(isbn10):
    isbn10_checksum = get_isbn10_checksum(isbn10)
    return isbn10_checksum % 11 == 0


def get_isbn10_checksum(isbn10):
    result = 0
    for index, digit_string in enumerate(isbn10):
        digit = 10 if digit_string == 'X' else int(digit_string)
        coefficient = 10 - index
        result += coefficient * digit
    return result
