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
    response = requests.get("https://api.github.com" + "/users" + "/" + userid + "/repos")
    print(response.status_code)

    if response.status_code != 200:
        print("This userid is invalid")
        return False

    responsej = response.json()
    # print(json.dumps(responsej, indent=1))

    if len(responsej) == 0:
        print("0 repos exists ")
        return False

    for repo in responsej:
        get_repocommits = requests.get(repo['commits_url'].split("{")[0])
        total_commits = get_repocommits.json()
        print("Repository Name: " + repo['full_name'] + " \nNumber Of Commits: " + str(len(total_commits)))

    return True


if __name__ == '__main__':
    username = input("Please enter your Github username: ")
    github_api(username)
