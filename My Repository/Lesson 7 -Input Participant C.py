# The script below increments participants data
"""
participantsNumber = 3
participantsData = []

registeredPartcipants = 0

outputFile = open("participantsData.txt", "w")

while(registeredPartcipants < participantsNumber):
    tempPartData = []
    name = input("Please type your name: ")
    tempPartData.append(name)
    country = input("Please input your country: ")
    tempPartData.append(country)
    age = int(input("Please type your age"))
    tempPartData.append(age)

    print(tempPartData)
    participantsData.append(tempPartData)
    print(participantsData)

    registeredPartcipants += 1

for participants in participantsData :
    for data in participants :
        outputFile.write(str(data))
        outputFile.write(" ")
    outputFile.write("\n")

outputFile.close()
"""
# The script below creates a list that stores the ages of participants.

inputFile = open("participantsData.txt", "r")
inputList = []

for line in inputFile:
    temparticipant = line.strip().split() # strip is an inbuilt keyword that removes "\n" from the output file.
    print(temparticipant)                 # split separates all elements of the output and puts them in a list.
    inputList.append(temparticipant)
    print(inputList)

Age = {}
for part in inputList:
    tempage = int(part[-1]) #clarify this aspect of the code: Tempage is calling the last element(age) in the list
    if tempage in Age:
        Age[tempage] += 1
    else:
        Age[tempage] = 1
print(Age)

#inputFile.close()
"""
Alternatively, we ca write the age script as follows.

Age = {}
for part in inputList:
    if part[-1] in Age:
        Age[part[-1]] += 1
    else:
        Age[part[-1]] = 1
    
"""

# Lets run a script to extract the youngest and oldest from the partcipants.
print(Age)
# The script below prints out countries that participated.
Countries = {}
for part in inputList:
    tempcountry = part[1] 
    if tempcountry in Countries:
        Countries[tempcountry] += 1
    else:
        Countries[tempcountry] = 1

print("Countries that attended", Countries)

#print(Oldest)
#print(Youngest)
#print("Most occuring age is :", mostocurringAge,"width",counter,"participants")
Oldest = 0
Youngest = 100
mostocurringAge = 0
counter = 0


for tempage in Age:
    if tempage > Oldest:
        Oldest = tempage
    if tempage < Youngest:
        Youngest = tempage
    if Age[tempage] >= counter:
        counter = Age[tempage]
        mostocurringAge = tempage

