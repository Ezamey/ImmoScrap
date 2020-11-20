# ImmoScrap 

### By:
- Axelle Paquet
- Julien Bert
- Christian Melot


_PoweredBy_:

[![N|Solid](https://res.cloudinary.com/practicaldev/image/fetch/s--xYNk7vjX--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://thepracticaldev.s3.amazonaws.com/i/dpf1jzsiy8n1tmdfxn1v.jpg)](https://nodesource.com/products/nsolid)

ImmoScrap is  script using scrapy and  BeautifulSoup to scrape data from the Immoweb.be site.
The needed libraries are in the requirement.txt

**Currently implemented**

- scrap the "appartement" research  result

**TODO**
- scrap the others  research result

### Commande :
In  the folder run in a terminal

``` scrapy runspider scrawler.py -o stocks.csv``` 

will save the result in a stock.csv file

Number of pages scrapped are changeable in getters.py
in the get_appartement_urls function.
