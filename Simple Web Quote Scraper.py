import requests
from bs4 import BeautifulSoup

def scrape_quotes(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('span', class_='text')

    if not quotes:
        print("No quotes found.")
        return

    print("Famous Quotes:")
    for i, quote in enumerate(quotes[:10], 1):  # Limiting to first 10 quotes
        print(f"{i}. {quote.get_text(strip=True)}")

if __name__ == "__main__":
    scrape_quotes("https://quotes.toscrape.com/")
