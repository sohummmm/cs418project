README
Team: SMJCBGGGM


Note:
Sohum:
I created a file called author.py that accepts a one column csv file.  Each attribute of this column 
in the csv is a yelp user profile ID.  The file name of the csv file should be titled test.csv and placed 
in the same directory as the author.py file in order for the program to work properly. 
The python file accepts this csv and returns a author.csv file with all the appropriate data fields.
The only reason we could not provide this file is because through the Yelp Fusion API we could not
return a the user ID. Through the API we can only return the user name and some image URLs 
associated with the user.  Since, we could not solve this step we cannot present a author.csv deliverable 
but I will provide the author.py file as well as the test.csv file and author.csv file for reference 
so that we can get some credit for this portion of the project.

Janelle:
I produced review.csv and restaurant.csv which are the files obtained from using the Yelp Fusion API. Because Yelp's API only allows 3 reviews per restaurant to be obtained, review.csv is incomplete in terms of the number of reviews per restaurant. As for restaurant.csv, information such as outdoor seating, ambience, HasTV, etc. are missing because the API does not include that information. scrapeReview.csv contains information from webscraping. 

REFERENCES:
https://www.yelp.com/developers/documentation/v3/business_reviews
https://www.yelp.com/developers/documentation/v3/business_search
