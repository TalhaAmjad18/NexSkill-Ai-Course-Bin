import pandas as pd
from bs4 import BeautifulSoup

with open(r'Week-6-Assignments\Web-Scrapping-Assignments\Daraz-Scrapping\Buy Smart Phones Online at Best Price in Pakistan - Daraz.pk.html', 'r', encoding='utf-8') as f:
    soup =  BeautifulSoup(f, 'html5lib')

smart_phones_list = list()

smart_phones = soup.find('div', class_="_17mcb")
for smart_phone in smart_phones.find_all('div', class_="Bm3ON"):
    smart_phone_dictionary = dict()
    title = smart_phone.find('div', class_="RfADt")
    smart_phone_dictionary['Title'] = title.a.text if title and title.a else 'NA'
    image = smart_phone.find('div', class_="picture-wrapper jBwCF")
    smart_phone_dictionary['Image'] = image.img.get('src') if image and image.img else 'NA'
    price = smart_phone.find('div', class_="aBrP0")
    smart_phone_dictionary['Price'] = price.span.text if price and price.span else 'NA'
    discount = smart_phone.find('div', class_="WNoq3")
    smart_phone_dictionary['Discount'] = discount.span.text if discount and discount.span else 'NA'
    origin = smart_phone.find('div', class_="_6uN7R")
    smart_phone_dictionary['Origin'] = origin.span.text if origin and origin.span else 'NA'
    smart_phones_list.append(smart_phone_dictionary)

df = pd.DataFrame(smart_phones_list)
print(df)
# df.to_csv('Daraz-BeautifulSoup.csv', index=False)