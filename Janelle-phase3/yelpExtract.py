#!/usr/bin/env python
"""Base code taken from Yelp Fusion Python/sample.py"""
from __future__ import print_function

import argparse
import json
import pprint
import requests
import sys
import urllib
import csv

try:
    from urllib.error import HTTPError
    from urllib.parse import quote
    from urllib.parse import urlencode
except ImportError:
    # Fall back to Python 2's urllib2 and urllib
    from urllib2 import HTTPError
    from urllib import quote
    from urllib import urlencode

# Group Yelp app API key
API_KEY= "Y6JG0Ur6iJ8l8NW7nsseUaUnsCnSlLM-wrvScUl14L8Ooi6p0K4-xVIHvOQdjoNN_F0TpzKe-1bj2Hw_Jb1CO_X7BrccbjxyNUH9Ko_dAjPUAjBl0WRii3_YxW-hWnYx"


# API constants, you shouldn't have to change these.
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.
REVIEW_SEARCH_PATH = '/v3/businesses/{id}/reviews'


# Defaults for our project
DEFAULT_TERM = 'restaurant'
DEFAULT_LOCATION = '60642'
SEARCH_LIMIT = 50
OFFSET = 50

resCsv = open('restaurant.csv', 'w')
revCsv = open('review.csv', 'w')
authCsv = open('author.csv', 'w')
restoUrlCsv = open('restaurantUrl.csv', 'w')


def request(host, path, api_key, url_params=None):
    """Given your API_KEY, send a GET request to the API.

    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        API_KEY (str): Your API Key.
        url_params (dict): An optional set of query parameters in the request.

    Returns:
        dict: The JSON response from the request.

    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

   # print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)
    #print(response.status_code)

    return response.json()


def search(api_key, term, location, offset):
    """Query the Search API by a search term and location.

    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.

    Returns:
        dict: The JSON response from the request.
    """

    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT,
        'offset': offset
    }

    return request(API_HOST, SEARCH_PATH, api_key, url_params=url_params)


def get_business(api_key, business_id):
    """Query the Business API by a business ID.

    Args:
        business_id (str): The ID of the business to query.

    Returns:
        dict: The JSON response from the request.
    """
    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path, api_key)

def get_review(api_key, business_id):
    # /businesses/{id}/reviews
    review_path = BUSINESS_PATH + business_id + '/reviews'
    return request(API_HOST, review_path, api_key)


def query_api(term, location):
    """Queries the API by the input values from the user.

    Args:
        term (str): The search term to query.
        location (str): The location of the business to query.
    """
    OFFSET = 0
    count = 0


    while count < 100:
        response = search(API_KEY, term, location, OFFSET)


        businesses = response.get('businesses')

        if not businesses:
            print(u'No businesses for {0} in {1} found.'.format(term, location))
            return

        print(u'{0} businesses found, querying business info...'.format(
            len(businesses)))


        for i in businesses:
            zip_code = i['location']['zip_code']
            if(zip_code == '60642' or zip_code == '60612'):
                print(i['id'])

                loc = i['location']['address1'] + ', ' + i['location']['city'] + ", " + i['location']['state'] + " " \
                    + i['location']['zip_code']

                categories = i['categories'][0]['alias']

                writeToCsv = i['id'] + ',' + i['name'] + ','  \
                    +loc + ',' + str(i['review_count']) + ',' + str(i['rating']) \
                    + ',' + categories + '\n'

                writeUrlToCsv = i['id'] + ',' + i['url'] + '\n'

                response = get_review(API_KEY, i['id'])
                reviews = response.get('reviews')
                # pprint.pprint(response, indent = 2)
                for r in reviews:
                    writeReview = r['id'] + ',' + i['id'] + ',' + r['user']['name'] + ',' + r['text'] + '\n'
                    revCsv.write(writeReview)
                resCsv.write(writeToCsv)
                restoUrlCsv.write(writeUrlToCsv)

                count = count + 1
        print(count)

        OFFSET = OFFSET + 50

    resCsv.close()
    revCsv.close()
    restoUrlCsv.close()


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-q', '--term', dest='term', default=DEFAULT_TERM,
                        type=str, help='Search term (default: %(default)s)')
    parser.add_argument('-l', '--location', dest='location',
                        default=DEFAULT_LOCATION, type=str,
                        help='Search location (default: %(default)s)')

    input_values = parser.parse_args()

    try:
        query_api(input_values.term, input_values.location)
    except HTTPError as error:
        sys.exit(
            'Encountered HTTP error {0} on {1}:\n {2}\nAbort program.'.format(
                error.code,
                error.url,
                error.read(),
            )
        )


if __name__ == '__main__':
    main()

