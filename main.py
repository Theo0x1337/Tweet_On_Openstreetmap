#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:40:06 2020

@author: bernardintheo
"""
import tweepy
from StreamListener import StreamListener
from UseDataGathered import UseDataGathered
from initMap import initMap

class Main:
    
    
    #different token to make request thanks to tweepy
    access_token = '1159875631670280201-lrXbOUzctlHaCXYOOB600DPDdoAncZ'
    access_token_secret = 'XPYPaEMZcagFT9KPRDjJGB9K5lL2AZPPoD6JzMi30oK5Y'
    consumer_key = '2BAaR711Mz6rTzkBQKgACVXUl'
    consumer_secret = 'eCFxVBntV9ebhC9yuqdDy2LNvaRHzEMHbFNcVyiNRRS2DOaVQe'
    
    #using our credential to instantiate a connection with tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    #Create a streamListener
    stream_listener = StreamListener()
    #Establish the connection with tweepy 
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
    stream.filter(languages=["fr"],locations=[-5.45,41.26,9.87,51.27])
    
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

    
    udg = UseDataGathered()
    tabInfo=[]
    tabInfo = udg.getCoordTweet()
            
    
    osmMap = initMap()
    osmMap.newMap()
    
    for info in tabInfo:
        osmMap.setMarkerOnMap(info[0],info[1],info[2])
        
    osmMap.displayMap()