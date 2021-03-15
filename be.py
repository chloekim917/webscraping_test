# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import presence_of_element_located

# #This example requires Selenium WebDriver 3.13 or newer
# with webdriver.Chrome() as driver:
#     wait = WebDriverWait(driver, 10)
#     driver.get("https://google.com/ncr")
#     driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
#     first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3>div")))
#     print(first_result.get_attribute("textContent"))





# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()

# url = 'http://textfiles.com/stories/alissadl.txt'

# driver.get(url)

# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,'u_cbox_area')))

# html =  BeautifulSoup(driver.page_source, "html.parser")

# result = html.find_all("span",{"class":"u_cbox_contents"})
# for item in result:
#     print(item.text)





from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

url = 'http://textfiles.com/stories/alissadl.txt'
driver.get(url)

html =  BeautifulSoup(driver.page_source, "html.parser")

for item in html:
    actual_text=item.text

print(len(actual_text))




