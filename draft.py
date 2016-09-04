#Main File for the project.
import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 
from datetime import datetime

print("\033c")
weather = pd.read_csv('weather.csv')




dates, avgHighTemps = [], []
i = 0
dateData = weather[['date']]
avgHighTemp = weather[['average_precipitation']]

while i < 364:
  date = dateData.iat[i,0]
  temp = avgHighTemp.iat[i,0]
  convertedDate = datetime.strptime(date, '%Y-%m-%d')
  dates.append(convertedDate)
  avgHighTemps.append(temp)
  i += 1

fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, avgHighTemps, linewidth=2, c="blue")
plt.title("Average High Temperatures", fontsize=16)
fig.autofmt_xdate()
plt.xlabel("Date", fontsize=14)
plt.ylabel("Avg High Temperature", fontsize=12)
plt.show()
mainQuitSelection()
  

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


