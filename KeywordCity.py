#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 03 22:17:36 2020

@author: bernardintheo
"""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist


class KeyWordCity :
    
    def __init__(self,chaine):
        self.content = chaine
        
        
        
    def getKeywordsCity(self):
        stop_words = set(stopwords.words('french'))
        
        tokenizer = RegexpTokenizer(r"\w+")
        new_words = tokenizer.tokenize(self.content)
        
        chInter = ""
        
        for elem in new_words: 
            chInter = chInter +" "+ elem
        
        words = word_tokenize(chInter)
         
        new_sentence = ""
                 
        for word in words:
            if word not in ['RT','https','t','co','le','que','on','ça','a','T ','T','J','J ','Je','je','va']:
                if word not in stop_words:
                    new_sentence = new_sentence +" "+ word
         
            
        stFinal = tokenizer.tokenize(new_sentence)
        
        return stFinal
    
    
    def get10TopKeyWords(self,tabWord):
        allWordDist = FreqDist(tabWord)
        allWordDist.plot(10)
        
    
        
            
        