import unittest

from isbn10 import InvalidISBN10Error, ISBN10


class ISBN10Test(unittest.TestCase):
    def test_invalid_type(self):
        with self.assertRaises(InvalidISBN10Error) as error:
            ISBN10(1932698183)
        self.assertEqual(str(error.exception), 'Invalid ISBN-10 type.')

    def test_incomplete_value(self):
        with self.assertRaises(InvalidISBN10Error) as error:
            ISBN10('193269818')
        self.assertEqual(str(error.exception), 'Invalid ISBN-10 format.')

    def test_value_with_small_x_at_the_end(self):
        with self.assertRaises(InvalidISBN10Error) as error:
            ISBN10('855080603x')
        self.assertEqual(str(error.exception), 'Invalid ISBN-10 format.')

    def test_invalid_format(self):
        with self.assertRaises(InvalidISBN10Error) as too_many_digits_error:
            ISBN10('19326981830')
        self.assertEqual(
            str(too_many_digits_error.exception),
            'Invalid ISBN-10 format.'
        )

    def test_invalid_value(self):
        with self.assertRaises(InvalidISBN10Error) as error:
            ISBN10('1932698180')
        self.assertEqual(str(error.exception), 'Invalid ISBN-10 value.')

    def test_invalid_value_with_x_at_the_end(self):
        with self.assertRaises(InvalidISBN10Error) as error:
            ISBN10('193269818X')
        self.assertEqual(str(error.exception), 'Invalid ISBN-10 value.')

    def test_valid_isbn10_string_conversion(self):
        isbn = ISBN10('1932698183')
        self.assertEqual(str(isbn), '19-326-9818-3')
