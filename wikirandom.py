import requests
from bs4 import BeautifulSoup
import csv

# Set the url we want
url = 'https://en.wikipedia.org/wiki/Special:Random'

# headers for csv file
headers = ['Title', 'Link', 'Categories']

with open('results.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # write the headers
    writer.writerow(headers)

    while True:
        r = requests.get(url)
        content = r.text  # content of wikipedia page
        soup = BeautifulSoup(content, 'html.parser')
        title = soup.find(id="firstHeading").get_text()  # title of wikipedia page
        link = soup.find("link", {'rel': 'canonical'})['href']  # link to wikipedia page
        catsoup = soup.find("div", {'id': 'mw-normal-catlinks'}).find('ul')
        categories = []  # list of categories

        print(title)
        print(link)
        for li in catsoup:
            categories.append(li.text)

        print(categories)

        data = [title, link]  # set data in list

        for x in categories:
            data.append(x)

        writer.writerow(data)  # write data
