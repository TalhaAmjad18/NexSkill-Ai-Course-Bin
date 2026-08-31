import pandas as pd
from bs4 import BeautifulSoup

with open(r'Week-6-Assignments/Web-Scrapping-Assignments/Amazon-Scrapping/Smart Home Devices & Systems.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html5lib')

devices_list = []

smart_home_devices = soup.find('ol', class_="a-carousel")
for device in smart_home_devices.find_all('li',class_="a-carousel-card ucw-widget-carousel-element"):
    devices_dictionary = {}
    title = device.find('span', class_="a-truncate-cut")
    devices_dictionary['Title'] = title.text if title else 'NA'
    img = device.find('img', class_="ucw-widget-product-card-image")
    devices_dictionary['Image'] = img.get('src') if img else 'NA'
    symbol = device.find('span', class_="a-price-symbol")
    price_whole = device.find('span', class_="a-price-whole")
    price_fraction = device.find('span', class_="a-price-fraction")
    devices_dictionary['Price'] = symbol.text + price_whole.text + "." + price_fraction.text
    reviews = device.find('span', class_="a-size-base a-color-secondary")
    devices_dictionary['Reviews'] = reviews.text if reviews else 'NA'
    rating = device.find('span', class_="a-icon-alt")
    devices_dictionary['Rating'] = rating.text.split()[0] if rating else 'NA'
    devices_list.append(devices_dictionary)

rows = soup.find_all('div', class_="_Y29ud_bxcGridRow_Zu5i8")
for row in range(1, len(rows)):
    for device in rows[row].find_all('div', class_="_Y29ud_bxcGridColumn_J5gfU _Y29ud_bxcGridColumn1Of5_UoKNf"):
        devices_dictionary = {}
        title = device.img.get('alt')
        devices_dictionary['Title'] = title if title else 'NA'
        img = device.img.get('src')
        devices_dictionary['Image'] = img if img else 'NA'
        devices_list.append(devices_dictionary)
        
df = pd.DataFrame(devices_list)
print(df)
# df.to_csv('Amazon-BeautifulSoup.csv', index=False)