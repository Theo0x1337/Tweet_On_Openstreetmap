#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:09:36 2020

@author: bernardintheo
"""
import folium
from IPython.display import display
import webbrowser as wb
import os
from geopy.geocoders import Nominatim


class UseDataGathered:

    def __init__(self) :
       self.nominatim = Nominatim()    # objet accesseurs aux fonctionnalites de Nominatim
        
    
    def getCoordTweet(self) :
    
        coordsTweet = []
        try:
            import json
        except ImportError:
            import simplejson as json
        
        # We use the file saved from last step as example
        tweets_filename = 'test_data_twitter.txt'
        tweets_file = open(tweets_filename, "r")
        
        
        with open(tweets_filename) as tfn:
                tweet = json.load(tfn)
        
        for i in range(0,len(tweet)):
            if tweet[i].get('geo') != None :
                coordsTweet.append([tweet[i]['geo']['coordinates'],tweet[i]['id'],tweet[i]['user']['name']])
        return coordsTweet
                
    
    
    def getCity(self,coords):
      location = self.nominatim.reverse(coords)
      city = location.raw['address']['county']    # recuperation de la ville associee
      return city
  
    
    def getCoordByCity(self,city):
        coords = []
        location = self.nominatim.geocode(city)
        coords = [location.latitude,location.longitude]
        
        return coords
  
    
    def getBox(self,city):
        location = self.nominatim.geocode(city)
        box = location.raw['boundingbox']
        box = [float(i) for i in box]
        return box




    def estDansBox(self, box = [], coords = ()) :
        """
        Permet de savoir les coordonnees en parametre
        se situent dans la bounding box
        PARAM bbox : bounding box de la zone courrante
        PARAM coords : coordonnees du lieu a tester
        """
        estBox   = False
        latitudes  = [box[0], box[2]]   # latitudes min et max de la bbox
        longitudes = [box[1], box[3]]   # longitudes min et max de la bbox

        if min(latitudes) < coords[0] and coords[0] < max(latitudes) :            # si les coords se trouvent dans le
            if min(longitudes) < coords[1] and coords[1] < max(longitudes) :      # rectangle que forme la bbox
                estBox = True

        return estBox

                
            


