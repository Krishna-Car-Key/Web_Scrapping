import time
import requests
import selectorlib
import emailSender
import sqlite3

URL = "http://programmer100.pythonanywhere.com/tours/"
Connection = sqlite3.connect("data.db")


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


def get_data(extracted):
    row = extracted.split(",")
    row = [item.strip("") for item in row]
    band, city, date = row
    cursor = Connection.cursor()
    result = cursor.execute("SELECT * FROM tours WHERE band=? AND city=? AND date=?",
                            (band, city, date))
    result = result.fetchall()
    return result


def write_data(extracted):
    row = extracted.split(",")
    row = [item.strip("") for item in row]
    band, city, date = row
    cursor = Connection.cursor()
    cursor.execute("INSERT INTO tours VALUES(?,?,?)", (band, city, date))
    Connection.commit()


while True:
    source = scrape(URL)
    extracted_data = extractor(source)
    if extracted_data.title() != "No Upcoming Tours":
        data = get_data(extracted_data)
        if not data:
            write_data(extracted_data)
            emailSender.send_email(user_mail="user@gmail.com", message=extracted_data)
    time.sleep(2)




