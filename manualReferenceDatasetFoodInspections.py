import csv

def mergeData(restaurantsData, foodInspectionData,mergedSet):
    groupNum = 1
    counter = 0

    print(restaurantsData[17])
    print(foodInspectionData[19228])

    for row1 in restaurantsData:
        for row2 in foodInspectionData:
            row1Name,row1Address = row1.split(",")
            row2InspectionID,row2Address,row2dbaName,row2Risk,row2Results,row2InspectionDate,row2akaName = row2.split(",")
            if(((row1Name == row2dbaName) | (row1Name == row2akaName)) & (row1Address == row2Address)):
                foodInspection = 'Food Inspections'
                mergedSet.append(str(groupNum) + "," + foodInspection + "," + row2InspectionID + "," + row2Address + "," + row2dbaName + "," + row2dbaName + "," + row2Risk + "," + row2Results + "," + row2InspectionDate)
                counter  = counter + 1
        groupNum = groupNum +1
    print(counter)
    return mergedSet

def createOutputCSV(outputFile):
    outputCSV = open("foodInspections.csv", "w")
    headerRow = "GroupID,Data Source,SourceID,Address,Name,DBA Name,Risk,Results,Inspection Date\n"
    outputCSV.write(headerRow)
    for row in outputFile:
        #print(row)
        outputCSV.write(str(row) + "\n")
    outputCSV.close()
    print("FOOD INSPECTION CSV GENERATED")   

#Function to parse the CSV
#Returns list
def parseFoodInspectionCSV(csvFile, data):
    with open(csvFile) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        
        counter = 0
        for row in csvReader:
            if(counter != 0): #Skips header
                address = row[6].replace(",","").upper().strip()
                inspectionID = str(row[0])
                dbaName = row[1].replace(",","").upper()
                risk = row[5]
                results = row[12]
                inspectionDate = row[10]
                akaName = row[2].replace(",","").upper()
                data.append(inspectionID + "," + address + "," + dbaName + "," + risk + "," + results + "," + inspectionDate + "," + akaName)
            counter = counter+1
    return data

#Function to parse the CSV
#Returns list
def parseRestaurantCSV(csvFile, data):
    with open(csvFile) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        
        counter = 0
        for row in csvReader:
            if(counter != 0): #Skips header
                name = row[1].replace(",","").upper()
                address = row[6].replace(",","").upper().strip()
                data.append(name + "," + address)
            counter = counter+1
    return data

def main():
    print("PROGRAM START")

    foodInspectionFile = 'Food_Inspections.csv'
    restaurantsFile = '40_restaurants.csv'

    foodInspectionData = []
    restaurantsData = []

    restaurantsData = parseRestaurantCSV(restaurantsFile, restaurantsData)

    foodInspectionData = parseFoodInspectionCSV(foodInspectionFile, foodInspectionData)

    mergedSet = []
    mergedSet = mergeData(restaurantsData,foodInspectionData,mergedSet)
    print(mergedSet[0])

    createOutputCSV(mergedSet)

    print("PROGRAM END")

if __name__ == "__main__": main()