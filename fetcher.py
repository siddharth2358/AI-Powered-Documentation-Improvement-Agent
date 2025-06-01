import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/122.0.0.0 Safari/537.36"
}

def fetch_article_content(url):
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.text

def extract_text_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    content_div = soup.find('div', class_='article-body') or soup.body
    return content_div.get_text(separator='\n') if content_div else soup.get_text()

if __name__ == "__main__":
    test_url = input("Enter article URL: ")
    html = fetch_article_content(test_url)
    print(extract_text_from_html(html)[:1000])
