#!/bin/usr/env python

# compute probability of types of crime given address
# types: assault, battery, burglary, criminal damage, criminal trespass, deceptive practice, motor veihicle theft
#        narcotics, other offense, robbery, sex offense, theft
# group by primary_type


import csv
import sqlite3
from sodapy import Socrata
import pandas
import numpy
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
import statsmodels.api as sm
from sklearn import tree
# import pylab as pl

# API constants
API_HOST = 'data.cityofchicago.org'
API_KEY = 'pMIREBy9SJVajtf7qXg0ZXoD9'
PATH = '6zsd-86xi'

client = Socrata(API_HOST, API_KEY)

referenceSet = open('sortedManualRefSet.csv', 'r')
referenceDict = csv.DictReader(referenceSet)

# read in sortedManualRefSet.csv as pandas dataframe?
df = pandas.read_csv('sortedManualRefSet.csv')

fieldnames = ['Address', 'CrimeType']
data1 = open('data1.csv', 'w')
data1write = csv.DictWriter(data1, fieldnames=fieldnames)
data1write.writeheader()

# create new data from manual ref data
# returns training model?
def refineData():
    for row in referenceDict:
        if row['DataSource'] == 'Crimes':
            data1write.writerow({'Address': row['Address'], 'CrimeType': row['CrimeType']})
    data1.close()


def dictToPandas(csv):
    tempCsv = open('data1.csv', 'r')
    df = pandas.read_csv(tempCsv)
    return df


def toTrain(df):
    retdf = df.groupby(['Address', 'CrimeType']).size().reset_index(name='#Crimes')
    dummy_types = pandas.get_dummies(retdf['CrimeType'])
    # print(dummy_types.head())
    cols_to_keep = ['Address', 'CrimeType', '#Crimes']
    retData = retdf[cols_to_keep].join(dummy_types.ix[:, 'ASSAULT':])
    # print(retData.head())
    return retData


# returns new dataset(?) containing probabilities for each crime type given an address
# using logistic regression
def log_reg(data):
    lrdf = dictToPandas(data)
    lrdf2 = toTrain(lrdf) # create dataset to perform logistic regression
    #print(lrdf2)
    X = lrdf2.loc[:, '#Crimes']
    y = lrdf2.loc[:, 'ASSAULT':]
    lr = LogisticRegression()
    lr.fit(y, X)

    lrcsv = open('lrcsv.csv', 'w')
    fieldnames = lrdf2.columns.get_values()

    lr_dict = csv.writer(lrcsv)
    lr_dict.writerow(fieldnames)
    lr_array = lr.predict_proba(y) # returns an array
    #print(lr_array)

    for index, row in lrdf2.iterrows():
        write_to = []
        write_to.append(row['Address'])
        write_to.append(row['CrimeType'])
        write_to.append(row['#Crimes'])
        write_to.extend(lr_array[index])
        lr_dict.writerow(write_to)

    lrcsv.close()
    return lr


def dec_tree(data):
    dtdf = dictToPandas(data)
    dtdf2 = toTrain(dtdf)
    X = dtdf2.loc[:, '#Crimes':]
    Y = dtdf2.loc[:, 'CrimeType']

    dt = tree.DecisionTreeClassifier()
    dt.fit(X, Y)
    print(dt.predict_proba(X))
    return dt



def main():
    print('PROGRAM START')
    refineData()
    log_reg(data1)
    dec_tree(data1)
    print(log_reg(data1))

    print('PROGRAM END')

if __name__ == '__main__': main()
