import unittest

from isbn10 import (
    format_isbn10,
    get_isbn10_checksum,
    is_valid_isbn10,
    is_valid_isbn10_format
)


class ISBN10Test(unittest.TestCase):
    def test_format_isbn10(self):
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
