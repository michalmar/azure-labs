#---
#title: "Train and deploy your first model with Azure ML"
#author: "David Smith"
#date: "`r Sys.Date()`"
#output: rmarkdown::html_vignette
#vignette: >
#  %\VignetteIndexEntry{Train and deploy your first model with Azure ML}
#  %\VignetteEngine{knitr::rmarkdown}
#  \use_package{UTF-8}
#---

setwd("~/azure-labs/HOL07-AML-R")


nassCDS <- read.csv("train-and-deploy-first-model/nassCDS.csv", 
                     colClasses=c("factor","numeric","factor",
                                  "factor","factor","numeric",
                                  "factor","numeric","numeric",
                                  "numeric","character","character",
                                  "numeric","numeric","character"))

accidents <- na.omit(nassCDS[,c("dead","dvcat","seatbelt","frontal","sex","ageOFocc","yearVeh","airbag","occRole")])
accidents$frontal <- factor(accidents$frontal, labels=c("notfrontal","frontal"))
accidents$occRole <- factor(accidents$occRole)
accidents$dvcat <- ordered(accidents$dvcat, 
                          levels=c("1-9km/h","10-24","25-39","40-54","55+"))

# saveRDS(accidents, file="accidents.Rd")

accidents
summary(accidents)



mod <- glm(dead ~ dvcat + seatbelt + frontal + sex + ageOFocc + yearVeh + airbag  + occRole, family=binomial, data=accidents)
summary(mod)
predictions <- factor(ifelse(predict(mod)>0.1, "dead","alive"))
accuracy <- mean(predictions == accidents$dead)


print(accuracy)



##### use Model#################################################################

newdata <- data.frame( # valid values shown below
 dvcat="10-24",        # "1-9km/h" "10-24"   "25-39"   "40-54"   "55+"  
 seatbelt="none",      # "none"   "belted"  
 frontal="frontal",    # "notfrontal" "frontal"
 sex="f",              # "f" "m"
 ageOFocc=22,          # age in years, 16-97
 yearVeh=2002,         # year of vehicle, 1955-2003
 airbag="none",        # "none"   "airbag"   
 occRole="pass"        # "driver" "pass"
 )

prob <- predict.glm(mod, newdata)
prob

factor(ifelse(predict.glm(mod, newdata)>0.1, "dead","alive"))
