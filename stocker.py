import requests
from bs4 import BeautifulSoup


l = []

with open('ASX_codes.txt') as f:
    line = f.readline()
    while line:
        line = line.strip()
        l.append(line)


        line = f.readline()

print(l)

open_file = open('file_to_save.txt', 'w')
url = 'https://www.asx.com.au/asx/share-price-research/company/'
i = 0
while i < len(l):
    r = requests.get(url + l[i] + "/statistics/shares")
    r_html = r.text

    soup = BeautifulSoup(r_html, "lxml")

    for stats in soup.find_all(id="company-information"): 
        
        print(stats.get('href'))

        if stats.a: 
            print(str(stats.a.text.replace("\n\n", " ").encode('utf-8').strip()))
            open_file.write(str(stats.a.text.replace("\n\n", " ").encode('utf-8').strip()))
       
        open_file.write("\n")

open_file.close()
