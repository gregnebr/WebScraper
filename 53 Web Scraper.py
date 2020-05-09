#code by Cory Althoff  from Self Taught Programmer Python Course
#key parts of the code are from Self Taught Programmer Python course  May 2020
#edits to the code by glc May 8 2020

import urllib.request
import urllib.error
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        print("Scraping... ")
        #assume the web url starts with https://
        h_site = "https://"+self.site
        try:
            r = urllib.request.urlopen(h_site)
        except urllib.error.URLError:
            h_site = "http://"+self.site
            try:
                r = urllib.request.urlopen(h_site)
            except urllib.error.URLError:
                print("Could not open ",self.site)
                return

        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        print("Scraping .... web site has been read...")
        # only search for anchor tags once and put the href values in a list
        # map takes in a lambda function and things to apply the function to
        urls = map(lambda tag: tag.get("href"), sp.find_all("a"))
        # list comprehension to collect just the urls that contain http
        http_urls = [url for url in urls if "http" in url]
        print("http links follow: \n")
        # join using the line separator character to have each on its own line
        print("\n".join(http_urls))
        non_http_urls = [url for url in urls if "http" not in url]
        if non_http_urls:
            print("\nNon-http Links follow: \n")
            print("\n".join(non_http_urls))
        else:
            print("\nNo non-http links were found\n")

        html_urls = [url for url in urls if "html" in url]
        if html_urls:
            print("\nLinks that have  'html'  ")
            print("\n".join(html_urls))
        else:
            print("\nNo html links were found\n")

        print("\nAt this page there are ",len(http_urls),
            " http links .... and ", len(non_http_urls),
            " non_http links ... and ",len(html_urls),
            " links with 'html.'")

#begin execution
target_url = input("Enter url, do  NOT  include http:// or https:// ")
print("Links found at "+target_url)

test = Scraper(target_url)
test.scrape()
