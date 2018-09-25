# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 13:09:38 2018

@author: Harsh Kava
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import re,time,os,codecs

def login(username,password):
    #access website
    try:
        driver.get('https://www.facebook.com/')
        
        #Accessing Login frame
        form=driver.find_element_by_id('login_form')
        form.click()
        
        #Entering email details
        email = form.find_element_by_id('email')
        email.send_keys(username)
        #time.sleep(1)
        
        #Entering password details
        pwd = form.find_element_by_id('pass')
        pwd.send_keys(password)
        time.sleep(1)
        
        #Clicking the login button
        button=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'loginbutton')))
        button.click()
        
    except Exception as e:
        print('Exception encountered during Login')
        print(e)
        
def scrapAndSaveData():
     try:
         driver.get("https://www.facebook.com/pg/ATT/community/?ref=page_internal")
         time.sleep(3)
        
         # Selenium script to scroll to the bottom, wait 3 seconds for the next batch of data to load, then continue scrolling.  It will continue to do this until the page stops loading new data.
         lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
         noOfPageScrolls=0
         while(noOfPageScrolls < 10):
             print("noOfPageScrolls: ",noOfPageScrolls)
             time.sleep(3)
             lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
             print(lenOfPage)
             noOfPageScrolls=noOfPageScrolls+1
         
         # Now that the page is fully scrolled, grab the source code.
         source_data = driver.page_source
         
         # Passing page source into BeautifulSoup to start parsing
         bs_data = bs(source_data)
     
     except Exception as e:
        print('Exception getting the Page Source')
        print(e)
     
     try:
         with codecs.open('Att_reviews.html', 'w',encoding='utf8') as fw: fw.write(str(bs_data))
         fw.close()
     except Exception as e:
        print('Exception writing the Page Source into File')
        print(e)
      

driver = webdriver.Chrome()
login("######","######")   # use your email address and password to login
scrapAndSaveData()





