"""
Name = input("Please enter your name : ")    # Basic python script to input data
print(Name)
Age = input("Please enter your age: ")
print(Age)


Age = int(input("Please enter your age: ")) # script allows converts a string input to an int output.
print(Age + 2)

Age = int(input("Please enter your age: ")) # script allows concatenation of integer and string
print(str(Age) + "2")

"""
"""
Scores = []

for i in range(5) :
    currentScore = int(input("Please enter your score: "))
    Scores.append(currentScore)
print(Scores)
"""
"""
Scores = []
for i in range(5) :
    currentScore = int(input("Please enter your score " + str(i) + ": "))
    Scores.append(currentScore)
print(Scores)

"""

Scores = []
for i in range(5) :
    currentScore = float(input("Please enter your score " + str(i + 1) + ": "))
    Scores.append(currentScore)
    print("The score you entered was :\n", currentScore)  # \n puts  currentScore on a new line
print(Scores)

