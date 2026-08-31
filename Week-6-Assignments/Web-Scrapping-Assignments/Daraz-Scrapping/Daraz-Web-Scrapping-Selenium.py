import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

url = 'https://www.daraz.pk/catalog/?spm=a2a0e.tm80331704.cate_5.5.77cc5aa7fPImi7&q=Smart%20Phones&from=hp_categories&src=all_channel'

driver = webdriver.Chrome()

driver.get(url)

smart_phones_list = list()

smart_phones = driver.find_element(By.CSS_SELECTOR, 'div._17mcb')
for smart_phone in smart_phones.find_elements(By.CSS_SELECTOR, 'div.Bm3ON'):
    smart_phone_dictionary = dict()
    try:
        title = smart_phone.find_element(By.CSS_SELECTOR, 'div.RfADt a')
        smart_phone_dictionary['Title'] = title.get_attribute('title') 
    except NoSuchElementException:
        smart_phone_dictionary['Title'] = 'NA'
    try:
        img = smart_phone.find_element(By.CSS_SELECTOR, 'div.picture-wrapper.jBwCF img')
        smart_phone_dictionary['Image'] = img.get_attribute('src')
    except NoSuchElementException:
        smart_phone_dictionary['Image'] = 'NA'
    try:
        price = smart_phone.find_element(By.CSS_SELECTOR, 'div.aBrP0 span.ooOxS')
        smart_phone_dictionary['Price'] = price.text.strip().split()[1] 
    except NoSuchElementException:
        smart_phone_dictionary['Price'] = 'NA'
    try: 
        origin = smart_phone.find_element(By.CSS_SELECTOR, 'div._6uN7R span.oa6ri ')
        smart_phone_dictionary['Origin'] = origin.text.strip() 
    except NoSuchElementException:
        smart_phone_dictionary['Origin'] = 'NA'
    try:
        coins_saved_rs = smart_phone.find_element(By.CSS_SELECTOR, 'div.WNoq3 span.ic-dynamic-badge.ic-dynamic-badge-text')
        smart_phone_dictionary['Coins saved Rs'] = coins_saved_rs.text.strip().split()[-1]
    except NoSuchElementException:
        smart_phone_dictionary['Coins saved Rs'] = 'NA'
    try:
        discount = smart_phone.find_element(By.CSS_SELECTOR, 'div.WNoq3 span.IcOsH')
        smart_phone_dictionary['Discount'] = discount.text.strip().split()[0]
    except NoSuchElementException:
        smart_phone_dictionary['Discount'] = 'NA'

    smart_phones_list.append(smart_phone_dictionary)

driver.quit()

df = pd.DataFrame(smart_phones_list)

print(df)

# df.to_csv('Daraz-Selenium.csv', index=False)