import pandas as pd
from bs4 import BeautifulSoup

productsList = []

with open(r'Week-6-Assignments/Web-Scrapping-Assignments/Alibaba-Scrapping/Alibaba.com.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html5lib')

products = soup.find('div', class_="organic-list app-organic-search-mb-20 viewtype-list")
for product in products.find_all('div', class_="fy26-product-card-wrapper list-card fy26-product-card searchx-offer-item"):
    productDictionary = dict()
    title = product.find('h2', class_="searchx-product-e-title")
    productDictionary['Title'] = title.a.span.text if title and title.a and title.a.span else 'NA'
    price = product.find('div', class_="searchx-product-price-price-main")
    productDictionary['Price'] = price.text if price else 'NA'
    minOrder = product.find('div', class_="searchx-moq")
    productDictionary['Min Order'] = minOrder.text.split(':')[-1] if minOrder else 'NA'
    img = product.find('div', class_="searchx-product-e-slider__wrapper")
    productDictionary['Img'] = img.a.img.get('src') if img and img.a and img.a.img else 'NA'
    link = product.find('div', class_="searchx-product-area supplier-area-layout")
    productDictionary['Link'] = link.a.get('href') if link and link.a else 'NA'
    productsList.append(productDictionary)

df = pd.DataFrame(productsList)

print(df)

# df.to_csv('Alibaba-BeautifulSoup.csv', index=False)