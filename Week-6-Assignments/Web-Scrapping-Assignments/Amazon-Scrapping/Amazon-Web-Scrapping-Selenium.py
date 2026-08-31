from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
driver = webdriver.Chrome()
driver.get('https://www.amazon.com/gp/browse.html?node=6563140011&ref_=nav_em_amazon_smart_home_0_2_8_2')
time.sleep(10)
try: 
    smart_home_products =  driver.find_element(By.CSS_SELECTOR, 'div._Y29ud_bxcGridContainer_2u9rb._Y29ud_bxcGridContainerWidth1500_36D4w._Y29ud_bxcGridmpGutterLayout_2hYHk')
    print(smart_home_products.get_attribute('innerHTML'))
except NoSuchElementException:
    print('NA')
driver.quit()