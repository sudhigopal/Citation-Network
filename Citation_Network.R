bin_search = function(v, t) {
  lo = as.integer(1)
  hi = length(v)
  while (lo <= hi) {
    mid = as.integer(round((lo + hi) / 2)) # always even!
    #  cat("lo, mid, hi = ", lo, mid, hi, "\n")
    
    if (v[mid] == t) {
      return(mid)
    }
    else if (v[mid] < t) { # C format OK in a function
      lo = mid + 1
    }
    else {
      hi = mid - 1
    }
  }
  
  return(0)
}

# main program

mydata<-allPatentData[,]

#mydata <- xx[order(xx$appyear),]
#Based on APPYEAR
#mydata[mydata$appyear == 1975, ]
#mydata[mydata$citing == 3970838, ]
#Based on YEAR and CITING
#mydata <- mydata[which(mydata$citing == 3931349 & mydata$gyear > mydata$appyear),]
#which(mydata$citing == 3931349)
selectedData<-data.frame(mydata$citing,mydata$cited)  
k=1;
myArray=NULL;
for(i in 1:dim(selectedData)[1]) {
  for(j in 1:dim(selectedData)[2]) {
    myArray[k]=selectedData[i,j];
    k=k+1;
  }
}

mynewArray<- sort(myArray, decreasing = FALSE)
mynewArray2<- unique(mynewArray)
mynewArray2

for(i in 1:dim(selectedData)[1]) {
  for(j in 1:dim(selectedData)[2]) {
    
    val<-bin_search(mynewArray2,selectedData[i,j])
    if(val>0){
      selectedData[i,j]=val;
    }
    
    
  }
}

#selectedData[30:50,]
#-------------
library(igraph)
u <- unique(c(selectedData$mydata.citing,selectedData$mydata.cited))
u
uniquePatIDs <- data.frame(v1=1:length(u),v2=u)

el <- data.frame(selectedData[,1:2])
elRe <- data.frame(v1=match(el$citing, uniquePatIDs$v2), v2=match(el$cited,uniquePatIDs$v2))
#V(selectedData$mydata.cited)$color <- "red"

#------- reinsert--------
for(i in 1:dim(selectedData)[1]) {
  for(j in 1:dim(selectedData)[2]) {
    
    for(k in 1:length(mynewArray2))
    {
      if(k==selectedData[i,j])
      {
        selectedData[i,j]=mynewArray2[k];
      }
      
    }
  }
}

#------- reinsert--------end


#g <- graph_from_data_frame(selectedData, directed=TRUE, vertices=u)
g <- graph_from_data_frame(selectedData, directed=TRUE, vertices=mynewArray2)
V(g)$color <- "red"
E(g)$color <- "Blue"

# simplify(g, remove.multiple = FALSE, remove.loops = FALSE)
# is_simple(g)
g2 <- delete.edges(g, which(is.multiple(g))-1)

# plot(g2,vertex.label.color="white", vertex.label=V(g)$name,edge.arrow.size=0.7,vertex.label.color = "black",
#      vertex.size=20,edge.width=2)
plot(g2,vertex.label.color="white", vertex.label=V(g)$name,edge.arrow.size=0.2,vertex.label.color = "black",vertex.size=20,edge.width=2)

clu <- components(g2)
groups(clu)


clu$csize
#---------------


#-----------

# 
# patGraph <- graph_from_edgelist(el2, directed = TRUE)
# plot(patGraph )