# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 10:36:34 2019

@author: Richie
"""

import nltk
from bs4 import BeautifulSoup
import requests
from nlp import *
from corpora import *

"""Accessing the text from web and from Disk"""
print("Please paste the url here...")
page = requests.get(str(input()))
raw_text_soup = BeautifulSoup(page.content,'html.parser')

"""Get the text from paragraph class of the html content"""
sent = []
chars=raw_text_soup.ASCII_SPACES + str('"')

for para in range(len(raw_text_soup.find_all('p'))):
    para_text = raw_text_soup.find_all('p')[para].get_text()
    for char in para_text:
        if char in chars[1:]:
            para_text = para_text.replace(char,'')
    sent.append(para_text)
ab = ''
for i in range(len(sent)):
    ab += sent[i]
text_words = ab.split()
type(text_words)
#freqDist(lower(sent1))

"""Expression (Analysis of modals; Nature of linguistic)"""


modals = ['can', 'could', 'may', 'might', 'must', 'will',"would","shall","should"]
dict = {}
for i in range(len(modals)):
    dict[modals[i]] = percent(modals[i],text_words)[1]


Expression = {"must":"Strong Obligation" ,"might":"Logical Conclusion",
              "can":"Ability","could":"Possibility","may":"possibility - probability",
              "shall":"Probability","should":"advice","will":"Polite","would":"Polite statement"}


for i in dict.keys():
    if dict[i] == max(dict.values()):
        print("The nature of this excerpt is more or less: "+str(Expression[i])+str('.')+
              str(" For more informaiton, please check https://www.myenglishpages.com/site_php_files/grammar-lesson-modals.php"))
