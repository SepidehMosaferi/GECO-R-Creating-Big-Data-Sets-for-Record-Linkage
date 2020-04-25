# =======================================================================
#   R program for Record Linkage
#   Date: Aug. 2017 
#   Author: Sepideh Mosaferi
# =======================================================================

require("RecordLinkage") 

## Preparing Data for Washington DC
DATAGeCo1 <- read.csv("/home/sepideh/RL/GECO-DC/synth-data1.csv",header=TRUE,sep=",")
DATAGeCo1 <- data.frame(DATAGeCo1)
DATAGeCo_DC <- data.frame(cbind(DATAGeCo1,rep("Washington DC",nrow(DATAGeCo1))))
colnames(DATAGeCo_DC) <- c(names(DATAGeCo_DC)[1:11],"City") 
ID1_DC <- sapply(1:length(DATAGeCo_DC$ID),
       function(i) unlist(strsplit(as.character(DATAGeCo_DC$ID[i]),split='rec-',fixed=TRUE))[2])
ID_DC <- noquote(sapply(1:length(ID1_DC),function(i) unlist(strsplit(ID1_DC[i],split='-',fixed=TRUE))[1]))
DUP1_DC <- sapply(1:length(DATAGeCo_DC$ID),
               function(i) unlist(strsplit(as.character(DATAGeCo_DC$ID[i]),split='rec-',fixed=TRUE))[2])
DUP2_DC <- noquote(sapply(1:length(ID1_DC),function(i) unlist(strsplit(DUP1_DC[i],split='-',fixed=TRUE))[2]))
DUP_DC <- ifelse(DUP2_DC=='dup',1,0)                     
DATAGeCo_DC <- data.frame(cbind(ID_DC,DUP_DC,DATAGeCo_DC))        
DATAGeCo_DC <- DATAGeCo_DC[,-3]
DATAGeCo_DC$ID_DC_modif <- noquote(paste0(1,DATAGeCo_DC$ID_DC))
DATAGeCo_DC <- data.frame(cbind(DATAGeCo_DC$ID_DC_modif,DATAGeCo_DC$DUP_DC,DATAGeCo_DC[,3:13]))
colnames(DATAGeCo_DC) <- c("ID","DUP", names(DATAGeCo_DC)[3:length(DATAGeCo_DC)])


## Preparing Data for Los Angeles
DATAGeCo2 <- read.csv("/home/sepideh/RL/GECO-LA/synth-data2.csv",header=TRUE,sep=",")
DATAGeCo2 <- data.frame(DATAGeCo2)
DATAGeCo_LA <- data.frame(cbind(DATAGeCo2,rep("Los Angeles",nrow(DATAGeCo2))))
colnames(DATAGeCo_LA) <- c(names(DATAGeCo_LA)[1:11],"City") 
ID1_LA <- sapply(1:length(DATAGeCo_LA$ID),
                 function(i) unlist(strsplit(as.character(DATAGeCo_LA$ID[i]),split='rec-',fixed=TRUE))[2])
ID_LA <- noquote(sapply(1:length(ID1_LA),function(i) unlist(strsplit(ID1_LA[i],split='-',fixed=TRUE))[1]))
DUP1_LA <- sapply(1:length(DATAGeCo_LA$ID),
                  function(i) unlist(strsplit(as.character(DATAGeCo_LA$ID[i]),split='rec-',fixed=TRUE))[2])
DUP2_LA <- noquote(sapply(1:length(ID1_LA),function(i) unlist(strsplit(DUP1_LA[i],split='-',fixed=TRUE))[2]))
DUP_LA <- ifelse(DUP2_LA=='dup',1,0)       
DATAGeCo_LA <- data.frame(cbind(ID_LA,DUP_LA,DATAGeCo_LA))        
DATAGeCo_LA <- DATAGeCo_LA[,-3]
DATAGeCo_LA$ID_LA_modif <- noquote(paste0(2,DATAGeCo_LA$ID_LA))
DATAGeCo_LA <- data.frame(cbind(DATAGeCo_LA$ID_LA_modif,DATAGeCo_LA$DUP_LA,DATAGeCo_LA[,3:13]))
colnames(DATAGeCo_LA) <- c("ID","DUP", names(DATAGeCo_LA)[3:length(DATAGeCo_LA)])


## Preparing Data for Chicago
DATAGeCo3 <- read.csv("/home/sepideh/RL/GECO-Chicago/synth-data3.csv",header=TRUE,sep=",")
DATAGeCo3 <- data.frame(DATAGeCo3)
DATAGeCo_Chicago <- data.frame(cbind(DATAGeCo3,rep("Chicago",nrow(DATAGeCo3))))
colnames(DATAGeCo_Chicago) <- c(names(DATAGeCo_Chicago)[1:11],"City") 
ID1_Chicago <- sapply(1:length(DATAGeCo_Chicago$ID),
                 function(i) unlist(strsplit(as.character(DATAGeCo_Chicago$ID[i]),split='rec-',fixed=TRUE))[2])
ID_Chicago <- noquote(sapply(1:length(ID1_Chicago),function(i) unlist(strsplit(ID1_Chicago[i],split='-',fixed=TRUE))[1]))
DUP1_Chicago <- sapply(1:length(DATAGeCo_Chicago$ID),
                  function(i) unlist(strsplit(as.character(DATAGeCo_Chicago$ID[i]),split='rec-',fixed=TRUE))[2])
DUP2_Chicago <- noquote(sapply(1:length(ID1_Chicago),function(i) unlist(strsplit(DUP1_Chicago[i],split='-',fixed=TRUE))[2]))
DUP_Chicago <- ifelse(DUP2_Chicago=='dup',1,0)       
DATAGeCo_Chicago <- data.frame(cbind(ID_Chicago,DUP_Chicago,DATAGeCo_Chicago))        
DATAGeCo_Chicago <- DATAGeCo_Chicago[,-3]
DATAGeCo_Chicago$ID_Chicago_modif <- noquote(paste0(3,DATAGeCo_Chicago$ID_Chicago))
DATAGeCo_Chicago <- data.frame(cbind(DATAGeCo_Chicago$ID_Chicago_modif,DATAGeCo_Chicago$DUP_Chicago,DATAGeCo_Chicago[,3:13]))
colnames(DATAGeCo_Chicago) <- c("ID","DUP", names(DATAGeCo_Chicago)[3:length(DATAGeCo_Chicago)])


## Preparing Data for New York City
DATAGeCo4 <- read.csv("/home/sepideh/RL/GECO-NewYork/synth-data4.csv",header=TRUE,sep=",")
DATAGeCo4 <- data.frame(DATAGeCo4)
DATAGeCo_NewYork <- data.frame(cbind(DATAGeCo4,rep("New York City",nrow(DATAGeCo4))))
colnames(DATAGeCo_NewYork) <- c(names(DATAGeCo_NewYork)[1:11],"City") 
ID1_NewYork <- sapply(1:length(DATAGeCo_NewYork$ID),
                      function(i) unlist(strsplit(as.character(DATAGeCo_NewYork$ID[i]),split='rec-',fixed=TRUE))[2])
ID_NewYork <- noquote(sapply(1:length(ID1_NewYork),function(i) unlist(strsplit(ID1_NewYork[i],split='-',fixed=TRUE))[1]))
DUP1_NewYork <- sapply(1:length(DATAGeCo_NewYork$ID),
                       function(i) unlist(strsplit(as.character(DATAGeCo_NewYork$ID[i]),split='rec-',fixed=TRUE))[2])
DUP2_NewYork <- noquote(sapply(1:length(ID1_NewYork),function(i) unlist(strsplit(DUP1_NewYork[i],split='-',fixed=TRUE))[2]))
DUP_NewYork <- ifelse(DUP2_NewYork=='dup',1,0)       
DATAGeCo_NewYork <- data.frame(cbind(ID_NewYork,DUP_NewYork,DATAGeCo_NewYork))        
DATAGeCo_NewYork <- DATAGeCo_NewYork[,-3]
DATAGeCo_NewYork$ID_NewYork_modif <- noquote(paste0(4,DATAGeCo_NewYork$ID_NewYork))
DATAGeCo_NewYork <- data.frame(cbind(DATAGeCo_NewYork$ID_NewYork_modif,DATAGeCo_NewYork$DUP_NewYork,DATAGeCo_NewYork[,3:13]))
colnames(DATAGeCo_NewYork) <- c("ID","DUP", names(DATAGeCo_NewYork)[3:length(DATAGeCo_NewYork)])


## Preparing Data for Austin
DATAGeCo5 <- read.csv("/home/sepideh/RL/GECO-Austin/synth-data5.csv",header=TRUE,sep=",")
DATAGeCo5 <- data.frame(DATAGeCo5)
DATAGeCo_Austin <- data.frame(cbind(DATAGeCo5,rep("Austin",nrow(DATAGeCo5))))
colnames(DATAGeCo_Austin) <- c(names(DATAGeCo_Austin)[1:11],"City") 
ID1_Austin <- sapply(1:length(DATAGeCo_Austin$ID),
                      function(i) unlist(strsplit(as.character(DATAGeCo_Austin$ID[i]),split='rec-',fixed=TRUE))[2])
ID_Austin <- noquote(sapply(1:length(ID1_Austin),function(i) unlist(strsplit(ID1_Austin[i],split='-',fixed=TRUE))[1]))
DUP1_Austin <- sapply(1:length(DATAGeCo_Austin$ID),
                       function(i) unlist(strsplit(as.character(DATAGeCo_Austin$ID[i]),split='rec-',fixed=TRUE))[2])
DUP2_Austin <- noquote(sapply(1:length(ID1_Austin),function(i) unlist(strsplit(DUP1_Austin[i],split='-',fixed=TRUE))[2]))
DUP_Austin <- ifelse(DUP2_Austin=='dup',1,0)       
DATAGeCo_Austin <- data.frame(cbind(ID_Austin,DUP_Austin,DATAGeCo_Austin))        
DATAGeCo_Austin <- DATAGeCo_Austin[,-3]
DATAGeCo_Austin$ID_Austin_modif <- noquote(paste0(5,DATAGeCo_Austin$ID_Austin))
DATAGeCo_Austin <- data.frame(cbind(DATAGeCo_Austin$ID_Austin_modif,DATAGeCo_Austin$DUP_Austin,DATAGeCo_Austin[,3:13]))
colnames(DATAGeCo_Austin) <- c("ID","DUP", names(DATAGeCo_Austin)[3:length(DATAGeCo_Austin)])


FinalDATA <- data.frame(rbind(DATAGeCo_DC,DATAGeCo_LA,DATAGeCo_Chicago,DATAGeCo_NewYork,DATAGeCo_Austin))

FinalDATA <- data.frame(cbind(FinalDATA[,1:10],FinalDATA[,13],FinalDATA[,c(11,12)]))

names(FinalDATA) <- c("ID","DUP","First Name","Last Name","Marital Status","Race","DOB","SSN","Income",
                      "Credit Card Number","City","ZIP Code","Telephone Number")

Administrative <- FinalDATA[FinalDATA$DUP==0,]

Survey_pre <- Administrative[sample(nrow(Administrative),3000),]
Survey <- FinalDATA[FinalDATA$ID %in% Survey_pre$ID,]

write.csv(Administrative,"/home/sepideh/RL/Final Data/Administrative.csv")
write.csv(Survey,"/home/sepideh/RL/Final Data/Survey.csv")










