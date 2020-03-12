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


df_train = pd.read_csv('train.csv').drop(columns=['trip_duration', 'dropoff_datetime'])
df_test = pd.read_csv('test.csv')
df = pd.concat([df_train, df_test], sort=False, ignore_index=True)


def generateBaseMap(default_location=[45.919362, 6.157258], default_zoom_start=12):
    base_map = folium.Map(location=default_location, control_scale=True, zoom_start=default_zoom_start)
    return base_map




from folium.plugins import HeatMap
df_copy = df[df.id>4].copy()
df_copy['count'] = 1
base_map = generateBaseMap()
mapHeat = HeatMap(data=df_copy[['pickup_latitude', 'pickup_longitude', 'count']].groupby(['pickup_latitude', 'pickup_longitude']).sum().reset_index().values.tolist(), radius=8, max_zoom=13).add_to(base_map)


LDN_COORDINATES = (45.919362, 6.157258)
myMap = folium.Map(location=LDN_COORDINATES, zoom_start=12,tiles='CartoDB')
tooltip = 'Click me!'

folium.Marker([45.919362, 6.157258], popup='<i>RU</i>', tooltip=tooltip).add_to(myMap)

myMap.save("mymap.html")
mapHeat.save("map.html")

wb.open('file://' + os.path.realpath("map.html"))



