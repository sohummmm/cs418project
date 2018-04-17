import csv

refData = open("sortedManualRefSet.csv")

csvReader = csv.reader(refData)
header = csvReader.__next__()

groupID			= header.index("GroupID")
censusBlock		= header.index("CensusBlock")
month 			= header.index("Month")
avgTemp 		= header.index("AverageTemperature")
typeOfRobbery	= header.index("CrimeType")
dateTime 		= header.index("DateTime")

censusList = []
crimesList = []
weatherList = []

for row in csvReader:
	group 		= row[groupID]
	block 		= row[censusBlock]
	m 			= row[month]
	temp 		= row[avgTemp]
	crimeType 	= row[typeOfRobbery]
	date 		= row[dateTime]

	# Build CensusList
	if (block != ''):
		censusList.append([group, block])

	# Build Crime List
	if (crimeType != ''):
		date = date[5:7]
		if (date == "06"):
			date = "June"
			crimesList.append([group, date, crimeType])
		elif (date == "07"):
			date = "July"
			crimesList.append([group, date, crimeType])
		elif (date == "08"):
			date = "August"
			crimesList.append([group, date, crimeType])

	# Build Weather List
	if (m != ''):
		if (m == "June" or m == "July" or m == "August"):
			weatherList.append([group, temp, m])

censusAndCrime = []

for census in censusList:
	for crime in crimesList:
		if (census[0] == crime[0]):
			censusAndCrime.append([census[0], census[1], crime[1], crime[2]])

combinedList = []

for c in censusAndCrime:
	for w in weatherList:
		if (c[0] == w[0] and c[2] == w[2]):
			combinedList.append([c[1], c[2], w[1], c[3]])

previousBlock = combinedList[1][1]
newList = []
juneTotal = 1
juneRob = 1
julyTotal = 1
julyRob = 1
augTotal = 1
augRob = 1

for i in combinedList:
	currentBlock = i[0]
	if (currentBlock == previousBlock):
		if (i[1] == "June"):
			if (i[3] == "ROBBERY"):
				juneRob += 1
				juneTotal += 1
			else:
				juneTotal +=1
		elif (i[1] == "July"):
			if (i[3] == "ROBBERY"):
				julyRob += 1
				julyTotal += 1
			else:
				julyTotal += 1
		elif (i[1] == "August"):
			if (i[3] == "ROBBERY"):
				augRob += 1
				augTotal += 1
			else:
				augTotal += 1
	else:
		juneProbability = (juneRob / juneTotal) * 100
		newList.append([previousBlock, "June", i[2], "ROBBERY", juneProbability])
		julyProbability = (julyRob / julyTotal) * 100
		newList.append([previousBlock, "July", i[2], "ROBBERY", julyProbability])
		augProbability = (augRob / augTotal) * 100
		newList.append([previousBlock, "August", i[2], "ROBBERY", augProbability])
		
		juneTotal = 0
		juneRob = 0
		julyTotal = 0
		julyRob = 0
		augTotal = 0
		augRob = 0

		if (i[1] == "June"):
			if (i[3] == "ROBBERY"):
				juneRob += 1
				juneTotal += 1
			else:
				juneTotal +=1
		elif (i[1] == "July"):
			if (i[3] == "Robbery"):
				julyRob += 1
				julyTotal += 1
			else:
				julyTotal += 1
		elif (i[1] == "August"):
			if (i[3] == "Robbery"):
				augRob += 1
				augTotal += 1
			else:
				augTotal += 1

	previousBlock = currentBlock

counter = 0
newValues = []
newValues.append(["Census Block", "Month", "Avg. Temperature", "Type of Robbery", "Probability (%)"])
for i in newList:
	if (counter > 2):
		newValues.append(i)
	counter += 1

newFile = open("query_10_answer.csv", "w", newline = '')
with newFile:
	writer = csv.writer(newFile)
	writer.writerows(newValues)

newFile.close()
refData.close()

