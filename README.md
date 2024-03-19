# WEB-CRAWLER

Overview
This Python script implements a recursive web crawler that explores web pages up to a specified maximum depth. It utilizes the requests library to fetch web pages and the BeautifulSoup library to parse the HTML content, extracting links for further exploration. The crawler operates in a depth-first manner, printing the URLs it encounters along the way.

Features
- Recursive Crawling: The crawler traverses web pages recursively, exploring links up to a specified maximum depth.
- URL Extraction: Extracts URLs from the HTML content of each page, allowing for further exploration.
- Error Handling: Robust error handling ensures the script gracefully handles any encountered errors during crawling.
