# Program to display countries in the all regions

import requests

# print("Countries In Each Region :-", end="")
resp = requests.get(fr"https://restcountries.eu/rest/v2/all")
# print(resp.status_code)
if resp.status_code == 404:
    print("Invalid Region")
elif resp.status_code != 200:
    print("Could Not Find Region Name")
else:
    deets = resp.json()
    count = {}
    for i in deets:
        if i["region"] in count:
            count[i["region"]] += 1
        elif i["region"] == "":
            pass
        else:
            count[i["region"]] = 1
    for m in count:
        print(f"{m:8} : {count[m]:2}")

    # *********************** METHOD 2 ******************************
    # regions = set()
    #     for i in deets:
    #         if i["region"] != "":
    #             regions.add(i["region"])
    #     count = {l: 0 for l in regions}
    #     for j in regions:
    #         # print(f"\n\nCountries In {j} :- ")
    #         for k in deets:
    #             if k["region"] == j:
    #                 count[k["region"]] += 1
    #     for m in count:
    #         print(f"{m:8} : {count[m]:2}")
