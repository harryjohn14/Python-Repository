# The script below increments participants data

participantsNumber = 5
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