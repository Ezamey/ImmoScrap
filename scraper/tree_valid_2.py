from requests_html import HTMLSession
from bs4  import BeautifulSoup
import json
import os
import pandas as pd
import re

from axelle_main import  details_urls



dict_list = []
for URL in details_urls:
    print("Scrapping : {}".format(URL))
    session = HTMLSession()
    r = session.get(URL)
    r.html.render()
    soup = BeautifulSoup(r.content,"lxml")

    head_tag = soup.head
    stuff = (head_tag.script)

    remove_window = str(stuff).split("[")
    remove_window.pop(0)
    join_v1 = "".join(remove_window)
    remove_window_2 = str(join_v1).split("]")
    remove_window_2.pop(-1)

    final = []
    for elem in remove_window_2:
        final.append(elem.strip())

    x = "".join(final)
    reg1 = re.findall(r'".*"',x)
    list_data = reg1[6:-10]

    dict_json = {}
    for data in  list_data:
        if not ":"in data:
            continue
        splitting = data.split(":")
        key = splitting[0][1:-1]
        value = splitting[1][2:-1]
        if dict_json.get(key):
            if "type" in key:
                dict_json["cuisine_type"]=value
                continue
            if "id" in key:
                dict_json["short_id"]= value
                continue
        if "count" in key:
            dict_json["room_number"]=value
            continue
        if "name" in key:
            dict_json["company_name"]=value
            continue
        if "exists" in key:
            continue
        if " " in value:
            dict_json[key]="False"
        dict_json[key]=value

        

    #getting  dimensions
    description_el =soup.find('p', attrs={'class': ['classified__information--property']})
    descriptions = list(description_el.stripped_strings)
    description = " ".join(descriptions) if descriptions else ""
    try:
        m2 = description.split("|")[1].strip().split()[0]
        dict_json["m2"]= m2
    except IndexError:
        m2 = description.split()[0]
        dict_json["m2"]=m2

    #Locality:
    locality = URL.split("/")[-3]
    dict_json["commune"]=locality

    dict_list.append(dict_json)

