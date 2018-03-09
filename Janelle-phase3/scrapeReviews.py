#!/usr/bin/env python

import urllib.request
from bs4 import BeautifulSoup
import csv
import json

f = open('scrapeReview.csv', 'w')

def soupUrl(url, id):
    example = url
    page = urllib.request.urlopen(example).read()

    soup = BeautifulSoup(page, 'html.parser')
    reviews = json.loads(soup.find('script', type='application/ld+json').text)
    """
        "review": [
            {"ratingRating": {"ratingValue":5},
             "datePublished": "2018-01-25",
             "description": "blah blah blah",
             "author": Dimitris K.}
            {...
    """
    views = reviews.get('review')
    num = reviews['aggregateRating']['reviewCount']
    max = 1

    if(num < 20):
        max = num
    else:
        max = 20

    count = 0
    while(count < max):
        singleReview = views[count]
        writeToCSV = id + ',' + singleReview['author'] + ',' + singleReview['description'] + '\n'
        f.write(writeToCSV)
        count += 1


#with open('restaurantUrl.csv') as urlcsv:
#   reader = csv.reader(urlcsv, delimiter=',')
#    for row in reader:
#        print(row[1])
z = open('restaurantUrl.csv', 'r')
for line in z:
    id, url = line.split(',')
    #print(id + '  ' + url + '\n')
    soupUrl(url, id)

z.close()
f.close()
