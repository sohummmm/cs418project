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
        
