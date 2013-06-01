#!/usr/bin/env python

"""
Convert bus routes from red to many colors.

The Regional Transportation Commission of Southern Nevada publishes a
KMZ file of all the bus routes. You can open this in Google Earth, but
all the bus routes are the same color. This script will modify the KMZ
file to make all the routes different colors so they are visually
distinct.
"""

import xml.dom.minidom
from xml.dom.minidom import Node

doc = xml.dom.minidom.parse('doc.kml')
# Each RTC bus route lives in a node 'Placemark'
nodes = doc.getElementsByTagName('Placemark')

mapping = dict()
for node in nodes:
    name = node.getElementsByTagName('name')[0]
	# Get the route name
    mapping[name.firstChild.nodeValue] = 'ffffffff'

numroutes = len(mapping.keys()) # as of this writing, 119 routes

for color in range(0, 0xffffff, 0xffffff / 119):
    newcolor =  "#%Xfa" % color
    print newcolor.lower()

