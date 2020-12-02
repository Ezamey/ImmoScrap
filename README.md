# ImmoScrap 

### By:
- Axelle Paquet
- Julien Bert
- Christian Melot


_PoweredBy_:

[![N|Solid](https://res.cloudinary.com/practicaldev/image/fetch/s--xYNk7vjX--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://thepracticaldev.s3.amazonaws.com/i/dpf1jzsiy8n1tmdfxn1v.jpg)](https://nodesource.com/products/nsolid)

ImmoScrap is  script using scrapy and  BeautifulSoup to scrap data from the Immoweb.be site.

**Currently implemented**

- scrap the apartment and house for sale in Belgium
- Save the result in a CSV file
- Clean the result

**TODO**
- scrap the others  research result


## Python Libraries

The needed libraries are in the requirement.txt


## Usage 
- <u>*How to scrap*</u>


In  the folder "scraper" run in a terminal :

``` scrapy runspider scrawler.py -o stocks.csv``` 

will save the result in a stock.csv file


- <u>*How to clean the csv*</u>

If you want, you can clean the csv to remove irrelevant data and harmonize the remaining data.
To do that, just run the cleaning.ipynb file in your favorite IDE.
The data are then saved in the "quick_clean.csv" file (This is the csv to use)

The available field are:

1. id
1. type
1. subtype
1. price
1. transactionType
1. zip
1. visualisationOption
1. cuisine_type
1. constructionYear
1. condition
1. heatingType
1. room_number
1. atticExists
1. basementExists
1. hasSwimmingPool
1. short_id
1. company_name
1. mètres carrés
1. commune

<hr>
02/12/2020