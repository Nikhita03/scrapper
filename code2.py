#CODE FOR SINGLE PAGE WEBSITE
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

#INSERT MAIN URL IN  HERE ""
my_url = ""

uClient = ureq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", (""))
#INSERT DIV CLASS ABOVE IN ""

print(len(containers))

    # print(soup.prettify(containers[0]))

container = containers[0]

filename = "council.csv"

f = open(filename, "w")
headers = "ward\n"
f.write(headers)

#INSERT SUB DIV CLASS IN HERE ""
for container in containers:
    ward_container = container.findAll("div", (""))
    ward = ward_container[0].text

    print("ward:" + ward)


#for x in range(1, 4):

    #getContents(my_url)


