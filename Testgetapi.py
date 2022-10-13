"""

test file for getgithub api

"""
__author__ = 'Yuzhi Wang'

import unittest
from unittest import mock
from unittest.mock import Mock, patch, MagicMock


class Testgetapi(unittest.TestCase):
    @mock.patch('Githubapi.github_api')
    def test_mock_api1(self, mock_username1):
        mock_username1.return_value = MagicMock(userid='yuzhi-wang')
        mockresult = mock_username1.return_value.userid
        self.assertEqual(mockresult, 'yuzhi-wang')

    @mock.patch('Githubapi.github_api')
    def test_mock_api2(self, mock_username2):
        mock_username2.return_value = MagicMock(userid='werwerwer')
        mockresult = mock_username2.return_value.userid
        self.assertEqual(mockresult, 'werwerwer')


if __name__ == '__main__':
    print("Test cases are running")
    unittest.main()
