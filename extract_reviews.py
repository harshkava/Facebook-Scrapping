# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 14:20:58 2018

@author: Harsh Kava
"""

from bs4 import BeautifulSoup
import re
import os
import csv

review_data=open('review.txt','w')

def fetchReview(soup):
    reviewChunk=soup.find('div',{'class':(re.compile("_5pbx userContent"))}) 
    print(reviewChunk)     
    if reviewChunk: review=reviewChunk.text.strip()
    print('*********************************')
    print(review)
    
    
    
file = "D:\\Courses\\04_Web Analytics\\Study Material\\At&t\\Att_reviews.html"
with open(file, 'rb') as html:
    soup = BeautifulSoup(html, "lxml")
    fetchReview(soup)

