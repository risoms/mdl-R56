###Compare SART Data with REDCap data###
library(plyr)
library(Hmisc)
library(tidyr)
library(dplyr)

#load sart and redcap datafiles
setwd("C:/Users/aaf2262/Box Sync/MDL Lab/MDL Projects/Projects/Attention Bias Methods/Data/Fall 2016/WF4 Data")
wf_accuracy<-read.csv("cleaned data/accmean.csv")
wf_emotion<-read.csv("cleaned data/AccEmotion.csv")
wf_sex<-read.csv("cleaned data/AccSex.csv")
redcap_data<-read.csv("redcap_data.csv")

redcap_data<-redcap_data[c(1,5:7,98,99,101:110,122,126)]

names(redcap_data)[2]<-"age"
names(redcap_data)[3]<-"gender"
names(redcap_data)[4]<-"race"
names(redcap_data)[5]<-"handedness"
names(redcap_data)[6]<-"honesty"

#create ID that matches SART ID
make_id <- function(x){
     x <- ifelse(nchar(x) == 3, paste("40", x, sep = ""), x)
  }

#create new 'id' column
redcap_data$id<-make_id(redcap_data$record_id)
wf_accuracy$id<-wf_accuracy$participant

accuracy<-join_all(list(redcap_data,wf_accuracy), by = c('id'))
accuracy<-accuracy[!is.na(accuracy$Accuracy.mean),]
accuracy<-accuracy[c(19,2:17,22)]
accuracy$overall_accuracy<-accuracy$Accuracy.mean
# accuracy$overall_sd<-accuracy$Accuracy.sd
accuracy<-accuracy[-c(18)]

#create data frames for each type of response rate and rename columns to identify which rate it is
acc_emo<-wf_emotion %>% select(participant:Accuracy.mean) %>%
  spread(Emotion, Accuracy.mean)
accuracy$neutral_accuracy<-acc_emo$NE
accuracy$sad_accuracy<-acc_emo$SA

acc_sex<-wf_sex %>% select(participant:Accuracy.mean) %>%
  spread(Sex, Accuracy.mean)
accuracy$male_accuracy<-acc_sex$M
accuracy$female_accuracy<-acc_sex$F

accuracy<-accuracy[c(1,7:22,2:6)]

#create file of Pearson's r correlations between mood ratings and hit/miss/CR/FA rates
wf_corrs<-rcorr(as.matrix(accuracy, type = "pearson"))
wf_corrs$r
write.csv(wf_corrs$r, file = "cleaned data/WF4_mood_correlations.csv")
write.csv(wf_corrs$P, file = "cleaned data/WF4_mood_cor_pvals.csv")

#create column of quantile splits
accuracy$masq_split <- with(accuracy, cut(masq_total, 
    breaks=quantile(masq_total, probs=seq(0,1, by=0.25)), 
    include.lowest=TRUE))

#Miss Rate plots by quartile split on depression
ggplot(accuracy, aes(x=overall_accuracy, y=masq_total, color=masq_split)) +
     geom_point(shape=1, position=position_jitter(width=1,height=.5)) +
     scale_colour_hue(l=50) + geom_smooth(method=lm, se=TRUE) + 
     ggtitle("Mean Accuracy by Quartile Split on Depression")
ggplot(accuracy, aes(x=neutral_accuracy, y=masq_total, color=masq_split)) +
     geom_point(shape=1, position=position_jitter(width=1,height=.5)) +
     scale_colour_hue(l=50) + geom_smooth(method=lm, se=TRUE) + 
     ggtitle("Accuracy on Neutral Faces by Quartile Split on Depression")
ggplot(accuracy, aes(x=sad_accuracy, y=masq_total, color=masq_split)) +
  geom_point(shape=1, position=position_jitter(width=1,height=.5)) +
  scale_colour_hue(l=50) + geom_smooth(method=lm, se=TRUE) + 
  ggtitle("Accuracy on Sad Faces by Quartile Split on Depression")
ggplot(accuracy, aes(x=male_accuracy, y=masq_total, color=masq_split)) +
  geom_point(shape=1, position=position_jitter(width=1,height=.5)) +
  scale_colour_hue(l=50) + geom_smooth(method=lm, se=TRUE) + 
  ggtitle("Accuracy on Male Faces by Quartile Split on Depression")
ggplot(accuracy, aes(x=female_accuracy, y=masq_total, color=masq_split)) +
  geom_point(shape=1, position=position_jitter(width=1,height=.5)) +
  scale_colour_hue(l=50) + geom_smooth(method=lm, se=TRUE) + 
  ggtitle("Accuracy on Female Faces by Quartile Split on Depression")

#create bias scores for each type of SART rate:
accuracy$emotion_bias <- accuracy$neutral_accuracy - accuracy$sad_accuracy
accuracy$gender_bias <- accuracy$male_accuracy - accuracy$female_accuracy

#Create another correlation matrix with bias scores:
accuracy$masq_split<-NULL
bias_corrs<-rcorr(as.matrix(accuracy, type = "pearson"))
bias_corrs$r
bias_corrs$P
write.csv(bias_corrs$r, file = "cleaned data/WF4 bias correlations.csv")
write.csv(bias_corrs$P, file = "cleaned data/WF4 bias cor pvalues.csv")

## Correlation scatter plots
ggplot(accuracy, aes(x=emotion_bias, y=masq_total)) +
  geom_point(shape=1) +
  geom_smooth(method=lm, se=FALSE) +
  ggtitle("Emotion Bias and Symptoms of Anxiety and Depression") +
  xlab("Emotion Bias") + ylab("MASQ Total Score")

ggplot(accuracy, aes(x=sad_accuracy, y=masq_total)) +
  geom_point(shape=1) +
  geom_smooth(method=lm, se=FALSE) +
  ggtitle("Accuracy on Sad Faces and Symptoms of Anxiety and Depression") +
  xlab("Accuracy on Sad Faces") + ylab("MASQ Total Score")

ggplot(accuracy, aes(x=overall_accuracy, y=masq_total)) +
  geom_point(shape=1) +
  geom_smooth(method=lm, se=FALSE) +
  ggtitle("Overall Accuracy and Symptoms of Anxiety and Depression") +
  xlab("Accuracy") + ylab("MASQ Total Score")

ggplot(accuracy, aes(x=neutral_accuracy, y=masq_total)) +
  geom_point(shape=1) +
  geom_smooth(method=lm, se=FALSE) +
  ggtitle("Accuracy on Neutral Faces and Symptoms of Anxiety and Depression") +
  xlab("Accuracy on Neutral Faces") + ylab("MASQ Total Score")




### RT and MASQ scores on Emotion Bias
alldata<-join_all(list(accuracy,rtmean), by = c('id'))

median(alldata$RT.mean)
alldata$RT.cutoff<-alldata$RT.mean>= median(alldata$RT.mean)
alldata$RT.cutoff<- ifelse(alldata$RT.cutoff==TRUE,"highRT","lowRT")

median(alldata$masq_total)
alldata$masq.cutoff<-alldata$masq_total>= median(alldata$masq_total)
alldata$masq.cutoff<- ifelse(alldata$masq.cutoff==TRUE,"highMASQ","lowMASQ")

rttest = t.test(emotion_bias~RT.cutoff, alldata, paired=FALSE, na.omit=TRUE)
rttest

masqtest = t.test(emotion_bias~masq.cutoff, alldata, paired=FALSE, na.omit=TRUE)
masqtest

par(mfrow=c(1,2))
boxplot(emotion_bias~RT.cutoff, data = alldata, ylab = "Emotion Bias")
boxplot(emotion_bias~masq.cutoff, data = alldata, ylab = "Emotion Bias")






# #### to compare SART and WF data within the group of ppts who completed both:
# # accuracy = WF data
# # r = sart data
# accuracy$id<-as.integer(accuracy$id)
# r$id<-as.integer(r$id)
# 
# alldata<-left_join(accuracy, r)
# wfsart<-rcorr(as.matrix(alldata, type = "pearson"))
# wfsart$r
# write.csv(wfsart$r,file="wf-sart-corrs.csv")


