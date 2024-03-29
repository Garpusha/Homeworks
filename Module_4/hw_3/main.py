import json
import requests
from time import sleep
from fake_headers import Headers
from bs4 import BeautifulSoup


def get_links(headers_, pages_):
    links_ = []
    index = 0
    url_ = "https://spb.hh.ru/search/vacancy?text=python&area=1&area=2"
    while index != pages_:
        print(f"Reading page {index + 1} of {pages_}")
        target_url = f"{url_}&page={str(index)}"
        result = requests.get(target_url, headers=headers_.generate())
        if result.status_code == 404:
            return links_
        sleep(1)
        soup = BeautifulSoup(result.text, "lxml")
        positions_list = soup.find_all("a", class_="serp-item__title")
        [links_.append(f'{position["href"]}') for position in positions_list]
        index += 1
    return links_


def get_title(my_soup):
    request = my_soup.find("h1", {"data-qa": "vacancy-title"})
    if request:
        return request.text.replace("\xa0", " ")
    return "Название позиции не указано"


def get_company(my_soup):
    request = my_soup.find("span", class_="vacancy-company-name")
    if request:
        return request.text.replace("\xa0", " ")
    return "Компания не указана"


def get_salary(my_soup):
    request = my_soup.find("div", {"data-qa": "vacancy-salary"})
    if request:
        return request.text.replace("\xa0", " ")
    return "Зарплата не указана"


def get_location(my_soup):
    request = my_soup.find("p", {"data-qa": "vacancy-view-location"})
    if request:
        return request.text.replace("\xa0", " ")
    else:
        request = my_soup.find("span", {"data-qa": "vacancy-view-raw-address"})
        if request:
            return request.text.replace("\xa0", " ")
    return "Адрес не указан"


def get_details(headers_, my_list):
    positions = len(my_list)
    dict_details = {}
    my_positions = []
    for index, url in enumerate(my_list):
        result = requests.get(url=url, headers=headers_.generate())
        if result.status_code == 404:
            print(f"Page '{url}' not found")
            exit()
        print(f"Checking job position {index + 1} of {positions}")
        job_html = result.text
        soup = BeautifulSoup(job_html, "lxml")
        description = soup.find("div", class_="vacancy-branded-user-content")
        if description:
            description = description.text
        else:
            description = soup.find("div", class_="g-user-content").text
        if "Flask" in description and "Django" in description:
            dict_details = {
                "name": get_title(soup),
                "link": url,
                "salary": get_salary(soup),
                "company": get_company(soup),
                "address": get_location(soup),
            }
            if usd:
                if "USD" in dict_details["salary"]:
                    my_positions.append(dict_details)
                else:
                    continue
            my_positions.append(dict_details)
        sleep(1)
    return my_positions


headers = Headers(browser="firefox", os="win")
choice = input("Pages to get (max.40): ")
if not choice.isdecimal():
    print("Wrong input.")
    exit()
else:
    pages = int(choice)
choice = input("Check all positions / USD salary only (1/0): ")
if choice == "0":
    usd = True
elif choice == "1":
    usd = False
else:
    print("Wrong input.")
    exit()
links = get_links(headers, pages)
job_details = get_details(headers, links)
with open("files\\result.json", "w", encoding="utf-8") as result_json:
    for job in job_details:
        json.dump(job, result_json, ensure_ascii=False, indent=2)
