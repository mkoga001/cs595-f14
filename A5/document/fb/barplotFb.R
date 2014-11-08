
data <- read.csv("fbSorted.txt", stringsAsFactors = F, header = FALSE, sep = " ")
incdata = data[,1]
meanOut <- paste("Mean: ", mean(incdata), collapse = "")
medianOut <- paste("Median: ", median(incdata), collapse = "")
sdOut <- paste("Std Dev: ", sd(incdata), collapse = "")
write(meanOut, stdout())
write(medianOut, stdout())
write(sdOut, stdout())
pdf("fb_barplot.pdf")
pos <- (incdata == 311)
cols <- c("white", "red") 
barplot(incdata, main="Friends of Friends on FaceBook", xlab="Friends sorted by increasing number of friends", ylab="Number of Friends", col=cols[pos + 1], ylim=c(0, 4000))
text(x=match(c(311), incdata)+12, y=(max(incdata)-20), labels="Mallika Kogatam", col='red')
arrows(x0=match(c(311), incdata)+12, y0=(max(incdata) - 80), x1=match(c(311), incdata)+12, y1=325, length=0.1, lwd=2.5, col='red')

