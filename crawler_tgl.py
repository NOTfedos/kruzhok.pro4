#!./bin/python3
import requests
import csv
import json
import sys
import time


DEBUG = False
DIRECT_URL = "http://dop.edu.ru/organization/list?institution_type=188&orientation=3&page=1&perPage=9000&region=42"


def main():

    try:
        r = requests.get(DIRECT_URL)
        r.encoding = "utf-8"
        json_data = r.json()
    except BaseException as e:
        print("request with error:", repr(e))
        sys.exit(0)

    # if got error: true in json response
    if not json_data["success"]:
        print("get error in json:", json_data["error"])
        sys.exit(0)

    orgs_list = []

    # parsing info
    for org in json_data["data"]["list"]:
        orgs_list.append([org["full_name"], org["name"], org["site_url"]])

    # write into CSV
    with open("output.csv", "w", encoding="utf-8") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(["Полное название организации",
                         "Краткое название организации",
                         "Адрес сайта организации"])
        writer.writerows(orgs_list)

    # DEBUG out json response
    if DEBUG:
        with open('data.json', 'w', encoding="utf-8") as output_file:
            json.dump(json_data, output_file, ensure_ascii=False)

    print("Success")


if __name__ == "__main__":
    timing = time.time()
    main()
    print("Finished in", (time.time() - timing), "seconds")
