#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:37:17 2020

@author: bernardintheo
"""

import folium
from IPython.display import display
import webbrowser as wb
import os
import pandas as pd


def generateBaseMap(default_location=[45.919362, 6.157258], default_zoom_start=12):
    base_map = folium.Map(location=default_location, control_scale=True, zoom_start=default_zoom_start)
    return base_map



LDN_COORDINATES = (45.919362, 6.157258)
myMap = folium.Map(location=LDN_COORDINATES, zoom_start=12,tiles='OpenStreetMap')
tooltip = 'Click me!'

folium.Marker([45.919362, 6.157258], popup='<i>RU</i>', tooltip=tooltip).add_to(myMap)

myMap.save("mymap.html")

wb.open('file://' + os.path.realpath("mymap.html"))



