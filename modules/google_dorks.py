import requests
from bs4 import BeautifulSoup
from urllib.parse import quote, unquote
from utils.ui import print_dork, print_error
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

DORKS = [
    'site:quikr.com intext:"{query}"',
    'site:sulekha.com intext:"{query}"',
    'site:justdial.com intext:"{query}"',
    'site:naukri.com intext:"{query}"',
    'site:indiamart.com intext:"{query}"',
    'site:99acres.com intext:"{query}"',
    'site:magicbricks.com intext:"{query}"',
    'site:olx.in intext:"{query}"',
    'site:click.in intext:"{query}"',
    'site:mobikwik.com intext:"{query}"',
    'site:paytm.com intext:"{query}"',
    'site:truelancer.com intext:"{query}"',
    'site:github.com intext:"{query}"',
    'site:pastebin.com intext:"{query}"',
    'site:linkedin.com intext:"{query}"',
    'site:facebook.com intext:"{query}"',
    'site:twitter.com intext:"{query}"',
    'site:telegram.me intext:"{query}"',
    'site:telegram.dog intext:"{query}"',
    'site:t.me intext:"{query}"'
]

def duckduckgo_search(query):
    try:
        encoded_query = quote(query)
        url = f"https://html.duckduckgo.com/html/?q={encoded_query}"
        res = requests.get(url, headers=HEADERS, timeout=10)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, 'html.parser')
        results = []

        links = soup.find_all("a", class_="result__a")
        snippets = soup.find_all("a", class_="result__snippet")

        for i, link in enumerate(links):
            raw_url = link.get("href", "")
            if "uddg=" in raw_url:
                encoded_url = raw_url.split("uddg=")[-1]
                decoded_url = unquote(encoded_url)
            else:
                decoded_url = raw_url

            snippet = snippets[i].text.strip() if i < len(snippets) else ""
            results.append({
                "query": query,
                "url": decoded_url,
                "snippet": snippet
            })

        return results

    except Exception as e:
        print_error(f"Failed to fetch results for: {query}")
        print_error(str(e))
        return []

def run_dork_scan(number):
    all_results = []
    for dork in DORKS:
        actual_query = dork.replace("{query}", number)
        results = duckduckgo_search(actual_query)

        for result in results:
            print_dork(result["query"], result["url"], result.get("snippet"))
            all_results.append(result)

        time.sleep(1.5)  # Delay to avoid getting blocked

    return all_results
