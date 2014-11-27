data <- read.csv("PagesInBlogs2.txt", stringsAsFactors = F, header = FALSE, sep = "|")

incdata = data[, 1]

incdata <- as.numeric(incdata)

brk <- seq(0, 3000, 100)

png("q1-histogram1.png")
hist(incdata, main = "Blogs vs. Number of Pages", breaks=brk, freq = T, xlab="Pages", ylab="Blogs")

