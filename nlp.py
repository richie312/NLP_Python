# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 10:16:57 2019

@author: Richie
"""
import nltk
import os
os.chdir(r"C:\Users\Richie\Desktop\NLP_Python")
NLTK_Location = r"C:\Users\Richie\AppData\Roaming\nltk_data"
#nltk.download()

# =============================================================================
# """Search Text"""
# list_of_words = ["monstrous","very","truth","violence"]
# text1.concordance("truth")
# text2.common_contexts(list_of_words)
# """Dispersion plot for the words"""
# text2.dispersion_plot(list_of_words)
# 
# len(set(text2))
# """Joining the words with/without separator and splitting"""
# a = ' '.join(list_of_words)
# a.split()
# 
# sentence = ' '.join(text6[0:])
# sentence = sentence.split()
# sentence
# 
# """Loop to find if any of the words is ending with "ize" """
# result = []
# 
# for word in range(len(sentence)):
#         if sentence[word].endswith("ise") == True:
#             result.append(sentence[word])
# result
# 
# """ find words with specific letter"""
# 
# find = []
# 
# for letter in range(len(sentence)):
#     if sentence[letter].find('z') != -1:
#         find.append(sentence[letter])
# find    
# 
# pt = []
# 
# for letter in range(len(sentence)):
#     if sentence[letter].find('pt') != -1:
#         pt.append(sentence[letter])
# pt    
# 
# """Lowercase the words except the starting letter"""
# sentence_lower = []
# for i in range(len(sentence)):
#     sentence_lower.append(sentence[i][0] + sentence[i][1:].lower())
# sentence_lower
# 
# """ Find all words which starts with sh"""
# 
# text_sh =['she', 'sells', 'sea', 'shells', 'by',
# 'the', 'sea', 'shore']
# 
# sh = []
# for letter in range(len(text_sh)):
#     if text_sh[letter].startswith("sh") == True:
#         sh.append(text_sh[letter])
# #print("The words which starts with 'sh' are", str(sh))
# 
# """ words which are greater than length of 4 chars"""
# words_greater_than_len_4 = []
# for i in range(len(text_sh)):
#     if len(text_sh[i]) > 4:
#         words_greater_than_len_4.append(text_sh[i])
#     
# words_greater_than_len_4
#  
# 
# """ Average word_length of a text"""
# 
#     
# def Avg_word_length(text):
#     Total_sumall_word_length=sum([len(w) for w in text])
#     avg = round(Total_sumall_word_length/len(text),0)
#     return avg
# 
# Avg_word_length(text9)
# 
# 
# """ Vocabulary Size"""
# 
# def vocab_size(text):
#     vocab_size = sum([len(w) for w in set(text)])
#     return vocab_size
# vocab_size(text6)
# 
# =============================================================================

""" Frequency of the word in the text"""
def lower(text):
    text_lower = []
    for i in range(len(text)):
        text_lower.append(text[i][0] + text[i][1:].lower())
    return text_lower

#lower(text1)
#text1[0:10]
def percent(word,text):

    assert type(word) == str
    count = 0.0
    for j in range(len(text)):
        if text[j] == word:
            count += 1
    percent = round((count/len(text))*100,0)
    return percent,count,len(text)

#percent("anxiety",text1)        
        
def freqDist(text):
    dict = {}
    for j in range(len(text)):
        if text[j] in dict:
            dict[text[j]] += 1
        else:
            dict[text[j]] = 1
    return dict

# =============================================================================
# """Test for freqDist and normal vis a vis nltk.FreqDist() method"""
# b = freqDist(sorted(normal(text1)))
# len(b)
# a = nltk.FreqDist(sorted(normal(text1)))
# len(a)
# len(a.keys())
# len(b.keys())
# a[','] == b[',']
# =============================================================================
