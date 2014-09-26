#!/usr/bin/Rscript

d = read.csv( "memUrlCdate.txt", stringsAsFactors=F, header = FALSE, sep = "\t" )

Mementos = d[,1]

brk <- seq(0, 3000, 1)

png("q2-histogram1.png")
hist(Mementos, col=heat.colors(3000), main = "URIs vs. Number of Mementos", breaks=brk, freq = T, xlab="Mementos", ylab="URIs")

dev.off()

Mementos = Mementos[which(Mementos<1500)]

brk <- seq(0, 1500, 1)

png("q2-histogram2.png")
hist(Mementos, col=heat.colors(1500), main = "URIs vs. Number of Mementos", breaks=brk, freq = T, xlab="Mementos", ylab="URIs")

dev.off()

Mementos = Mementos[which(Mementos<100)]

brk <- seq(0, 100, 1)

png("q2-histogram3.png")
hist(Mementos, col=heat.colors(90), main = "URIs vs. Number of Mementos", breaks=brk, freq = T, xlab="Mementos", ylab="URIs")

dev.off()