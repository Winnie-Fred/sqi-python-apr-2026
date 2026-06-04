import requests

from bs4 import BeautifulSoup

url = "http://books.toscrape.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.find("h1"))
# print(soup.find_all("h1"))
# print(soup.find_all("p"))

articles = soup.select("li article.product_pod")
number_of_books = len(articles)
print(f"Number of books: {number_of_books}")

prices_p = soup.select("div.product_price p.price_color")

prices = [float(price_p.text[2:]) for price_p in prices_p]

print(prices)



total_price = sum(prices)
avg_price = round(total_price / number_of_books, 2)
print(f"Average price: {avg_price}")

# Find the most expensive book

a_title_tags = soup.select("li article.product_pod h3 a")

books = {title_tag["title"]: price for title_tag, price in zip(a_title_tags, prices)}

print(books)

most_expensive_book = max(books, key=books.get)
print(f"Most expensive book: {most_expensive_book}")