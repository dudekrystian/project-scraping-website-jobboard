from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import math  
from datetime import date

today = date.today()


number_of_offers = [] 
number_of_spec = []


all_offers_url = "https://theprotocol.it/filtry/zdalna,hybrydowa,stacjonarna;rw"
all_specialization_url = "https://theprotocol.it/filtry/backend,devops,frontend,fullstack,gamedev,mobile,embedded,architecture,qa-testing,security,ai-ml,big-data-science,helpdesk,it-admin,agile,product-management,project-management,ux-ui,business-analytics,sap-erp,system-analytics;sp"

list = [all_offers_url, all_specialization_url]
table = []


page_to_scrape = requests.get(all_offers_url)
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
offers = soup.find('span', class_='tqbmuwc ss93d95 su6nd6p')
text = offers.text
text_without_brackets = re.sub(r"[\([{})\]]", "", text).split()
get_number = text_without_brackets[0]
number_offers = int(get_number)

page_to_scrape = requests.get(all_specialization_url)
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
offers = soup.find('span', class_='tqbmuwc ss93d95 su6nd6p')
text = offers.text
text_without_brackets = re.sub(r"[\([{})\]]", "", text).split()
get_number = text_without_brackets[0]
number_speciaization = int(get_number)

percent = number_speciaization / number_offers * 100
rounded_number = math.ceil(percent*100)/100  
table.append({rounded_number, str(today)})

df = pd.DataFrame(table)
df.to_csv('spec.csv', mode='a', index=False, header=False)
print('data add sucessfully!')









