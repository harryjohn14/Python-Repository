# The code below write vacation spots to vacation places.
"""
vacationSports = ["London", "Paris", "Moscow", "Calabar", "Lagos"]
vacationFile = open("vacationPlaces", "w")

for spots in vacationSports:
    vacationFile.write(spots + ", ")
vacationFile.close()
vacationFile = open("vacationPlaces","r")
theWholeFile = vacationFile.read()
print(theWholeFile)

vacationFile.close()
"""
# Compare the code below
vacationSports = ["London", "Paris", "Moscow", "Calabar", "Lagos"]
vacationFile = open("vacationPlaces", "w")

for spots in vacationSports:
    vacationFile.write(spots + ", ")
vacationFile.close()
vacationFile = open("vacationPlaces","r")

for line in vacationFile:
    print(line, end ="" )