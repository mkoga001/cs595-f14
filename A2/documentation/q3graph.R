#!/usr/bin/Rscript

mems_vs_days <- read.csv("dayvsmem.txt", stringsAsFactors = F, header = FALSE, sep = " ")

data = mems_vs_days[,c(2,3)]

png("q3-scatterplot.png")

plot(data, col=c("blue"), ylab="Age (in days)", xlab="Number of Mementos", main = "Number of Mementos vs. Age of URI")

dev.off()