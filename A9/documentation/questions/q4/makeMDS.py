#!/usr/local/bin/python

import clusters

blognames,words,data=clusters.readfile('blogdata120-atom-500.txt')

coords = clusters.scaledown(data)

clusters.draw2d(coords, blognames, jpeg='blogs2d.jpg')
