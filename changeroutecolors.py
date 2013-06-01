#!/usr/bin/env python

import xml.dom.minidom
from xml.dom.minidom import Node

doc = xml.dom.minidom.parse('doc.kml')
nodes = doc.getElementsByTagName('Placemark')

mapping = dict()
for node in nodes:
    name = node.getElementsByTagName('name')[0]
    mapping[name.firstChild.nodeValue] = 'ffffffff'

for key in mapping.keys():
	print key
