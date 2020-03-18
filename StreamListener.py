#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 15:49:38 2020

@author: bernardintheo
"""

import sys
import tweepy
import json

class StreamListener(tweepy.StreamListener):
    
    
    def __init__(self):
        super().__init__()
        self.max_tweets = 10
        self.tweet_count = 0

    #method executed when the connection is established
    def on_status(self, status):
        #print the tweet found by the program 
        #open the file test_data_twitter.txt
        with open('test_data_twitter.txt','a') as tf:
            if(self.tweet_count<self.max_tweets):
                #write the tweet in JSON format in the file 
                tf.write(json.dumps(status._json))
                #separate the different JSON objects with a ,
                tf.write(",")
                self.tweet_count=self.tweet_count+1
                return True
            else:
                return False
    
    #when there is an error with the connection
    def on_error(self, status_code):
        if status_code == 420:
            print('cc')
            return False
        
        #[43.6044, 1.4443]

