#!/usr/local/bin/python

import clusters

blognames,words,data=clusters.readfile('blogdata120-atom-500.txt')

print "For k=5"
kclust=clusters.kcluster(data, k=5)
print

print "For k=10"
kclust=clusters.kcluster(data, k=10)
print

print "For k=20"
kclust=clusters.kcluster(data, k=20)
print
