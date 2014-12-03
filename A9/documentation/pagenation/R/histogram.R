data <- read.csv("noOfPages.txt", stringsAsFactors = F, header = FALSE, sep = "|")

incdata = data[, 1]

incdata <- as.numeric(incdata)

brk <- seq(0, 300, 10)

png("q1-histogram1.png")
hist(incdata, main = "Blogs vs. Number of Pages", breaks=brk, freq = T, xlab="Pages", ylab="Blogs")
