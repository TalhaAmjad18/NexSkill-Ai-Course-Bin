from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

url = 'https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094'

def getData(tag,selector):
    try:
        x = tag.find_element(By.CSS_SELECTOR, selector)
        return x
    except NoSuchElementException:
        return 'NA'

driver = webdriver.Chrome()
driver.get(url)

time.sleep(10)

# WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located(
#         (By.CSS_SELECTOR, "ul.brwrvr__item-results.brwrvr__item-results--list")
#     )
# )

cell_phones_list = list()
cell_phones = driver.find_element(By.CSS_SELECTOR, 'ul.brwrvr__item-results.brwrvr__item-results--list')
for cell_phone in cell_phones.find_elements(By.CSS_SELECTOR, 'li.brwrvr__item-card'):
    cell_phone_dictionary = dict()
    cell_phone_dictionary['Title'] = getData(cell_phone, 'h3.textual-display.bsig__title__text').text.strip()
    cell_phone_dictionary['Price'] = getData(cell_phone, 'span.textual-display.bsig__price.bsig__price--displayprice').text.strip()
    cell_phone_dictionary['Image'] = getData(cell_phone, 'a.brwrvr__item-card__image-link img.brwrvr__item-card__image').get_attribute('src')
    try:
        cell_phone_dictionary['Status'] = cell_phone.find_elements(By.CSS_SELECTOR, 'span.textual-display.bsig__generic.bsig__listingCondition.secondary')[0].text.strip()
    except IndexError:
        cell_phone_dictionary['Status'] = 'NA'
    try:
        cell_phone_dictionary['Company'] = cell_phone.find_elements(By.CSS_SELECTOR, 'span.textual-display.bsig__generic.bsig__listingCondition.secondary')[-1].text.strip()
    except IndexError:
        cell_phone_dictionary['Company'] = 'NA'
   
    cell_phones_list.append(cell_phone_dictionary)

df = pd.DataFrame(cell_phones_list)

print(df)

# df.to_csv('Ebay-Selenium.csv', index=False)