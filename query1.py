#!/bin/usr/env python

import csv
import sqlite3
from sodapy import Socrata
import pandas

# Year, Business Type (a,b,c) [grocery store, school restaurant] , Business Name, Address, Has Tobacco License,
# Has Liquor License, Crime Type, #Crimes, #Arrests, #On Premises

# from manual ref: business type, business name, address, has tobacco license, has liquor
# crime api: #crimes, #arrests, #on premises

# API constants
API_HOST = 'data.cityofchicago.org'
API_KEY = 'pMIREBy9SJVajtf7qXg0ZXoD9'
PATH = '6zsd-86xi'

client = Socrata(API_HOST, API_KEY)

referenceSet = open('sortedManualRefSet.csv', 'r')
referenceDict = csv.DictReader(referenceSet)

# read in sortedManualRefSet.csv as pandas dataframe?
df = pandas.read_csv('sortedManualRefSet.csv')

ret_df = pandas.DataFrame(columns=['Year', 'Business Type', 'Business Name', 'Address', 'Has Tobacco License',
                                   'Has Liquor License', 'Crime Type', '#Crimes', '#Arrests', '#On Premises'])

testCSV = open('testCSV.csv', 'w')
testWriter = csv.writer(testCSV)
testWriter.writerow(['Year', 'Business Type', 'Business Name', 'Address', 'Has Tobacco License',
                     'Has Liquor License', 'CrimeType', 'Arrest'])


# finds the block of a restaurant from manual ref based
# on the first crime row in that group
def findBlock(groupId):
    for row in referenceDict:
        if row['GroupID'] == str(groupId) and row['DataSource'] == 'Crimes':
            return row['Address']
    return ''


def find3blocks(addr):
    # addr in form XXXXX Street Name
    blocks = []
    blocks.append(addr)
    num, rest = addr.split('X', 1)
    print(num + ' | ' + rest)
    number = int(num)
    length = len(num)
    blocks.append(toBlock(number+1, length, rest))
    blocks.append(toBlock(number+2, length, rest))
    blocks.append(toBlock(number-1, length, rest))
    blocks.append(toBlock(number-2, length, rest))
    return blocks


# original : 002XX ...
# split : 002 X X ...
# params : num = 2, len = 3
# goal: return 002
def toBlock(num, len, rest):
    ret = ''
    if num == -1:
        for x in range(0, len):
            ret += '0'
        ret += '9'
        return ret + rest
    if num == -2:
        for x in range(0, len):
            ret += '0'
        ret += '8'
        return ret + rest
    if num == 10:
        for x in range(0, len-2):
            ret += '0'
        ret += '1'
        return ret + 'XX' + rest
    if num == 11:
        for x in range(0, len-2):
            ret += '0'
        ret += '2'
        return ret + 'XX' + rest
    else:
        for x in range(0, len - 1):
            ret += '0'
        ret += str(num)
        return ret + 'X' + rest


# returns the number of crimes in a given block
def crimesPer(address):
    offset = 0
    results = []
    prev = 1
    while prev:
        results += client.get(PATH, block=address, offset=offset)
        if prev == len(results): break
        prev = len(results)
        offset += 1000
    return len(results)


# returns number of crimes within 3 blocks of given addr
def totalCrimes(address):
    total = 0
    allBlocks = find3blocks(address)
    print(allBlocks)
    for i in allBlocks:
        total += crimesPer(i)
        print(total)
    return total


def businessName(id):
    df1 = df[df['DataSource'].str.contains('Y')]
    df2 = df1['Name'].tolist()
    return df2[id-1]


def has_t(id):
    for row in referenceDict:
        if row['GroupID'] == str(id):
            if 'tobacco' in str(row['LicenseDescription']):
                return True
    return False


def has_l(id):
    for row in referenceDict:
        if row['GroupID'] == str(id) and row['LicenseDescription'].contains('liquor'):
            return True
    return False


# returns result list of crimes by an address
def crime_by(addr):
    offset = 0
    results = []
    prev = 1
    while prev:
        results += client.get(PATH, block=addr, offset=offset)
        if prev == len(results): break
        prev = len(results)
        offset += 1000
    return results


def total_crime_by(id):
    total = []
    allBlocks = find3blocks(findBlock(id))
    print(allBlocks)
    for i in allBlocks:
        total += crime_by(i) #add all result lists together
    # print(total)
    return total


# method to write to csv? then from csv to pandas?
# 'Year', 'Business Type', 'Business Name', 'Address', 'Has Tobacco License',
#    'Has Liquor License', 'Crime Type', '#Crimes', '#Arrests', '#On Premises'
#
def find_result(id):
    # big_list is a list of dictionaries
    # addr = findBlock(id)
    big_list = total_crime_by(id)

    for c in big_list:
        write_to = []
        write_to.append(c['year'])
        write_to.append('c')
        write_to.append(businessName(id))
        write_to.append(findBlock(id))
        write_to.append(has_t(id))
        write_to.append(has_l(id))
        write_to.append(c['primary_type'])
        write_to.append(c['arrest'])
        testWriter.writerow(write_to) #csv contains crime data for everything


def convert_to_pandas(csv):
    df = pandas.read_csv(csv)
    df2 = df.groupby(['Year', 'Business Name', 'CrimeType']).size().reset_index(name='#Crimes')
    return df2


def main():
    print('PROGRAM START')

    num = len(df.GroupID.unique()) - 1
    #for x in range(1, num):
        # print(find3blocks(findBlock(x)))
        #find_result(x)
    #find_result(1)
    find_result(2)

    testCSV.close()
    readCSV = open('testCSV.csv', 'r')
    maindf = convert_to_pandas(readCSV)

    ret_csv = open('query1.csv', 'w')
    maindf.to_csv(ret_csv)

    #print(ret_df)
    print('PROGRAM END')

if __name__ == '__main__': main()


