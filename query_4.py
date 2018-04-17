import csv

refData = open("sortedManualRefSet.csv")

csvReader = csv.reader(refData)
header = csvReader.__next__()

groupID			= header.index("GroupID")
name 			= header.index("Name")
address 		= header.index("Address")
reviewRating	= header.index("ReviewRating")
result 			= header.index("Result")
dataSource		= header.index("DataSource")

groupDict = dict()
counter = 1
n = 0
addr = 0
review = 0
countPass = 0
countFail = 0
conditions = 0
prevGroup = 0

for row in csvReader:

	group = row[groupID]
	data = row[dataSource]
	res = row[result]
	if (group == str(counter)):
		if (res == "Pass"):
			countPass += 1
		elif (res == "Fail"):
			countFail += 1
		elif (res == "Pass w/ Conditions"):
			conditions += 1
	else:
		groupDict[prevGroup] = [n, addr, review, countPass, conditions, countFail] 
		counter = counter + 1
		countPass = 0
		countFail = 0
		conditions = 0
		group = row[groupID]
		if (group == str(counter)):
			if (res == "Pass"):
				countPass += 1
			elif (res == "Fail"):
				countFail += 1
			elif (res == "Pass w/ Conditions"):
				conditions += 1

	prevGroup = group
	if (data == "Yelp"):
		n = row[name]
		addr = row[address]
		review = row[reviewRating]

#print(groupDict)

newValues = []
newValues.append(["Restaurant Name", "Address", "Average Review", "Pass", "Conditional", "Fail"])

for key, value in groupDict.items():
	newValues.append(value)

newFile = open("query_4_answer.csv", "w", newline = '')
with newFile:
	writer = csv.writer(newFile)
	writer.writerows(newValues)

newFile.close()
refData.close()