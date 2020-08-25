# Program to display details of countries

import requests

while True:
    name = input("Enter The Name : ")
    if name == 'end':
        break
    resp = requests.get(fr"https://restcountries.eu/rest/v2/name/{name}")
    # print(resp.status_code)
    if resp.status_code == 404:
        print("Invalid Country Name")
    elif resp.status_code != 200:
        print("Could Not Find Country Name")
    else:
        countries = resp.json()
        for i in countries:
            print(f'\nName : {i["name"]}\nCapital : {i["capital"]}\nFlag : {i["flag"]}')
            if len(i["borders"]) == 0:
                print("No Borders", end="")
            else:
                print(f"Borders : ", end="")
            for j in i["borders"]:
                print(f"{j}", end=" ")
            print("\nCurrencies : ", end="")
            for k in i["currencies"]:
                print(f"\n\tCode : {k['code']}", end=" ")
                print(f"\n\tName : {k['name']}", end=" ")
