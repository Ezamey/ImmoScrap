#pas utile pour le script mais je garde ce  snipet
# qui permet de diviser une liste en  plus petite liste
# pour un possible multithread
from axelle_main_2 import get_urls

splitter = 5
details_urls =  get_urls()
chunks = [details_urls[x:x+10] for x in range(0,len(details_urls),5)]


for chunk in chunks:
    #TODO: faire une class thread qui scraperait 

