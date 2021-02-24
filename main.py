#import panda 
import pandas as pd

class DataAnalyse:
  def __init__(self):
    df = pd.read_csv('monthlyvisitors.csv')
    TopThreeCountries(df)
    UserInput(df)
#reads the csv file with panda
df = pd.read_csv("monthlyvisitors.csv")

#function for the top three country of asia pacific
def TopThreeCountries(df):
  #Getting the headers/ country in the region
  HeaderSelected = df[['Year','Month', ' Hong Kong ', ' Korea, Republic Of ', ' China ', ' Japan ', ' Taiwan ']]
  #Get the years from the csv file from 2000 to 2010
  YearsSelected = HeaderSelected.iloc[265:396]
  CountriesSelected = YearsSelected[[ ' Hong Kong ', ' Korea, Republic Of ', ' China ', ' Japan ', ' Taiwan ']]

  #Get the total number of visitors on each country
  TotalVisitors = CountriesSelected.sum(axis=0)
  #sort the values in decending order
  MostVisitors_Descending = TotalVisitors.sort_values(ascending = False)
  #Print only the top 3 countries 
  Top3Countries = MostVisitors_Descending.head(3)
  print("These are the Top 3 Countries that Visited Singapore in the years 2000-2010.")
  print(Top3Countries)
  print("\n \n ")



  #User input function
def UserInput(df1):
  #variables for the year range 
  FirstLine = 0
  SecondLine = 0
  print('#' * 50)
  print("1.Asia Pacific\n2.South-Asia Pacific\n3.Europe\n4.Middle East\n5.South-East Asia\n6.North-America\n7.Australia\n8.Africa")
  #Loop for choosing the region
  while True:
    RegionChosen = input("Please Choose a region(e.g. 1,2,3 e.t.c)\n>")
    #Get the countries from selected region in the csv file
    if RegionChosen == "1":
      CountriesChosen = df1[[' Hong Kong ',' China ', ' Japan ', ' Taiwan ', ' Korea, Republic Of ']]
      break
    
    elif RegionChosen == "2":
      CountriesChosen = df1[[' India ',' Sri Lanka ', ' Pakistan ']]
      break
    
    elif RegionChosen == "3":
      CountriesChosen = df1[[' United Kingdom ', ' Germany ', ' France ', ' Italy ', ' Netherlands ',' Greece ', ' Belgium & Luxembourg ', ' Switzerland ', ' Austria ',' Scandinavia ', ' CIS & Eastern Europe ']]
      break

    elif RegionChosen == '4':
      CountriesChosen = df1[[' Saudi Arabia ', ' Kuwait ', ' UAE ']]
      break

    elif RegionChosen == '5':
      CountriesChosen = df1[[' Brunei Darussalam ', ' Indonesia ',' Malaysia ',' Philippines ', ' Thailand ', ' Viet Nam ', ' Myanmar ']]
      break

    elif RegionChosen == '6':
      CountriesChosen= df1[[' USA ', ' Canada ']]
      break

    elif RegionChosen == '7':
      CountriesChosen = df1[[' Australia ', ' New Zealand ']]
      break

    elif RegionChosen == '8':
     CountriesChosen = df1[[' Africa ']]
     break
    #Error checking 
    else:
      print('Error! Please select a valid region.')

  print("So you have chosen number", RegionChosen )
  #For the range of years 
  print("Please choose a range of years starting from 2000-2010.")
  #loop for the range of years
  while True:
    #Get the starting year = FirstYear
    FirstYear = input("Please enter the starting year.\n>")
    #Error checking if the input is numeric
    if FirstYear.isdigit() == False:
      print('ERROR!')
    #Get the ending Year = LastYear
    else:
      LastYear = input("Please enter the ending year.\n>")
      #Error checking if the input is numeric
      if LastYear.isdigit() == False:
        print("ERROR!")
      #changing bothe years to int for error checking below
      else:
        FirstYear = int(FirstYear)
        LastYear = int(LastYear)
        #Check if the years selected by user is within range
        if FirstYear in range(2000, 2010):
          if LastYear in range(2000, 2010):
            print("You have chosen", FirstYear, "and", LastYear)
            break
          #Error check for the starting year
          else:
              print("ERROR! Please choose a valid Ending year.")
             
        #Error check for the ending year
        else:
          print("ERROR! Please choose a valid starting year.")
  #All this is to change the variables to get the years in the .csv file
  #For the starting year 
  if str(FirstYear) == "2000":
          FirstLine = 264
  if str(FirstYear) == "2001":
          FirstLine = 277
  if str(FirstYear) == "2002":
          FirstLine = 289
  if str(FirstYear) == "2003":
          FirstLine = 301
  if str(FirstYear) == "2004":
          FirstLine = 313
  if str(FirstYear) == "2005":
          FirstLine = 325
  #For the ending year
  if str(LastYear) == "2000":
          SecondLine = 276
  if str(LastYear) == "2001":
          SecondLine = 288
  if str(LastYear) == "2002":
          SecondLine = 300
  if str(LastYear) == "2003":
          SecondLine = 312
  if str(LastYear) == "2004":
          SecondLine = 324
  if str(LastYear) == "2005":
          SecondLine = 336

  print("Line 1 is " + str(FirstLine) + " and Line 2 is " + str(SecondLine))

  #Get the years from the .csv file
  CountryYear = CountriesChosen.iloc[FirstLine:SecondLine]


  #Get the total sum of the countries
  FinalResult = CountryYear.sum(axis=0)
  #Sort it to decending order
  TopChosen = FinalResult.sort_values(ascending = False)
  #Print only top 3
  print(TopChosen.head(3))

#Main code
if __name__ == '__main__':
  #Run Code
  DataAnalyse()