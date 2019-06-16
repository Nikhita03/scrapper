from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

def getContents(my_url):
    uClient = ureq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findaAll("div", (""))

    print(len(containers))

    container = containers[0]

    filename = "council.csv"

    f = open(filename, "w")
    headers = "ward\n"
    f.write(headers)

    for container in containers:
        ward_container = container.findAll("div", (""))
        ward = ward_container[0].text.strip()
        print("ward" + ward)

for x in range(1, 4):
   my_url = ""
   getContents(my_url)



