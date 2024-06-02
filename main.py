import requests
import selectorlib
import emailSender

URL = "http://programmer100.pythonanywhere.com/tours/"


def scrape(url):
    """Scrape data from web page."""
    response = requests.get(url)
    source = response.text
    return source


def extractor(source):
    """extract the specific data using yaml file from the source"""
    extract_instance = selectorlib.Extractor.from_yaml_file("script.yaml")
    extracted = extract_instance.extract(source)["tours"]
    return extracted


if __name__ == "__main__":
    source = scrape(URL)
    extracted_data = extractor(source)
    if extracted_data.title() != "No Upcoming Tours":
        emailSender.send_email()




