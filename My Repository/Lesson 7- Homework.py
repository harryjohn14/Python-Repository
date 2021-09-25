

participantsNumber = 1
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

#outputFile = open("participantsData.txt", "r+")

inputText = participantsData
#print(inputText)

userInput = input("Please enter the filename: ")
# Code is not producing the right output
for userInput in inputText:
    if userInput != outputFile:
        filename = input("Please enter any statement: ")
    else:
        if userInput == outputFile:
            print(inputText)
             #filename= open("inputText", "r")


#print(operation)
