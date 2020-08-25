# Program to accept github user ID and display list of repos

import requests

name = input("Enter User ID : ")
resp = requests.get(fr"https://api.github.com/users/{name}/repos")
print(resp.status_code)
if resp.status_code == 404:
    print("Invalid Id")
elif resp.status_code != 200:
    print("Could Not Find Repo")
else:
    repos = resp.json()
    for i in repos:
        print(i["name"])
