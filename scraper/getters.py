from requests import get
from datetime import datetime

def get_appartement_urls() -> list:
    '''function to get urls from the 'a-vendre' section'''
    detail_urls = []
    for i in range(300):
        url = f"https://www.immoweb.be/fr/search-results/appartement/a-vendre?countries=BE&page={i}&orderBy=relevance"#génère une nouvelle url =égale une nouvelle page de recherche
        response = get(url)
        source = None
        if response.status_code == 200:
            source = response.json()

        if source:
            results = source["results"]
            for j in range(len(results)):
                id_ = results[j]["id"]
                locality = results[j]["property"]["location"]["locality"]
                postal_code = results[j]["property"]["location"]["postalCode"]

                detail_urls.append(
                    f"https://www.immoweb.be/fr/annonce/appartement/a-vendre/{locality}/{postal_code}/{id_}")#récupère toutes les liens sur la page de recherche
    return detail_urls
