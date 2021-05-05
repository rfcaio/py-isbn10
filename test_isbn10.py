import unittest

from isbn10 import InvalidISBN10Error, ISBN10


class ISBN10Test(unittest.TestCase):
    def test_invalid_type_for_isbn10_constructor(self):
        with self.assertRaises(InvalidISBN10Error) as invalid_type_error:
            ISBN10(1234567890)
        self.assertEqual(
            str(invalid_type_error.exception),
            'Invalid ISBN-10 type.'
        )

    def test_invalid_format_for_isbn10_constructor(self):
        with self.assertRaises(InvalidISBN10Error) as incomplete_code_error:
            ISBN10('012345678')
        self.assertEqual(
            str(incomplete_code_error.exception),
            'Invalid ISBN-10 format.'
        )

        with self.assertRaises(InvalidISBN10Error) as final_x_lower_error:
            ISBN10('012345678x')
        self.assertEqual(
            str(final_x_lower_error.exception),
            'Invalid ISBN-10 format.'
        )

        with self.assertRaises(InvalidISBN10Error) as too_many_digits_error:
            ISBN10('0123456789X')
        self.assertEqual(
            str(too_many_digits_error.exception),
            'Invalid ISBN-10 format.'
        )

    def test_invalid_value_for_isbn10_constructor(self):
        with self.assertRaises(InvalidISBN10Error) as value_error:
            ISBN10('1932698184')
        self.assertEqual(str(value_error.exception), 'Invalid ISBN-10 value.')

        with self.assertRaises(InvalidISBN10Error) as value_with_final_x_error:
            ISBN10('193269818X')
        self.assertEqual(
            str(value_with_final_x_error.exception),
            'Invalid ISBN-10 value.'
        )

    def test_isbn10_string_conversion(self):
        isbn = ISBN10('1932698183')
        self.assertEqual(str(isbn), '19-326-9818-3')

        isbn_with_final_x = ISBN10('855080603X')
        self.assertEqual(str(isbn_with_final_x), '85-508-0603-X')
