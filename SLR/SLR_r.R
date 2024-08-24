dataset = read.csv('Salary_Data.csv')
#install.packages('caTools')
#library(caTools)

#Split the data
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset,split == TRUE)
test_set = subset(dataset, split == FALSE)

#Fit the regressor in the training set
regressor = lm(formula = Salary ~ YearsExperienceInField,
               training_set)
#summary(regressor)

predictions = predict(regressor, newdata = test_set)
predictions

#Visualize the training set
#install.packages("ggplot2")
#library('ggplot2')
#TRAINING SET

ggplot()+
  geom_point(aes(x = training_set$YearsExperienceInField, y = training_set$Salary),
            colour = 'red')+
  geom_line(aes(x = training_set$YearsExperienceInField, y = predict(regressor, newdata = training_set)),
            colour = 'blue')+
  xlab('Years Experience(Training Set)')+
  ylab("Salary")

#Test Set
ggplot()+
  
  geom_point(aes(x = test_set$YearsExperienceInField, y = test_set$Salary),
             colour = 'orange')+
  geom_line(aes(x = test_set$YearsExperienceInField, y = predict(regressor, newdata = test_set)),
            colour = 'black')+
  xlab('Years Experience(Test Set)')+
  ylab("Salary")

  
