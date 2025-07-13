#install.packages('rmeta')

library("rmeta")
library("readxl")

setwd("H:/Peijia/graph/c2 ERAP")
mydata <- read_excel('2020-4-3 ERAP-HLA total_EBVpos_EBVneg.xlsx', sheet='Sheet2')
head(mydata)
lb=cbind(mydata$combination, round(mydata$OR,2))
lb1=rbind(c('','OR'),lb)
forestplot(labeltext=lb1, mean=c(NA,mydata$OR), lower=c(NA,mydata$lower), 
           upper=c(NA,mydata$upper), boxsize=0.5, xlab="odds ratio", zero=1, 
           align="c", is.summary=c(TRUE,rep(FALSE,11)),
           xlog=FALSE,xticks=c(0,1,2,5,10,15),
           col=meta.colors(box="royalblue",
                           line="royalblue"))

#forestplot(labeltext=cbind(mydata$combination, round(mydata$OR,2)), mean=mydata$OR, lower=mydata$lower, 
#           upper=mydata$upper, boxsize=0.5, xlab="odds ratio", zero=1, align="c",
#           xlog=FALSE,xticks=c(0,1,2,5,10,15))


