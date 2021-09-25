import random

#random.seed(1)
randint = random.randint(0,10) #start<=N<=end
print(randint)

randfloat = random.random()  # q.q<=N<1.0
print(float)

randUniform = random.uniform(1,1100) # inclusion of ending value
print(randUniform)


# Another Script

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
import random
secretNumber = random.randint(1, 20)
print("I'm thinking of a nummber between 1 and 20.")
for guessesTaken in range(1, 7):
    print("Take a guess.")
guess = int(input())


# Another way of importing

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#from random import randint # Targeted at int variable
from random import uniform # Takes care of float variable

# randint = randint(0,10) #start<=N<=end
# print(randint)

# randFloat = random()  # q.q<=N<1.0   The Float code is not working.
# print(Float)

randUniform = uniform(1,1100) # inclusion of ending value
print(randUniform)



if guess < secretNumber:
    print("Your guess is to low")
elif guess > secretNumber:
    print("Your guess is to high")
# else:
#     break # This condition is the correct guess!

if guess == secretNumber:
    print("Good job! You guessed my number in " + str(guessesTaken) + "guesses!" )
else:
    print("Nope.The number I was thinking of was " + str(secretNumber)) 