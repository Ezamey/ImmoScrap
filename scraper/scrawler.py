import re
from bs4 import BeautifulSoup
import scrapy
from scrapy.http.request import Request
from getters import get_urls

# scrapy runspider scrawler.py -o stocks.csv
class MySpider(scrapy.Spider):
    name = "immoscrap"
    start_urls = get_urls()

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        url = str(response.url)

        for _ in response.xpath("(//main[@id='main-content'])[1]"):
            source = response.text
            soup = BeautifulSoup(source, 'lxml')
            head_tag = soup.head
            #get the value from the script tag
            stuff = (head_tag.script)


            remove_window = str(stuff).split("[")                               #
            remove_window.pop(0)                                                #
            join_v1 = "".join(remove_window)                                    # All these operations are intended to clean
            remove_window_2 = str(join_v1).split("]")                           # the script tag in order
            remove_window_2.pop(-1)                                             # to arrive at an iterable.
                                                                                #
            final = []                                                          #
            for elem in remove_window_2:                                        #
                final.append(elem.strip())                                      #
            x = "".join(final)                                                  #
            reg1 = re.findall(r'".*"',x)                                        #
            list_data = reg1[6:-10]                                             #

            
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
            try:
                description_el = soup.find('p', attrs={'class': ['classified__information--property']})#BeautifulSoup method
                descriptions = list(description_el.stripped_strings)#list + BeautifulSoup method
                description = " ".join(descriptions) if descriptions else "" #remove white space
                try:
                    m2 = description.split("|")[1].strip().split()[0]
                    dict_json["m2"]= m2
                except IndexError:
                    m2 = description.split()[0]
                    dict_json["m2"]=m2
            except AttributeError:
                pass

            #Location:
            locality = url.split("/")[-3]
            dict_json["commune"]=locality

            yield dict_json 
