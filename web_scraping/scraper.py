import requests

from bs4 import BeautifulSoup

# url = "https://www.fiverr.com/"
url = "https://www.netflix.com/ng/"



try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print(f"Oops! Something went wrong: {e}")
else:
    status_code = response.status_code
    if status_code == 200:
            
        print(status_code)
        soup = BeautifulSoup(response.text, 'html.parser')

        with open("netflix-home-page.html", "w") as f:
            f.write(soup.prettify())
    else:
        print(f"Unexpected status code: {status_code}")
        print("Response:")
        print(response.text)

    
# CAPTCHA - Computer Aided Public Test to Tell Computers And Humans Apart

# Alan Turing came up with the Turing Test

# reCAPTCHA 

# DOS, DDOS - (Distributed) Denial Of Service