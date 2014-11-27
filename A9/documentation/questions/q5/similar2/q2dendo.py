import clusters


blognames,words,data=clusters.readfile('blogList500-matrix.txt')
clust = clusters.hcluster(data)

# print ASCII dendrogram
clusters.printclust(clust, labels=blognames)

# save JPEG dendrogram
clusters.drawdendrogram(clust, blognames, jpeg='blogclust-q5.jpg')