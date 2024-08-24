dataset = read.csv('Data.csv')

#replace any missing data with the mean of the column
#replace missing age

dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)), dataset$Age)


dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave(dataset$Salary, FUN = function(x)mean(x, na.rm =TRUE)), dataset$Salary)

#Encode our categorical data
dataset$City = factor(dataset$City, levels = c('Syracuse', 'Oswego','Albany','Buffalo'), labels = c(1,2,3,4))

factor(dataset$Purchased, levels = c("Yes", "No"), labels = c(1, 2))


#split into a test and training set
#install.packages('caTools')
library(caTools)
#set Random seed
set.seed(123)

#split data 
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)




#x,na.rm
#albany and then buffalo

