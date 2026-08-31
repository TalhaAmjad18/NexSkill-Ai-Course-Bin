import pandas as pd
from bs4 import BeautifulSoup

cell_phones_list = list()

with open(r'Week-6-Assignments/Web-Scrapping-Assignments/Ebay-Scrapping/Cell Phones & Smartphones _ eBay.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html5lib')

cell_phones = soup.select_one('ul.brwrvr__item-results.brwrvr__item-results--list')
for cell_phone in cell_phones.select('li.brwrvr__item-card--list'):
    cell_phone_dictionary = dict()
    title = cell_phone.select_one('h3.textual-display.bsig__title__text')
    cell_phone_dictionary['Title'] = title.text.strip() if title else 'NA'
    price = cell_phone.select_one('span.textual-display.bsig__price.bsig__price--displayprice')
    cell_phone_dictionary['Price'] = price.text.strip().replace('to','-') if price else 'NA'
    img = cell_phone.select_one('img.brwrvr__item-card__image')
    cell_phone_dictionary['Image'] = img['src'] if img else 'NA'
    rating = cell_phone.select_one('div.star-rating')
    cell_phone_dictionary['Rating'] = rating['aria-label'].split()[0] if rating else 'NA'
    cell_phones_list.append(cell_phone_dictionary)

df = pd.DataFrame(cell_phones_list)
print(df)
# df.to_csv('Ebay-BeautifulSoup.csv', index=False)