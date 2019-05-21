						#####Center Image Data Preparation 2#####
# ###Importing files
# path = "~/Documents/Attention:Race Bias/Summer 2016/Image Cue/Clean Data"

setwd("C:/Users/aaf2262/Box Sync/MDL Lab/MDL Projects/Projects/Attention Bias Methods/Data/Fall 2016/WF4 Data/cleaned data")
data<-read.csv("alldata.csv")
head(data)
str(data)

########Sorting by Participant Column#######
data_all = data[order(data$participant),]
str(data_all)
head(data_all)
tail(data_all)
dim(data_all)
table(data_all$participant)

############Changing Column Names###################
str(data_all)

###Change Key_Resp.rt Column Name to RT Column Name
colnames(data_all)[colnames(data_all)=="Key_Resp.rt"] = "RT"
colnames(data_all)
str(data_all)

###Add Accuracy Column
data_all$Accuracy = data_all$accuracy
colnames(data_all)
str(data_all)
#Change Correct Column to factor
data_all$accuracy = as.factor(data_all$accuracy)
str(data_all)

#######Save Final Dataset##########
#export a file called data_all.csv that contains data from all the participants
#in write.csv we need a path and a file name that we want to create
#we can use the paste function to create that path
# path
# #we combined that path to where all the data are and created a new file name called data_all.csv that we want to contain all the data
# paste(path, "/finaldata_all.csv", sep="")
# #the command below actually saves it to your computer
write.csv(data_all, file="finaldata_all.csv")
						