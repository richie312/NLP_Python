# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 12:05:09 2019

@author: Richie
"""

from bs4 import BeautifulSoup
import requests

"""Accessing the image from web and from Disk"""
url = "https://www.pyimagesearch.com/2017/08/21/deep-learning-with-opencv/"

page = requests.get(url)
raw_soup = BeautifulSoup(page.content,'html.parser')

images = raw_soup.find_all('img')

for image in images:
    print(image.attrs.get('src'))
    print(image.attrs.get('title'))

