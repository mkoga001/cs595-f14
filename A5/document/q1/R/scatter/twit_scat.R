
no_vs_followers <- read.csv("twitter.txt", stringsAsFactors = F, header = FALSE, sep = " ")

pdf("q1-scatterplot.pdf")

plot(no_vs_followers, col=c("blue"), ylab="No of Followers", xlab="Followers of Followers", main = "Followers of Followers on Twitter")

dev.off()