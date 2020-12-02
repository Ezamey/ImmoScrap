# ImmoScrap 

### By:
- Axelle Paquet
- Julien Bert
- Christian Melot


_PoweredBy_:

[![N|Solid](https://res.cloudinary.com/practicaldev/image/fetch/s--xYNk7vjX--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://thepracticaldev.s3.amazonaws.com/i/dpf1jzsiy8n1tmdfxn1v.jpg)](https://nodesource.com/products/nsolid)

ImmoScrap is  script using scrapy and  BeautifulSoup to scrap data from the Immoweb.be site.

**Currently implemented**

- Scrap the apartment and house for sale in Belgium
- Save the result in a CSV file
- Clean the result

**TODO**
- Scrap the others  research result


## Python Libraries

The needed libraries are in the `requirement.txt`.
To install it, use the command below:

```python -m pip install -r requirements.txt```

*Links to the official documentation of libraries :*
- [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/)
- [Scrapy](https://docs.scrapy.org/en/latest/)
- [Pandas](https://pandas.pydata.org/docs/reference/index.html#api)


## Usage 
- <u>*How to scrap*</u>


In  the folder "scraper" run in a terminal :

``` scrapy runspider scrawler.py -o stocks.csv``` 

Will save the result in a `stock.csv` file


- <u>*How to clean the csv*</u>

If you want, you can clean the csv to remove irrelevant data and harmonize the remaining data.
To do that, just run the `cleaning.ipynb` file in your favorite IDE.
The data are then saved in the `quick_clean.csv` file (This is the csv to use)

The available field are:
```
-  id
-  type
-  subtype
-  price
-  transactionType
-  zip
-  visualisationOption
-  cuisine_type
-  constructionYear
-  condition
-  heatingType
-  room_number
-  atticExists
-  basementExists
-  hasSwimmingPool
-  short_id
-  company_name
-  mètres carrés
-  commune
```

<hr>
02/12/2020