from bs4 import BeautifulSoup
import requests
import csv

def main():
    #Defining Wiki URL to access
    AUTHOR_PATH = "https://www.yelp.com/user_details?userid="    
    list_of_user_URLS = []
    list_of_user_IDS = []
    #import and build user URLs
    with open('test.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            for attribute in row:
                fullUrl = AUTHOR_PATH + attribute
                list_of_user_URLS.append(fullUrl)
                list_of_user_IDS.append(attribute)

    for row in list_of_user_URLS:
        print(row)

    authors = []
    #requesting HTML from URL and saving as soup
    for authorInfo in list_of_user_URLS:
        req = requests.get(authorInfo)
        data = req.text
        soup = BeautifulSoup(data, "html.parser")

        ##AUTHOR ID
        authorID = authorInfo.split("userid=")[1]
        print(authorID)

        ##NAME
        name = soup.find("h1").text
        print(name)

        ##LOCATION
        location = soup.find("h3").text

        location = location.replace(",", "")

        print(location)

        pCount1 = {"class": ["user-passport-stats"]}
        pCount2 = soup.find_all("ul", pCount1) 
        pCount2 = str(pCount2)
        photoData = pCount2.split("strong>") 

        photoData[1] = photoData[1].split("</")[0]
        print(photoData[1])
        ##FRIEND COUNT
        friendCount = photoData[1]

        ##REVIEW COUNT
        photoData[3] = photoData[3].split("</")[0]
        print(photoData[3])
        reviewCount = photoData[3]

        ##PHOTO COUNT
        photoData[5] = photoData[5].split("</")[0]
        print(photoData[5])
        photoCount= photoData[5]

        authors.append(authorID + "," + name + "," + location + "," + reviewCount + "," + friendCount + "," + photoCount + "\n")

    csvFile = open("author.csv", "w")
    headerRow = "authorID,name,location,reviewCount,friendCount,photoCount\n"
    csvFile.write(headerRow)
    for row in authors:
        csvFile.write(row)
    csvFile.close()
    

if __name__ == "__main__": main()
