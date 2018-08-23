					#######Center Image Paradigm Data Analysis######
###Import Data
setwd("C:/Users/aaf2262/Box Sync/MDL Lab/MDL Projects/Projects/Attention Bias Methods/Data/Fall 2016/WF4 Data/cleaned data")
data=read.csv("FinalCleanData.csv")
str(data)
head(data)
tail(data)
dim(data)
colnames(data)

library(doBy)


rtmean=summaryBy(RT.mean~participant, data, na.rm=TRUE)
rtmean
names(rtmean)[1]<-"id"
names(rtmean)[2]<-"RT.mean"


######Obtaining summary info for each participant########
###Accuracy & RT
rbavrgall=summaryBy(RT+Accuracy~participant+Sex+Emotion, data, FUN=c(mean, sd), na.rm=TRUE)
rbavrgall
####Save RT & Accuracy .csv file
write.csv(rbavrgall, file=("RTAccAvrgAll.csv"))
#IF NEED TO DELETE participant
# rbavrgall = rbavrgall[!(rbavrgall$participant=="207"),]
# rbavrgall
# #SAVING CSV FILE W/ DELETED PARTICIPANTS
# paste(path, "/RTAccAvrg(GOODSUBJ).csv", sep="")
# write.csv(rbavrgall, paste(path,"/RTAccAvrgAll(GOODSUBJ).csv", sep=""), row.names=FALSE)

####Accuracy####
#Looking at Accuracy by participant
accuracy = summaryBy(Accuracy~participant, data, FUN=mean)
accuracy

summary(accuracy)
OverallMeanAccuracy = mean(accuracy$Accuracy.mean)
OverallMeanAccuracy
OverallMeanSD = sd(accuracy$Accuracy.mean)
OverallMeanSD

lowA=ifelse(accuracy$Accuracy.mean<=(OverallMeanAccuracy-(2*OverallMeanSD)), 1, 0)
table(lowA)
#Add shortA row to data frame
accuracy$lowA = lowA
accuracy
#Would have to delete ids w/ low accuracy
table(accuracy$Accuracy.mean<"0.3")
#Take out 3 people with less than 30% accuracy
accuracy$excludeA=ifelse(accuracy$Accuracy.mean<=0.3, 1, 0)
accuracy
write.csv(accuracy, file="accuracy_all.csv")

accuracy = accuracy[!(accuracy$participant=="40436"),]
accuracy = accuracy[!(accuracy$participant=="40460"),]
accuracy = accuracy[!(accuracy$participant=="40463"),]

accuracy
write.csv(accuracy, file=("accmean.csv"))

## Low accuracy ppts: 40436, 40460, 40463

###Accuracy by Emotion
accravrg = summaryBy(Accuracy~participant+Emotion, data, FUN=c(mean, sd))
accravrg
#Deleting 3 participants with low accuracy
accravrg = accravrg[!(accravrg$participant=="40436"),]
accravrg = accravrg[!(accravrg$participant=="40460"),]
accravrg = accravrg[!(accravrg$participant=="40463"),]
accravrg
acctest = t.test(Accuracy.mean~Emotion, accravrg, paired=TRUE, na.omit=TRUE)
acctest
accanova = aov(Accuracy.mean~Emotion + Error(participant/Emotion), accravrg)
summary(accanova)
#Save file
# paste(path1, "/AccEmotion.csv", sep="")
write.csv(accravrg, file=("AccEmotion.csv"))


###Accuracy by Sex
accsavrg = summaryBy(Accuracy~participant+Sex, data, FUN=c(mean, sd))
accsavrg
accsavrg = accsavrg[!(accsavrg$participant=="40436"),]
accsavrg = accsavrg[!(accsavrg$participant=="40460"),]
accsavrg = accsavrg[!(accsavrg$participant=="40463"),]
accsavrg
accstest = t.test(Accuracy.mean~Sex, accsavrg, paired=TRUE, na.omit=TRUE)
accstest
#Save file
write.csv(accsavrg, file=("AccSex.csv"))

###Accuracy by Emotion & Sex
accavrg = summaryBy(Accuracy~participant+Emotion+Sex, data, FUN=c(mean, sd))
accavrg
accavrg = accavrg[!(accavrg$participant=="40436"),]
accavrg = accavrg[!(accavrg$participant=="40460"),]
accavrg = accavrg[!(accavrg$participant=="40463"),]
accavrg
#Save file
write.csv(accavrg, file=("AccEmotionSex.csv"))

####RT######
###RT by Emotion
rtravrg = summaryBy(RT~participant+Emotion, data, FUN=c(mean, sd))
rtravrg
rtravrg = rtravrg[!(rtravrg$participant=="40436"),]
rtravrg = rtravrg[!(rtravrg$participant=="40460"),]
rtravrg = rtravrg[!(rtravrg$participant=="40463"),]
rtravrg
rttest = t.test(RT.mean~Emotion, rtravrg, paired=TRUE, na.omit=TRUE)
rttest
#Save file
write.csv(rtravrg, file=("RTEmotion.csv"))

###RT by Sex
rtsavrg = summaryBy(RT~participant+Sex, data, FUN=c(mean, sd))
rtsavrg
rtsavrg = rtsavrg[!(rtsavrg$participant=="40436"),]
rtsavrg = rtsavrg[!(rtsavrg$participant=="40460"),]
rtsavrg = rtsavrg[!(rtsavrg$participant=="40463"),]
rtsavrg
rtstest = t.test(RT.mean~Sex, rtsavrg, paired=TRUE, na.omit=TRUE)
rtstest
#Save file
write.csv(rtsavrg, file=("RTSex.csv"))

###RT by whether correct or incorrect
rtcavrg=summaryBy(RT~participant+Emotion+Correct, data, FUN=c(mean, sd), na.rm=TRUE)
rtcavrg
rtcavrg = rtcavrg[!(rtcavrg$participant=="40436"),]
rtcavrg = rtcavrg[!(rtcavrg$participant=="40460"),]
rtcavrg = rtcavrg[!(rtcavrg$participant=="40463"),]
rtcavrg
write.csv(rtcavrg, file=("rtcavrg.csv"))

######Obtaining summary info for cue location & Emotion########
#create Cue_position column
for (i in 1:dim(data)[1]){
  if(data$C1[i]=="1"){
    data$Cue_position[i]="1"}
  else if (data$C2[i]=="2"){
    data$Cue_position[i]="2"}
  else if (data$C3[i]=="3"){
    data$Cue_position[i]="3"}
  else if (data$C4[i]=="4"){
    data$Cue_position[i]="4"}
  else {data$Cue_position[i]="0"}
}

data$Cue_position=as.factor(data$Cue_position)
str(data)

###Accuracy, Cue Location, & Emotion
CueEmotionAcc=summaryBy(Accuracy~participant+Cue_position+Emotion, data, FUN=c(mean, sd), na.rm=TRUE)
CueEmotionAcc
####Save RT & Accuracy .csv file
write.csv(CueEmotionAcc, file=("CueEmotionAcc.csv"))

###Accuracy & Cue Location
CueAcc=summaryBy(Accuracy~participant+Cue_position, data, FUN=c(mean, sd), na.rm=TRUE)
CueAcc
####Save RT & Accuracy .csv file
write.csv(CueAcc,file=("CueAcc.csv"))

###Accuracy & Cue Location Without Participant
CueAccuracy=summaryBy(Accuracy~Cue_position, data, FUN=c(mean, sd), na.rm=TRUE)
CueAccuracy
####Save RT & Accuracy .csv file
write.csv(CueAccuracy, file=("SimpleCueAccuracy.csv"))

###Accuracy & Cue Location & Emotion without participant
CueEmotionAccuracy=summaryBy(Accuracy~Cue_position+Emotion, data, FUN=c(mean, sd), na.rm=TRUE)
CueEmotionAccuracy
####Save RT & Accuracy .csv file
write.csv(CueEmotionAccuracy, file=("SimpleCueEmotionAccuracy.csv"))

###Save RT .csv file
# write.csv(rtavrgall, paste(path,"/rtavrgall.csv", sep=""), row.names=FALSE)


par(mfrow=c(1,2))
boxplot(Accuracy.mean~Emotion, data = accravrg, ylab = "Accuracy")
boxplot(Accuracy.mean~Sex, data = accsavrg, ylab = "Accuracy")

par(mfrow=c(1,2))
boxplot(RT.mean~Emotion, data = rtravrg, ylab = "RT")
boxplot(RT.mean~Sex, data = rtsavrg, ylab = "RT")

