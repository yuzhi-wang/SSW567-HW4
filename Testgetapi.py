"""

test file for getgithub api

"""
__author__ = 'Yuzhi Wang'

import unittest
from unittest import mock
from unittest.mock import Mock, patch, MagicMock

from Githubapi import github_api


class Testgetapi(unittest.TestCase):
    @mock.patch('Githubapi.github_api')
    def test_mock_api1(self, mock_username1):
        mock_username1.return_value = MagicMock(userid='yuzhi-wang')
        result = mock_username1.return_value.userid
        try:
            self.assertEqual(result, 'yuzhi-wang')
        except:
            print("Failed")
        else:
            print("Success")

    def testgetGapi(self):
        self.assertEqual(github_api('werwerwer'), False)

    def testgetGapi2(self):
        self.assertEqual(github_api('yuzhi-wang'), True)

    def testgetGapi3(self):
        self.assertEqual(github_api('asdfawefaf'), False)


if __name__ == '__main__':
    print("Test cases are running")
    unittest.main()
