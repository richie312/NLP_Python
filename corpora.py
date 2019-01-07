# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 11:16:17 2019
@author: Richie
"""

import os
os.chdir(r"C:\Users\Richie\Desktop\NLP_Python")
import nltk
from nltk.corpus import gutenberg
gutenberg.fileids()

emma = nltk.corpus.gutenberg.words("austen-emma.txt")
len(set(emma))

emma = nltk.Text(emma)

emma.concordance("surprize")

"""Sentences"""
dir(emma)
emma_sentences = gutenberg.sents("austen-emma.txt")

""" Find out the longest sentence in the emma text"""

longest_len = max([len(w) for w in emma_sentences])
[s for s in emma_sentences if len(s) == longest_len]

for s in emma_sentences:
    if len(s) == longest_len:
        print(s)
""" Brown Corpus (Brown University, 1960s)"""

from nltk.corpus import brown

categories = brown.categories()

words = brown.words(categories = categories[categories.index("government")])
' '.join(words[0:])
len(words)

""" Frequency Distribution of words in given words"""

# =============================================================================
# nltk.FreqDist()
# 
# words_lower = []
# for w in words:
#     words_lower.append(w.lower())
#     
# nltk.FreqDist(words_lower)
# 
# =============================================================================

from nlp import *
import pandas as pd
list_of_words = ['can', 'could', 'may', 'might', 'must', 'will']

def ConditionalFreq(list_of_words):
    results =[]
    
    for genre in categories:
        _ = []
        for m in list_of_words:
            _.append(percent(m,brown.words(categories = categories[categories.index(genre)]))[1])
        results.append(_) 
        """ Converting the results into dataframe to view the results in tabular format"""
    df = pd.DataFrame(results)
    df.columns = list_of_words

    """Re indexing the datanames with list of rown mes from dictionary"""

    dict={}
    for i in range(len(categories)):
        dict[i] = categories[i]
    df = df.rename(index = dict)
    return df

#ConditionalFreq(list_of_words)

""" Import Stopwords"""

from nltk.corpus import stopwords

stopwords.words('english')


    
