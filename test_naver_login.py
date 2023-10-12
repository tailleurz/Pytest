#!/usr/bin/env python
# coding: utf-8

# In[3]:


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

driver.get("https://www.naver.com")
time.sleep(3)

driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div/a').click()
time.sleep(3)

id = 'Naver ID'
password = 'Naver Password'

pyperclip.copy(id)
driver.find_element(By.CLASS_NAME, "input_text").send_keys(Keys.CONTROL, 'v')
time.sleep(3)

pyperclip.copy(password)
driver.find_element(By.NAME, "pw").send_keys(Keys.CONTROL, 'v')
time.sleep(3)

driver.find_element(By.CLASS_NAME, "btn_login").click()
time.sleep(3)

CURL = driver.current_url


def test_url():
    try:
        driver.find_element(By.ID, 'new.dontsave').click()
        time.sleep(1)

    except:
        pass

if CURL == 'https://www.naver.com':
    assert 1
else:
    print('error')

time.sleep(3)


# In[ ]:




