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

