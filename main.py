import requests
import selectorlib

URL = "http://programmer100.pythonanywhere.com/tours/"


def scrape(url):
    """Scrape data from web page."""
    response = requests.get(url)
    source = response.text
    return source


def extractor(source):
    """extract the specific data using yaml file from the source"""
    extract = selectorlib.Extractor.from_yaml_file("script.yaml")
    extracted = extract.extract(source)["tours"]
    return extracted


if __name__ == "__main__":
    source = scrape(URL)
    extractor(source)

