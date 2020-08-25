# Program to print required details related to countries

import requests

resp = requests.get(r"https://restcountries.eu/rest/v2/all")
# print(resp.status_code)
if resp.status_code == 404:
    print("Invalid Country Name")
elif resp.status_code != 200:
    print("Could Not Find Country Name")
else:
    countries = resp.json()
    sel_countries = filter(lambda c: c["area"] is not None, countries)
    top10 = sorted(sel_countries, key=lambda l: l["area"], reverse=True)[:10]
    for i in top10:
        print(f"{i['name']:50}:{i['population']:11}{round(i['area']):11}{round(i['population'] / i['area']):8}")
    # ****************************Alternate Method********************
    # population = {}
    # for i in countries:
    #     if type(i["population"]) is int and type(i["area"]) is float:
    #         population[i["name"]] = i["population"]
    #     else:
    #         pass
    #
    # area = {}
    # for i in countries:
    #     if type(i["population"]) is int and type(i["area"]) is float:
    #         area[i["name"]] = i["area"]
    #     else:
    #         pass
    #
    # try:
    #     count = 0
    #     for i in sorted(population, key=population.get, reverse=True):
    #         print(f"{i:50}:{population[i]:11}{round(area[i]):11}{round(population[i] / area[i]):8}")
    #         count += 1
    #         if count == 10:
    #             break
    # except:
    #     pass
