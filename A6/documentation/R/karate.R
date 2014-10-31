library(igraph) # for graph functions
library(igraphdata) # for karate club data

data(karate)# loading the weighted graph for karate club from the packages.
#karate <- read.graph("Z:/mallika/cs595/A6/karate/karate.gml",format = "gml")
#Used the above line to load karate.gml file
club <- karate
threshold <- 2


plot.igraph(club, 
           main="Karate Club Graph Prior to Breakup",
           )
i <- 0

while( clusters(club)$no < threshold ) {
  #calculate the betweenness between edges by using the function edge.betweenness
  club.edge.betweenness <- edge.betweenness(club)
  #Ordering the edges in descresing order basing on their betweenness values.
  decreasing.betweenness <- order(club.edge.betweenness, decreasing = TRUE)
  #collect the node which has the highest betweenness and stored it in a variable.
  highest.betweenness <- decreasing.betweenness[-1]
  
  edge.to.delete <- get.edge(club, highest.betweenness)
  cat(i)# check the number of itteration it took to slipt it into 2 clusters
  club <- delete.edges(club, E(club, P = edge.to.delete))
  #Delete the edge which had the highest betweenness
  ++i
}


plot.igraph(club, 
            main="Karate Club Split, Predicted by Girvan-Newman Betweenness",
            )
