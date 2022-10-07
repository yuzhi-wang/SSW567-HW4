"""

test file for getgithub api

"""
__author__ = 'Yuzhi Wang'
import unittest

from Githubapi import github_api


class Testgetapi(unittest.TestCase):
    def testgetGapi(self):
        self.assertEqual(github_api('werwerwer'), False)

    def testgetGapi2(self):
        self.assertEqual(github_api('yuzhi-wang'), True)

    def testgetGapi3(self):
        self.assertEqual(github_api('asdfawefaf'), False)


if __name__ == '__main__':
    print("Test cases are running")
    unittest.main()
