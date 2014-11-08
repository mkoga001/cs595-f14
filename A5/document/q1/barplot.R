
data <- read.csv("followed-sorted.txt", stringsAsFactors = F, header = FALSE, sep = " ")

incdata = data[,1]

meanOut <- paste("Mean: ", mean(incdata), collapse = "")

medianOut <- paste("Median: ", median(incdata), collapse = "")

sdOut <- paste("Std Dev: ", sd(incdata), collapse = "")

write(meanOut, stdout())
write(medianOut, stdout())
write(sdOut, stdout())

pdf("barplot.pdf")
pos <- (incdata == 148)

cols <- c("white", "red") 


barplot(incdata, main="Friends of Friends on Twitter", xlab="Friends sorted by increasing number of friends", ylab="Number of Friends", col=cols[pos + 1],xlim = c(0,175), ylim=c(0, 4000))
text(x=match(c(148), incdata)+13, y=max(incdata), labels="phonedude_mln", col='red')
arrows(x0=match(c(148), incdata)+13, y0=(max(incdata) - 80), x1=match(c(148), incdata)+13, y1=175, length=0.1, lwd=3, col='red')


