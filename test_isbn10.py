import unittest

from isbn10 import get_isbn10_checksum


class ISBN10Test(unittest.TestCase):
    def test_get_isbn10_checksum(self):
        self.assertEqual(get_isbn10_checksum('1932698183'), 264)
        self.assertEqual(get_isbn10_checksum('855080603X'), 253)
