import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv

def webpage(source):
    all_records = []
    for i in range(2,8):
        source = 'https://reviews.webmd.com/drugs/drugreview-1027-dexamethasone-oral'
        url = f'{source}?conditionid=&sortval=1&page={i}&next_page=true'
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        
        records = soup.find_all('p', class_ = "description-text")
        
        for record in records:
            all_records.append(record.text)

    return all_records
# with open('comments.csv', 'w', newline='') as myfile:
#      wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#      wr.writerow(all_records)

# df = pd.DataFrame(all_records, columns = ['comments'])
# df.to_csv('comments.csv')