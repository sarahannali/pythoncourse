import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

with open("webscraping_practice.csv","w",newline="") as csvFile:
    csv_writer = writer(csvFile)
    csv_writer.writerow(["Title","Date","URL"])

    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text()
        url = a_tag["href"]
        date = article.find("time")["datetime"]
        csv_writer.writerow([title,date,url])