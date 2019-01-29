# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 12:05:09 2019

@author: Richie
"""

from bs4 import BeautifulSoup
import requests
import urllib
import pandas as pd

"""Accessing the image from web """
url = "https://www.kohls.com/search.jsp?submit-search=web-ta-keyword-cat&search=floral+dresses&CN=Department%3AClothing%2BGender%3AWomens&S=1&PPP=60&kls_sbp=30791824592479704744051542053675060422"

page = requests.get(url)
raw_soup = BeautifulSoup(page.content,'html.parser')

images = raw_soup.find_all('img',class_="pmp-hero-img")

"""INstantitate the url and description list"""
image_link =[]
image_desc = []

for image in images:
    image_link.append(image.attrs.get('src'))
    image_desc.append(image.attrs.get('title'))

# =============================================================================
# """Get the files to local drive"""
# 
# for i in range(len(image_desc)):
#     urllib.request.urlretrieve(image_link[i], image_desc[i]+'.jpg')
# 
# =============================================================================
"""Instantiate tthe dataframe"""

dataframe = pd.DataFrame()

dataframe["Image_Index"] = ["Image_{}.jpg".format(i) for i in range(len(image_desc))] 
dataframe["features"] = [','.join(i.split()[1:]) for i in image_desc]

""" Write the submission file"""

dataframe.to_csv("kohl_features.csv",index = False)

