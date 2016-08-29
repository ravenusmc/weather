#Main File for the project.
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

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
  mainQuitSelection(choice)

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
    lowTemp()
  elif choice == 3:
    highTemp()
  elif choice == 4:
    averageRain()
  elif choice == 5:
    quit()

def meanTemp(weather):
  print("\033c")




#Auxillary Functions below this line.

def mainQuitSelection(choice):
  if choice == 1: 
    mainMenu()
  elif choice == 2:
    quit()

def quit():
  print("I am sorry you do not want to use this program!")
  print("Please come again!")




main()