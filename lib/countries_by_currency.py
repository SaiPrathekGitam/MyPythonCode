# Program to display details of countries

import requests

currency = input("Enter The Currency Code : ")

resp = requests.get(r"https://restcountries.eu/rest/v2/all")
# print(resp.status_code)
if resp.status_code == 404:
    print("Invalid Country Code")
elif resp.status_code != 200:
    print("Could Not Find Country Name")
else:
    countries = resp.json()
    for i in countries:
        for j in i['currencies']:
            try:
                # print(j['code'])
                if currency in j['code']:
                    print(i['name'])
            except TypeError:
                pass
