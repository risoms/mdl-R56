					#####Center Image Data Preparation 1#####
# 					
# #read in all participant files and combine
# #we are adding to the empty data frame we created called data
# #remember we want to combine all files so we want the sequence to be from 1:30 or
# 1:length(sub_paths)

library(tidyverse)
library(Hmisc)

setwd("C:/Users/aaf2262/Box Sync/MDL Lab/MDL Projects/Projects/Attention Bias Methods/Data/Fall 2016/WF4 Data/raw data")					
					
files <- list.files(pattern = "*.csv")
data <- data_frame()
					for(i in seq_along(files)){
					  temp <- read_csv(files[i], na = c("9999", "#N/A", "99990", "."))
					  temp$filename <- files[i]
					  temp<-temp[21:385,7:49]
					  data <- rbind(data, temp)
					}					
# 
# for (i in 1:length(sub_paths)){
# 	RB=read.csv(sub_paths[i]) #read in the path
# 	data=rbind(data, RB) #rbind with combine the data by rows with pvt data
# 	}
	
head(data)
tail(data)
dim(data)
table(data$participant)


############Step 2###################
#export a file called data.csv that contains data from all the participants

setwd("C:/Users/aaf2262/Box Sync/MDL Lab/MDL Projects/Projects/Attention Bias Methods/Data/Fall 2016/WF4 Data")
write.csv(data, file="cleaned data/alldata.csv", row.names = FALSE)

data<-read.csv("cleaned data/alldata.csv")
###Changing Image Columns to Character columns###
str(data)
data$Image0._Position=as.character(data$Image0._Position)
data$Image1._Position=as.character(data$Image1._Position)
data$Image2._Position=as.character(data$Image2._Position)
data$Image3._Position=as.character(data$Image3._Position)

data$Center_image=as.character(data$Center_image)
str(data)

###Checking to see where Center Image was located###
data$C1=ifelse(data$Image0._Position==data$Center_image, 1, 0)
data$C2=ifelse(data$Image1._Position==data$Center_image, 2, 0)
data$C3=ifelse(data$Image2._Position==data$Center_image, 3, 0)
data$C4=ifelse(data$Image3._Position==data$Center_image, 4, 0)
str(data)
head(data)

class(data$Key_Resp.keys)
class(data$C4)
# data$Key_Resp.keys<-as.numeric(data$Key_Resp.keys)


# ###Checking to see if Correct###
# data$CA1=ifelse(data$Key_Resp.keys==data$C1, 1, 0)
# data$CA2=ifelse(data$Key_Resp.keys==data$C2, 2, 0)
# data$CA3=ifelse(data$Key_Resp.keys==data$C3, 3, 0)
# data$CA4=ifelse(data$Key_Resp.keys==data$C4, 4, 0)
# str(data)
# head(data)


###Creating Correct Answer ("CA") Column###
#already have this in version 4: `correct_answer`
# for (i in 1:dim(data)[1]){
# if(data$CA1[i]=="1"){
# 	data$CA[i]="1"}
# 	else if (data$CA2[i]=="2"){
# 	data$CA[i]="1"}
# 	else if (data$CA3[i]=="3"){
# 	data$CA[i]="1"}
# 	else if (data$CA4[i]=="4"){
# 	data$CA[i]="1"}
# 	else {data$CA[i]="0"}
#   }


table(data$accuracy)
head(data)
str(data)
table(data$accuracy, data$participant)

#########Add Race Column#############
head(data)
str(data)
#data$EmotionSex=as.character(data$EmotionSex)

data$Emotion<-grepl("SA",data$Center_image)
data$Emotion<-ifelse(data$Emotion=="TRUE", "SA","NE")

data$Sex<-grepl("AF",data$Center_image)
data$Sex<-ifelse(data$Sex=="TRUE", "F","M")


#Change variables to factors
data$Emotion=as.factor(data$Emotion)
data$Sex=as.factor(data$Sex)
str(data)
head(data)


######Exporting final file####
#export a file called data.csv that contains data from all the participants
write.csv(data, file="cleaned data/alldata.csv", row.names=FALSE)
