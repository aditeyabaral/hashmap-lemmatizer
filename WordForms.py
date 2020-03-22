import requests
from bs4 import BeautifulSoup
url = r"https://www.worldclasslearning.com/english/five-verb-forms.html"
re = requests.get(url).text
soup = BeautifulSoup(re,"html")
f = open("VerbForms.csv","w")
#print(soup.prettify())
tables = soup.find_all("table")[1:]
d = dict()
for table in tables:
    trow = table.find_all("tr")
    for tr in trow:
        td = tr.find_all("td")
        d[td[0].text]=[]
        s = ""
        temp = []
        for j in td[1:]:
            print(j.text,end = ",")
            if j.text not in temp:
                s+=j.text+","
                d[td[0].text].append(j.text)
                temp.append(j.text)
        f.write(s+"\n")
        print("\n")
f.close()
