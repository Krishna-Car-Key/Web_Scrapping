import requests
import selectorlib

URL = "http://programmer100.pythonanywhere.com/tours/"


def scrape(url):
    """Scrape data from web page."""
    response = requests.get(url)
    source = response.text
    return source


if __name__ == "__main__":
    print(scrape(URL))
