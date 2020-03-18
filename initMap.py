#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 02 16:29:42 2020

@author: bernardintheo
"""

import folium
import webbrowser as wb
import os

class initMap : 
    
    def __init__(self):
        self.map = None
    
    def newMap(self,LDN_COORDINATES=[48.8534,2.3488]):
        myMap = folium.Map(location=LDN_COORDINATES, zoom_start=4,tiles='OpenStreetMap')
        self.map = myMap
    
    
    def setMarkerOnMap(self,coord,popup,tooltip):
        folium.Marker(coord, popup='<i>'+str(popup)+'</i>', tooltip=tooltip).add_to(self.map)

        
    def displayMap(self):
        self.map.save("mymap.html")
        wb.open('file://' + os.path.realpath("mymap.html"))