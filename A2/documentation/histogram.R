#!/usr/bin/Rscript

d = read.csv( "mementos.txt", stringsAsFactors=F, header = FALSE, sep = "\t" )

Mementos = d[,1]

brk <- seq(0, 48375, 1)

png("q2-histogram1.png")
hist(Mementos, col=heat.colors(48375), main = "URIs vs. Number of Mementos", breaks=brk, freq = T, xlab="Mementos", ylab="URIs")

dev.off()

Mementos = Mementos[which(Mementos<1000)]


brk <- seq(0, 1000, 1)

png("q2-histogram2.png")
hist(Mementos, col=heat.colors(1000), main = "URIs vs. Number of Mementos", breaks=brk, freq = T, xlab="Mementos", ylab="URIs")

dev.off()

Mementos = Mementos[which(Mementos<200)]

brk <- seq(0, 200, 3)

png("q2-histogram3.png")
hist(Mementos, col=heat.colors(200), main = "URIs vs. Number of Mementos", breaks=brk, freq = T, xlab="Mementos", ylab="URIs")

dev.off()