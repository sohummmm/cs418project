Contributor: Sohum Mehrotra

Food Inspections for Manual Data Reference Set

I created some python files to parse through the Food_Inspections.csv file found on the 
Chicago Data Portal Datasets archive and I also parsed through a custom file with 40 yelp 
restaurants.
This custom file was made from a subset of the TA data.  We chose businesses alphabetically 
that were food-related to create our list.
Some of these restaurants were closed down and no longer have accurate addresses or records in 
the Food_Inspections.csv, so there are some missing food inspection entries for certain 
group IDs.  

Contriburot: Janelle Cueto

Crime Data for Manual Reference Data Set

I called an API provided by data.cityofchicago.org powered by Socrata for crime data. Given an 
address from our subset of 40 restaurants, I modified that address into a 'block' to fit the search
term for the crime data API. Instead of including crimes within 3 blocks of a given restaurant, I
decided to keep the crime data limited to the same block as the business because including data 
from 2001 to present would mean having to write thousands of crime data to our reference data set.
As advised on Piazza, I limited crime data to 100 crimes per restaurant. 

Contributor:

Census, Demographics and Weather for Manual Data Reference Set

- Changes were made to quite a few entries from the Yelp restaurant file because of erroneous data
- SourceID and Address values are blank for census data because sourceID wasn't present in the datasource and adding an address value didn't make sense. Population is as per census blocks. The block chosen was the block in which the restaurant was present. Census data was taken from city of Chicago's data portal.
- Source ID is blank for weather because the SourceID or IDs in the data source for weather was the combination of the weather station that recorded the temperature and the time stamp of the reading. The relevant weather columns for us (keeping the queries in mind) were the temperature and month. So I had to build that dataset from the weather data source. And therefore I couldn't include the source IDs of the main dataset. The average temperature was calculated by averaging temperature readings for all months of the year 2017. The address for the weather source is the address of the weather station that was chosen. This station was chosen as it is closest to the zipcodes we're working on.
- Demographics Data was obtained from:
https://www.cityofchicago.org/content/dam/city/depts/doit/general/GIS/Chicago_Maps/Census_Maps/Age_0to19.pdf
https://www.cityofchicago.org/content/dam/city/depts/doit/general/GIS/Chicago_Maps/Census_Maps/Age_20to64.pdf
https://www.cityofchicago.org/content/dam/city/depts/doit/general/GIS/Chicago_Maps/Census_Maps/Age_65Plus.pdf
- The above data is in a color coded map format and is based on the 2000 census because I couldn't find one for 2010. I had to manually prepare a datasheet from it. The community column is the neighborhood. The age group is divided into three parts: 0-19, 20-64, 65+. The population for each age group was calculated by taking averages and is an approximate.




