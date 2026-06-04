import requests

from bs4 import BeautifulSoup

url = "https://netflix.com.ng/"

try:
    response = requests.get(url)
except requests.exceptions.ConnectionError as e:
    print(f"You are not connected to the internet: {e}")
except requests.exceptions.RequestException as e:
    print("Something went wrong!")
else:

    soup = BeautifulSoup(response.text, "html.parser")

    status_code = response.status_code

    print(f"Status Code: {status_code}")

    with open("netflix-home.html", "w") as f:
        f.write(soup.prettify())



