import re

import pandas as pd


def get_name(split_list: list) -> str:
    return split_list[0]


def get_city(split_list: list) -> str:
    try:
        if int(split_list[-2][0]) or split_list[-2][0] == "0":
            result_return = re.sub(r"\d+", "", split_list[-3], flags=re.UNICODE)
            return result_return
    except ValueError:
        pass
    result_return = re.sub(r"\d+", "", split_list[-2], flags=re.UNICODE)
    return result_return


def get_country(split_list: list) -> str:
    return split_list[-1]


def main():
    data_df = pd.read_csv("ScopusConferencies.csv", sep=',', error_bad_lines=False)
    data_list = data_df["Авторы организаций"].to_list()
    data_list_split = []
    name_list = []
    city_list = []
    country_list = []
    for elem in data_list:
        try:
            for item in elem.split("; "):
                data_list_split.append(item)
        except AttributeError:
            pass

    for item in data_list_split:
        item_split = item.split(", ")
        name_list.append(get_name(item_split))
        city_list.append(get_city(item_split))
        country_list.append(get_country(item_split))

    result_df = pd.DataFrame({"Author": name_list, "City": city_list, "Country": country_list})
    result_df.to_excel("result_new.xlsx", index=False)
