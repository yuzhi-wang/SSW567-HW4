"""

For this assignment imagine that you have been asked to develop a function that will
interface with GitHub in order to extract and present useful information to your user.
The function will communicate using the RESTful services APIs provided by GitHub.
The GitHub APIs will allow you to query for information about users,
repositories, etc... which can be retrieved using the function,
and then be displayed in the application.

"""
__author__ = 'Yuzhi Wang'

import requests
import json


def github_api(userid):
    response = requests.get("https://api.github.com/users/%s/repos" % userid)
    print(response.status_code)

    if response.status_code != 200:
        print("This userid is invalid")
        return False

    responsej = response.json()
    # print(json.dumps(responsej, indent=1))

    if len(responsej) == 0:
        print("0 repos exists ")
        return False

    for i in range(len(responsej)):
        name = responsej[i]['full_name']
        urlcommits = responsej[i]["commits_url"]
        getcommits = requests.get(urlcommits.split("{")[0])
        commitsnumber = len(getcommits.json())
        print(name + "\nNumber of commits: " + str(commitsnumber))

    return True


if __name__ == '__main__':
    username = input("Please enter your Github username: ")
    github_api(username)
