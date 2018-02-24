# Weekly Status Reports
### [Main Page](https://nuknuk48.github.io/cs418project/)
## Week One:
Sohum Mehrotra:

This week I created and set up the git repository for our team.  I developed and formatted our team web page.  I created my bio.  I created the weekly status reports page. I did some light research to discover Chicago land data in the apartment pricing sphere.  I plan to do more research in the upcoming week to find concrete data to make interesting observations about this data in the future.  A block that we are having is that we are not all focused on the same task, so our research is scattered.

Janelle Cueto:

This week I updated my bio for our team page. I also did some research around flights and pricing from Chicago to other major cities as well as looked into apartment search sites such as Zillow and Trilio to research what spaces are available in the Chicago area. I also researched hotels in the downtown Chicago area to compare pricing during spring break, and I found myself also looking greatly into each hotel's ratings and reviews. In the upcoming week, I plan to refine my own observations from the data I can obtain from common travel and lodging sites and I want to find sources for data sets that we'll extract data from later on. A block that I think we can easily resolve this week is that the team needs to get on the same page and we just need to meet together to decide how we'll move forward in terms of group work. 

Brandon Goodman Gibis:

This week I updated my bio for our team page. I researched Health reports in the city of Chicago, specifically Morbidity and Clinical Care of the population from the Chicago Health Atlas. Next week I plan on finding 1-2 more sources, 1 on Health reports and 1 on another category. One issue I noticed was that the data on the Health reports from the website I used was very brief. I hope to find a more extensive source to use for our project.

Glenn Mascarenhas:

For the 1st week I added my bio to the our project webpage and I looked for data sets that are related to the city of Chicago. Being an aviation enthusiast, I searched for data related to Chicago's O'Hare airport and I came across the Chicago Deparment of Aviation's website: flychicago.com which is not only responsible for providing basic arrival/departure information of flights at O'Hare and Midway, but also maintains statistical data on the monthly aircraft operations, passenger volumes and cargo tonnage at both these airports. My challenge for week 2 would be to analyze this data, and figure out what aspects make it a good candidate to be used in Data Science. I would also look for the useful information that I can extract from it, which could give an insight to the CDA and could be used to predict future growth/ decline in each of the above mentioned sectors and the factors affecting them. I noticed that the data is available as pdf files for each month (for a period of 18 years) so I might not be able to use this data directly in the format provided as it would be tough to manipulate it. Besides this, I'm also in search for other interesting datasets that can be added to the Data Discovery deliverable of week 2.


## Week Two:
Sohum Mehrotra:

This week I found two valuable sources for the data discovery portion of this project.  The real estate database company Zillow has provided data on home values, listings, as well as rental values and listings and real estate forecasting.  Zillow provides hundredes of excel files consisting of zip codes, neighborhoods, pricings etc.  This kind of data can be referenced against datasets containing locations in chicago as well as demographics to see what kind of real estate different demographics own. The second source I found was the City of Chicago Data Portal. This repository has thousands of data sets that cover a variety of categories such as Buildings, Transportation, Finances, Public Safety, Sanitation, and many other topics.  This site provides a visualization tool to view the tables as well as the geographical distribution of data that pertain to their respective location in Chicago.  For the next week, I plan to discuss with my team what topics we should focus our research on and consolidate all of our findings to help set a course for the semester, so that we can start data scraping and analysis.

Brandon Goodman Gibis:

For week two I was able to find three websites for data discovery. The Chicago Health Atlas provided information on morbitity, hospitalizations and access to health care in Chicago. The Statistic Atlas provided tables and graphs of income, demographics, and race and ethnicity of the city's population. The World Population Review had tables on the yearly population, growth and growth rate. Next week I plan to start scraping the data. At the moment there does not appear to be anything blocking me from doing my work.

Janelle Cueto:

This week I found three sources: skyscanner, OpenTable, and CPS.edu. I explored each site to find what kind of information they provided, and tried to relate each source to Chicago and its people in general. I thought about how this data would fit into a data set that could be joined with the attributes in the Data Extraction section. For example, looking at OpenTable and searching for restaurants in Chicago made me realize that I could relate cuisine type, price points and ratings to the demographic of that location. For the upcoming week, I plan to start thinking about how I want to begin extracting data off of census.gov and Chicago's data portal. As for scraping data from Yelp, I wonder what exactly we are trying to find about restaurants in Chicago. Again, one of the blocks I see for our team in general is a lack of actual communication. We've been doing much of our work chatting online but I'd like to be able to meet all together to work on our stuff. 

Glenn Mascarenhas: 

In week 2 I worked on searching for datasets that were related to the city of Chicago. The three datasets that I found were: 1) Air traffic data at O'Hare and Midway from the Chicago Department of Aviation's website flychicago.com 2) Weather data for the Chicago area from weather.gov and 3) Data on the history of theatre in Chicago on chicagotheatrehistoryproject.org. I read through each of these datasets in order to understand them, their attributes and to also identify how they could be joined with datasets mentioned in the data extraction section. For each of the datasets I researched, I found that they are present in different formats eg. flychicago's dataset was a bunch of pdfs while the theatre history dataset was a directory of html pages.  I also made the final compiled report for this week's data discovery deliverable. Before I start next week's data extraction work, I plan to do some study on web scraping as I'm not much familiar with it and we need it for scraping data from Yelp. 

## Week Three:

Brandon Goodman Gibis:

This week I began to research the following categories for our data extraction, Business Licenses, Food Inspections, Crime, Census, Demographics, and weather from the City of Chicago’s data portal and census.gov. Once I figured out how this data was stored, my intitial idea was to use BeautifulSoup in order to pull the data from the site. Next week I plan to actual pull the data from the website and store it for later use. At the moment the only thing stopping me from reaching my goal is whether or not the use of BeautifulSoup will work for this project.

Sohum Mehrotra:

In week 2, I started to investigate the specific sources I found in the data extraction portion of the project.  I increased my understanding of some of the real estate data provided by Zillow and discovered that Zillow provides their own special index that serves as a ranking tool to try and make general comparisons between different kinds of listings with different attributes.  In a sence the Zillow Home Value Index helps to bridge the gap between the endless possible combinations of house and apartment configurations (ie. different number of bedrooms, baths, square feet, pricing etc).  The data from Zillow can be exported through the website, so web scraping would not be necessary here, so I will start performing some analysis on the data that is readily available from the site and see what kind of information I can garner from these datasets.  I will try to use this as a bit of a learning experience, so that I can be more efficient in understanding data and creating generic functions that I can apply on any dataset.


Glenn Mascarenhas:

Our team was assigned zip code: 60642 this week for extracting restaurant data from Yelp. The first thing that I did was to find the location of this zip code on Google Maps. I then headed to Yelp and searched for restaurants by this zip code. It's very true that although you enter a zip code, Yelp doesn't sort the results as per the code you've entered so after some 'find'ing and filtering I finally got a count of all the restaurants and it was approximately 59 which is much lower than the required 100. Morevoer, the number of reviews for quite a few were much below 20 therefore we might need to expand our search to a wider area. Besides this, I downloaded the Business Licenses and Food Inspection datasets for the zip codes 60601 to 60607 from data.cityofchicago.org. This was an easy task as it required just a little filtering and searching to do. The files downloaded are in .csv format for Excel.
