import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    return soup.get_text()

if __name__ == "__main__":
    data = scrape_website("https://debales.ai")
    
    with open("data.txt", "w", encoding="utf-8") as f:
        f.write(data)