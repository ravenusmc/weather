#Main File for the project.
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from datetime import datetime

print("\033c")
weather = pd.read_csv('weather.csv')

# date = weather[['date']]
# print(date.iat[2,0])
# test = date.iat[2,0]
# print(datetime.strptime(test, '%Y-%m-%d'))


dates = [] 
i = 0
dateData = weather[['date']]

while i < 364:
  date = dateData.iat[i,0]
  convertedDate = datetime.strptime(date, '%Y-%m-%d')
  print(convertedDate)
  dates.append(convertedDate)
  i += 1

print(dates)
  






#This will get the date data that I need in the correct format
# date = '2014-7-1'
# print(datetime.strptime(date, '%Y-%m-%d'))



#Getting the specific column I want-in this case the mean temp column
# meanTemp = weather[['actual_mean_temp']]
# date = meanTemp.loc[[date]]
# print(date)


#Getting the specific column I want-in this case the mean temp column
# meanTemp = weather[['actual_mean_temp']]
# print(meanTemp.iat[3,0])

#meanTemp = weather[['actual_mean_temp']]

#Temperature loop-It works!!!
# avgTemps = []
# i = 0
# while i <= 364:
#   temp = meanTemp.iat[i,0]
#   avgTemps.append(temp)
#   i += 1 
# print(avgTemps)


