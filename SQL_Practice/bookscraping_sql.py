import sqlite3
import requests
from bs4 import BeautifulSoup


def requestURL(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article")
    library = []
    for book in books:
        bookData = (
            getTitle(book),
            getPrice(book),
            getRating(book)
        )
        library.append(bookData)
    return library

def getTitle(book):
    title = book.find("h3").find("a")["title"]
    return title


def getPrice(book):
    price = book.find(class_="price_color").get_text()
    fPrice = float(price.replace("Â£", ""))
    return fPrice


def getRating(book):
    rating = book.find(class_="star-rating").get_attribute_list("class")[1]
    ratingDict = {
        "Zero": 0,
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    fRating = ratingDict[rating]
    return fRating

def saveData(url):
    conn = sqlite3.connect("books.db")
    c = conn.cursor()
    # c.execute('''CREATE TABLE books
    #     (title TEXT, price REAL, rating INTEGER)''')
    c.executemany('INSERT INTO books VALUES (?,?,?)', requestURL(url))
    conn.commit()
    conn.close()

# Save data to database

saveData("http://books.toscrape.com/catalogue/category/books/history_32/index.html")