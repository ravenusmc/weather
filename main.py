#Main File for the project.
import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 
from datetime import datetime

#Importing required file that I will need for the program
from valid import *

#Ideas: Maybe do something with record max year temperature data-break the data up into chunks? 

#The main function that will start the program. 
def main():
  print("\033c")
  print("[------------~-------~~~~-----------]")
  print("--Welcome to Charlotte Weather data--")
  print("[------------~-------~~~~-----------]")
  print("1. Look at Data")
  print("2. Quit")
  choice = int(input("What is your choice? "))
  while not mainValid(choice):
    print("Incorrect selection!")
    choice = int(input("What is your choice? "))
  if choice == 1:
    mainMenu()
  elif choice == 2:
    quit()

#This is the main menu of the program which will allow the user to select what they want to look at.
#Finally the data sample is set up here as well.
def mainMenu():
  print("\033c")
  weather = pd.read_csv('weather.csv')
  print("Welcome to the main menu!")
  print("1. Mean Temperature")
  print("2. Daily Low Temperatures")
  print("3. Daily High Temperatures")
  print("4. Average precipitation")
  print("5. Quit")
  choice = int(input("What is your choice? "))
  while not mainMenuValid(choice):
    print("Invalid Selection!")
    choice = int(input("What is your choice? "))
  if choice == 1: 
    meanTemp(weather)
  elif choice == 2:
    lowTemp(weather)
  elif choice == 3:
    highTemp(weather)
  elif choice == 4:
    averageRain(weather)
  elif choice == 5:
    recordmaxtemp(weather)
  elif choice == 6:
    quit()

#This funtion will show the user the average mean temp data. 
def meanTemp(weather):
  introLines()
  #Here I am setting up arrays to hold the dates and avgtemps
  dates, avgTemps = [], []
  #i will be a counter that as it increments will pull data from that specific slot.
  i = 0
  #These next two lines look at the specific columns. In this case, the date and actual_mean_temp
  #columns.
  dateData = weather[['date']]
  meanTemp = weather[['actual_mean_temp']]

  #A while loop is started which will loop through each date.
  while i < 364:
    #These next two lines get the date and the mean temperature at that specific date.
    date = dateData.iat[i,0]
    temp = meanTemp.iat[i,0]
    #This line is needed to convert the date to another format to use with matplotlib. 
    convertedDate = datetime.strptime(date, '%Y-%m-%d')
    #These next two lines will append the data at the specific date and average mean columns to
    #the dates and avgTemps arrays. 
    dates.append(convertedDate)
    avgTemps.append(temp)
    #The counter is increased by one which will bring it to the next row the next time the 
    #loop goes around. 
    i += 1

  #This line is used to configure the size of the display.
  fig = plt.figure(dpi=128, figsize=(10,6))
  plt.plot(dates, avgTemps, linewidth=2, c="blue")
  plt.title("Average Daily Temperature, 2014", fontsize=16)
  #This line will turn the dates, on the x axis diagnol for easy ready. 
  fig.autofmt_xdate()
  plt.xlabel("Date", fontsize=14)
  plt.ylabel("Temperature", fontsize=12)
  plt.show()
  mainQuitSelection()

#This function will show the user the average low temperatures. Most of the code is the same as 
#Mean Temp function which I could probably combine these.
def lowTemp(weather):
  introLines()
  dates, avgMinTemps = [], []
  i = 0
  dateData = weather[['date']]
  avgMinTemp = weather[['average_min_temp']]

  while i < 364:
    date = dateData.iat[i,0]
    temp = avgMinTemp.iat[i,0]
    convertedDate = datetime.strptime(date, '%Y-%m-%d')
    dates.append(convertedDate)
    avgMinTemps.append(temp)
    i += 1

  fig = plt.figure(dpi=128, figsize=(10,6))
  plt.plot(dates, avgMinTemps, linewidth=2, c="blue")
  plt.title("Average Minimun Temperatures", fontsize=16)
  fig.autofmt_xdate()
  plt.xlabel("Date", fontsize=14)
  plt.ylabel("Avg Min Temperature", fontsize=12)
  plt.show()
  mainQuitSelection()

#This function will show the user the average high temperatures.
def highTemp(weather):
  introLines()
  dates, avgHighTemps = [], []
  i = 0
  dateData = weather[['date']]
  avgHighTemp = weather[['average_max_temp']]

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

#This function will show the user the average precipitation.
def averageRain(weather):
  introLines()
  dates, avgRain = [], []
  i = 0
  dateData = weather[['date']]
  avgRainFall = weather[['average_precipitation']]

  while i < 364:
    date = dateData.iat[i,0]
    temp = avgRainFall.iat[i,0]
    convertedDate = datetime.strptime(date, '%Y-%m-%d')
    dates.append(convertedDate)
    avgRain.append(temp)
    i += 1

  fig = plt.figure(dpi=128, figsize=(10,6))
  plt.plot(dates, avgRain, linewidth=2, c="blue")
  plt.title("Average Rain Fall", fontsize=16)
  fig.autofmt_xdate()
  plt.xlabel("Date", fontsize=14)
  plt.ylabel("Avg Rain Fall (inches)", fontsize=12)
  plt.show()
  mainQuitSelection()

def recordmaxtemp(weather):
  introLines()

### Auxillary Functions below this line.

#This function will present the user with a menu at the end of each graphing function on whether 
#or not they want to return to the main menu or leave the program.
def mainQuitSelection():
  print("1. Return to main menu")
  print("2. Quit")
  choice = int(input("What is your choice: "))
  if choice == 1: 
    mainMenu()
  elif choice == 2:
    quit()

#Quit function that which will be displayed over and over again. 
def quit():
  print("I am sorry you do not want to use this program!")
  print("Please come again!")

#This function will be used for the opening lines for each function which is used with the program.
def introLines():
  print("\033c")
  print("Once the data appears, you must close the graph to move on")
  input("Press enter to see the Graph!")


main()