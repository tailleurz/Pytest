#!/usr/bin/env python
# coding: utf-8

# In[11]:


import time
import pyperclip
import requests
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--ignore-local-proxy")
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("https://www.google.com")
time.sleep(3)

driver.find_element(By.CLASS_NAME, 'gLFyf').click()
driver.find_element(By.CLASS_NAME, 'gLFyf').send_keys('블랙핑크')
driver.find_element(By.CLASS_NAME, 'gLFyf').send_keys(Keys.ENTER)

def search():
    search = search_name
    
def result():
    result = driver.find_element(By.CSS_SELECTOR, "[value = '블랙핑크']")

def test_search_google():
    if search == result:
        assert true
    else:
        print('error')


# In[ ]:




