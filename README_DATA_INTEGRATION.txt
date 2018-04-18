query1.py | Janelle
    This file calls the crime API given by data.cityofchicago.org. For every distinct GroupID
    in our sortedManualRefSet.csv, this program finds the block address associated with that
    GroupID, establishes a list of the blocks 3 blocks away (including the original block), and
    calls the API to find all of the crimes within the blocks included in the list. After finding
    each crime and inserting that information in a temporary csv file, the program converts this
    data into a pandas dataframe in order to organize the data grouped by year, business, and crime
    type. I was not able to count the occurrences of arrests or on premises factors, but I was able
    to find the number of crimes per crime type. For some reason, I also could not find crimes for
    each GroupID in a list, but could find crimes for each GroupID individually.
        To run:
        python query1.py
        * creates csv file: query1.csv
        * this file reads from a csv called sortedManualRefSet.csv which is the team's reference
          allignment set


query2.py | Janelle
    This file uses data solely from sortedManualRefSet.csv. The data read in from our reference
    allignment data is converted to a pandas data frame in order to easily organize and break
    apart the data to train against the included crime statistics using supervised learning. I
    primarily used the sklearn library, which includes LogisticRegression and DecisionTreeClassifier.
    I was able to train a model for Logistic Regression technique, but could not correctly yield
    results using Decision Trees or Random Forests.
        To run:
        python query2.py
        * creates csv file: lrcsv.csv 
        * reads from sortedManualRefSet.csv
        
        
query3.py | Sohum
 Files Required:
query_3.py
sortedManualRefSet.csv

INSTRUCTIONS
------------

You must have a file in the same directory called sortedManualRefSet.csv.
Either the phyiscal file in the directory should be changed to this name
or the line of code in main that defines the file name should be adjusted accordingly
to properly run the program. 

This program operates under the assumption that the data from the manual reference data set
is of the following format:
-Crime Data: DateTime, CrimeType
-Census Data: Census Block
-Demographics Data: Approximated populations for three age groups within a census block.
		    0-19,20-64,>=65

I am lacking exact numbers and ages for who committed these crimes from the provided 
demographics data, so some assumptions had to be made in order to make computations.

Assumption One: Crimes of all different types committed within a census block are 
committed at the same frequency with each age group.  
Assumption Two: Because of the first assumption we must now use the approximated population data
and compute the number of crimes committed by each age group proportionally as different
numbers of people can exist in a given census block for each of the age ranges. So, this
assumption helps to give us a more realistic estimate of who commits crimes.  
For example: a census block with 10 crimes and a population spread of 30 50 20 would mean that 
3 5 2 crimes are committed respectively by each age group.


query4.py | Brandon
    To run:
    python query4.py
    * requires sortedManualRefSet.csv
    
    
query8.py | Sohum
Files Required:
query_8.py
sortedManualRefSet.csv

INSTRUCTIONS
------------

You must have a file in the same directory called sortedManualRefSet.csv.
Either the phyiscal file in the directory should be changed to this name
or the line of code in main that defines the file name should be adjusted accordingly
to properly run the program. 

This program runs under the assumption that certain attributes of food inspections
are in a designated and specific column from which the program will parse in order to 
mine the data.


query10.py | Brandon
    To run:
    python query10.py
    * requires sortedManualRefSet.csv
