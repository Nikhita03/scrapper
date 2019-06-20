from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

my_url = "http://www.apsec.gov.in/ELECTIONRESULTS/RESULTS%202014/Andhra%20Elected%20Corporators%20List,%202014.pdf"

uClient = ureq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", ("canvasWrapper"))

print(len(containers))

    # print(soup.prettify(containers[0]))

container = containers[0]

filename = "council.csv"

f = open(filename, "w")
headers = "ward\n"
f.write(headers)

for container in containers:
    ward_container = container.findAll("div", ("textLayer"))
    ward = ward_container[0].text

    print("ward:" + ward)


#for x in range(1, 4):

    #getContents(my_url)


