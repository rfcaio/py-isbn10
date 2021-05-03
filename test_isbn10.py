import unittest

from isbn10 import (
    format_isbn10,
    get_isbn10_checksum,
    is_valid_isbn10,
    is_valid_isbn10_format,
    InvalidISBN10Error,
    ISBN10
)


class ISBN10Test(unittest.TestCase):
    def test_invalid_type_for_isbn10_constructor(self):
        with self.assertRaises(InvalidISBN10Error) as e:
            ISBN10(1234567890)

        self.assertEqual(str(e.exception), 'Invalid ISBN-10 type.')

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

    def test_format_isbn10(self):
        with self.assertRaises(InvalidISBN10Error):
            format_isbn10('193269818X')

        self.assertEqual(format_isbn10('1932698183'), '19-326-9818-3')
        self.assertEqual(format_isbn10('855080603X'), '85-508-0603-X')

    def test_get_isbn10_checksum(self):
        self.assertEqual(get_isbn10_checksum('1932698183'), 264)
        self.assertEqual(get_isbn10_checksum('855080603X'), 253)

    def test_is_valid_isbn10(self):
        self.assertFalse(is_valid_isbn10('1932698184'))
        self.assertFalse(is_valid_isbn10('8550806030'))
        self.assertFalse(is_valid_isbn10(1932698183))
        self.assertFalse(is_valid_isbn10('855080603x'))

        self.assertTrue(is_valid_isbn10('1932698183'))
        self.assertTrue(is_valid_isbn10('855080603X'))

    def test_is_valid_isbn10_format(self):
        self.assertFalse(is_valid_isbn10_format(1932698183))
        self.assertFalse(is_valid_isbn10_format('855080603x'))

        self.assertTrue(is_valid_isbn10_format('1932698183'))
        self.assertTrue(is_valid_isbn10_format('855080603X'))
