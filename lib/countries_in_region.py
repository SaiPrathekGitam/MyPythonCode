# Program to display countries in the given region

import requests

name = input("Enter The Region : ")

resp = requests.get(fr"https://restcountries.eu/rest/v2/region/{name}")
# print(resp.status_code)
if resp.status_code == 404:
    print("Invalid Region")
elif resp.status_code != 200:
    print("Could Not Find Region Name")
else:
    region = resp.json()
    lr = list(region)
    print(f"The Number Of Countries in {name.upper()} : {len(lr)}")
    for i in region:
        print(i["name"])