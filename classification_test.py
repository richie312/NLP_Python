# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 12:38:49 2019

@author: Richie
"""

import nltk
import os

os.chdir("C:/Users/Richie/Desktop/NLP_Python")

from nltk.corpus import  webtext
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.corpus import stopwords
textword=[w.lower() for w in webtext.words('pirates.txt')]
finder = BigramCollocationFinder.from_words(textword)

finder.nbest(BigramAssocMeasures.likelihood_ratio,10)
ignored_words = set(stopwords.words('english'))

filterstops = lambda w: w in ignored_words

type(finder)

finder.apply_word_filter(filterstops)