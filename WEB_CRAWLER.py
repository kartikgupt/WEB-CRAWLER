import requests
from bs4 import BeautifulSoup

def crawl(url, depth=1, max_depth=5):
    if depth > max_depth:
        return

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Crawling {url} (depth={depth})")
            soup = BeautifulSoup(response.text, 'html.parser')
            # Process the page content here, such as extracting links, data, etc.
            # For example, printing all links on the page:
            for link in soup.find_all('a', href=True):
                print(link['href'])
                crawl(link['href'], depth + 1, max_depth)
        else:
            print(f"Failed to crawl {url}: {response.status_code}")
    except Exception as e:
        print(f"Error crawling {url}: {str(e)}")

# Example usage:
crawl('https://example.com', max_depth=2)