import requests
import csv
import json
import sys


DEBUG = True
DIRECT_URL = "http://dop.edu.ru/organization/list?institution_type=188&orientation=3&region=42&page=1&perPage=10000"


def main():

    try:
        r = requests.get(DIRECT_URL)
        r.encoding = 'utf-8'
        json_data = r.json()
    except BaseException as e:
        print("request with error" + repr(e))
        sys.exit(0)

    # if got error: true in json response
    if not json_data["success"]:
        print("get error in json:", + json_data["error"])
        sys.exit(0)

    arr = []

    # parsing info
    for org in json_data["data"]["list"]:
        arr.append([org["full_name"], org["name"], org["site_url"]])

    # write into CSV
    with open("output.csv", "w") as output_file:
        writer = csv.writer(output_file)
        writer.writerows(arr)

    # DEBUG out json response
    if DEBUG:
        with open('data.json', 'w', encoding="utf-8") as output_file:
            json.dump(json_data, output_file, ensure_ascii=False)


if __name__ == "__main__":
    main()
