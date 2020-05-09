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
        print("Scraping ... ")
        n_http_no = 0
        n_http = 0
        n_html = 0
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
        print("http links follow: ")
        for tag in sp.find_all("a"):    #added by glc
            url = tag.get("href")
            try:
                if "http" in url:
                    n_http += 1
                    print(url)
            except TypeError:
                continue

        print("\nNon-http Links follow: ")
        for tag in sp.find_all("a"):    #added by glc
            url = tag.get("href")
            try:
                if "http" not in url:
                    n_http_no += 1
                    print(url)       #this print was not in the code suggested by the course author
                              #this prints links to other web pages
            except TypeError:
                continue

        if n_http_no == 0:
            print("        No non-http links were found\n")

        print("\nLinks that have  'html'  ")
        for tag in sp.find_all("a"):   # this loop prints urls with html in the link
            url = tag.get("href")
            if url is None:
                continue

            try:
                if "html" in url:
                    n_html += 1
                    print(url)
            except TypeError:
                continue

        if n_html == 0:
            print("          No html links were found\n")

        print("\nAt this page there are ",n_http, " http links .... and ", n_http_no," non_http links ... and ",n_html, " links with 'html.'")


#begin execution
target_url = input("Enter url, do  NOT  include http:// or https:// ")
print("Links found at "+target_url)

test = Scraper(target_url)
test.scrape()
