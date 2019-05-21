					#######Center Image Data Preparation 3######

###Import Data
setwd("C:/Users/aaf2262/Box Sync/MDL Lab/MDL Projects/Projects/Attention Bias Methods/Data/Fall 2016/WF4 Data/cleaned data")
					
data=read.csv("finaldata_all.csv")
str(data)
head(data)
tail(data)
dim(data)
colnames(data)


###Eliminate responses under 300 ms & over 2.5 SDs from mean#######
data$false_start=ifelse(data$RT<=.300, 1, 0)
head(data)
table(data$false_start)
#Delete rows with false starts
data = data[!(data$false_start=="1"),]
#Check data
str(data)
table(data$false_start)
dim(data)
head(data)
tail(data)
tail(data$false_start)

#Find SD for each participant
#install.packages("doBy")
library(doBy)
msd=summaryBy(RT~participant, data, FUN=c(mean, sd), na.rm=TRUE)
msd
#CHANGE THIS:
#Delete extra row at bottom
msd = msd[-(45),]
msd
#Merge SD data with original dataset by participant
sddata=merge(data, msd, by="participant")
str(sddata)
head(sddata)
tail(sddata)
dim(sddata)

#Row checking for RTs 2.5 SDs above mean
longRT=ifelse(sddata$RT>=(sddata$RT.mean+(2.5*sddata$RT.sd)), 1, 0)
table(longRT)
#Add longRT row to data frame
sddata$longRT = longRT
#Delete rows with RTs 2.5SDs above mean
Data = sddata[!(sddata$longRT=="1"),]
dim(Data)
str(Data)
table(Data$participant)


#######Save Final Dataset##########
#export a file called data_all.csv that contains data from all the participants
#in write.csv we need a path and a file name that we want to create
#we can use the paste function to create that path
# path = "~/Documents/Attention:Race Bias/Summer 2016/Image Cue/Clean Data"
# path
# #we combined that path to where all the data are and created a new file name called data_all.csv that we want to contain all the data
# paste(path, "/FinalCleanData.csv", sep="")
#the command below actually saves it to your computer
write.csv(Data, file=("FinalCleanData.csv"))
          