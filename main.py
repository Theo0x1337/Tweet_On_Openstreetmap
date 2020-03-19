#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 02 16:40:06 2020

@author: bernardintheo
"""

import tweepy
import json
from StreamListener import StreamListener
from UseDataGathered import UseDataGathered
from initMap import initMap
from KeywordCity import KeyWordCity

class Main:
    
    
    #different token to make request thanks to tweepy
    access_token = 'YOUR TOKEN HERE'
    access_token_secret = 'YOUR TOKEN HERE'
    consumer_key = 'YOUR TOKEN HERE'
    consumer_secret = 'YOUR TOKEN HERE'
    
    #using our credential to instantiate a connection with tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    #Create a streamListener   
    stream_listener = StreamListener()
    #Establish the connection with tweepy 
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
    stream.filter(locations=[-5.45,41.26,9.87,51.27])
    
    
    search_results = api.search(geocode="48.6833,6.2,10km", count=500)
    
    with open('data_twitter_search.txt','a') as tfs:
        for i in search_results:
            tfs.write(json.dumps(i._json))
            #separate the different JSON objects with a ,
            tfs.write(",")
    
    
    with open('data_twitter_search.txt', 'r+') as f:
       content = f.read()
       content = content[:-1]
       f.seek(0, 0)
       f.write('['.rstrip('\r\n') + '\n' + content)
       f.close()
    
    f=open('data_twitter_search.txt','a')
    f.seek(0) #get to the first position
    f.write("]")
    f.close()
    
    
    with open('test_data_twitter.txt', 'r+') as f:
        content = f.read()
        content = content[:-1]
        f.seek(0, 0)
        f.write('['.rstrip('\r\n') + '\n' + content)
        f.close()
    
    f=open('test_data_twitter.txt','a')
    f.seek(0) #get to the first position
    f.write("]")
    f.close()


    coordNancy = [6.2,48.6833]
    boxNancy = [6.134292,48.666906,6.212619,48.709235]
    
    udg = UseDataGathered()
    tabInfo=[]
    tabInfo = udg.getCoordCentreVille(boxNancy,coordNancy)
    
    osmMap = initMap()
    osmMap.newMap()
    
    
    for info in tabInfo:
        osmMap.setMarkerOnMap(info[0],info[1],info[2])
        
    osmMap.displayMap()
    
    
    content_tweet_city = udg.getContentTweet("data_twitter_search.txt")
    
    kw = KeyWordCity(content_tweet_city)
    tabWords = kw.getKeywordsCity()
    
    
    print("Les 10 mots les plus cités dans la ville que vous avez choisie sont : ")
    
    tenKeywords = kw.get10TopKeyWords(tabWords)
