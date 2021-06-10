import unittest

from isbn10 import InvalidISBN10Error, ISBN10


class ISBN10Test(unittest.TestCase):
    def test_invalid_type(self):
        with self.assertRaises(InvalidISBN10Error) as error:
            ISBN10(1932698183)
        self.assertEqual(str(error.exception), 'Invalid ISBN-10 type.')

    def test_invalid_format(self):
        with self.assertRaises(InvalidISBN10Error) as incomplete_code_error:
            ISBN10('193269818')
        self.assertEqual(
            str(incomplete_code_error.exception),
            'Invalid ISBN-10 format.'
        )

        with self.assertRaises(InvalidISBN10Error) as small_x_error:
            ISBN10('855080603x')
        self.assertEqual(
            str(small_x_error.exception),
            'Invalid ISBN-10 format.'
        )

        with self.assertRaises(InvalidISBN10Error) as too_many_digits_error:
            ISBN10('19326981830')
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
