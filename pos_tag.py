# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:00:10 2019

@author: Richie
"""

import nltk

sentence = "They refuse to permit us to obtain the refuse permit"
words = sentence.split()
pos_tags = nltk.pos_tag(words)
pos_tags[1][1]
""" Find the count for each POS"""

def count_postag(text):
    assert type(text) == str
    words = sentence.split()
    pos_tag = nltk.pos_tag(words)
    count_key = []
    dict = {}
    for i in range(len(pos_tag)):
        if pos_tag[i][1] not in count_key:
            dict[pos_tag[i][1]] = 1
            count_key.append(pos_tag[i][1])
        else:
            dict[pos_tag[i][1]] += 1
    return dict
count_postag(sentence)

""" Classifier for male-Female names """

def gender_features(word):
    return{'last_letter':word[-1]}

gender_features("Richie")

from nltk.corpus import names
import random
names=[(name,'male') for name in names.words('male.txt')]+[(name, 'female') for name in names.words('female.txt')]
random.shuffle(names)
featureset = [(gender_features(name),gender) for (name,gender) in names]

training_set, testing_set = featureset[500:] , featureset[:100]

classifier = nltk.NaiveBayesClassifier.train(training_set)

classifier.classify(gender_features('Pema'))

nltk.classify.accuracy(classifier,testing_set)

classifier.show_most_informative_features(5)

for n,g in names:
    print(n,g)

names[99][0]


