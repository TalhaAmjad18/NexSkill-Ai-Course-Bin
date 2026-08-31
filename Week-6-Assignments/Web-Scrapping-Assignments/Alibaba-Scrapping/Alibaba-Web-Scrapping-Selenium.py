from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://www.alibaba.com/trade/search?spm=a2700.product_home_newuser.header.132.2ce267afSeLPmg&SearchText=Auto+Accessories&indexArea=product_en&search_cource_scene=pc_home_product_category&has4Tab=true&tab=all')

def getData(tag, css_selector):
    try:
        x = tag.find_element(By.CSS_SELECTOR, css_selector)
        return x
    except NoSuchElementException:
        return "NA"

auto_accessories_list = list()

auto_accessories = getData(driver, 'div[data-content="abox-ProductNormalList"]')
for auto_accessory in auto_accessories.find_elements(By.CSS_SELECTOR, 'div.fy26-product-card-wrapper.list-card.fy26-product-card.searchx-offer-item'):
    auto_accessory_dictionary = dict()
    title = getData(auto_accessory, 'h2.searchx-product-e-title a span')
    auto_accessory_dictionary['Title'] = title.text.strip()
    link = getData(auto_accessory, 'h2.searchx-product-e-title a')
    auto_accessory_dictionary['Link'] = link.get_attribute('href')
    price = getData(auto_accessory, 'div.searchx-product-price-price-main')
    auto_accessory_dictionary['Price'] = price.text.replace('PKR', '').strip()
    min_order = getData(auto_accessory, 'div.searchx-moq')
    auto_accessory_dictionary['Minimum Order'] = ''.join([ i for i in min_order.text if i.isdigit() ])
    img = getData(auto_accessory, 'div.searchx-product-e-slider__wrapper a img')
    auto_accessory_dictionary['Image'] = img.get_attribute('src')

    auto_accessories_list.append(auto_accessory_dictionary)

driver.quit()

df = pd.DataFrame(auto_accessories_list)

print(df)

# df.to_csv('Alibaba-Selenium.csv', index=False)