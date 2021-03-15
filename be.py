from selenium import webdriver
from bs4 import BeautifulSoup
import re

driver = webdriver.Chrome()

url = 'http://textfiles.com/stories/alissadl.txt'
driver.get(url)

html =  BeautifulSoup(driver.page_source, "html.parser")

for item in html:
    actual_text=item.text

# print(len(actual_text))
driver.close() 

def freq(actual_text): 
  
    #eliminate special characters except
    new_string = re.sub(r'[^a-zA-Z0-9 ]','',actual_text)
    # break the string into list of words
    str_list = new_string.casefold().split()

  
    # gives set of unique words 
    unique_words = set(str_list) 
      
    for words in unique_words : 
        print(words,':', str_list.count(words)) 
  
# driver code 
if __name__ == "__main__": 
    actual_text
    # calling the freq function 
    freq(actual_text) 



