# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

from random import random
import time
randVal = random() #0.0<=N<1.0

upper = 1.0
lower = 0.0
#guess = 0.5

startTime = time.process_time()
while (True):
    guess = (upper + lower)/2      # note this input
    if guess == randVal:
        break
    elif guess< randVal:
        lower = guess
    else:
        upper = guess
endTime = time.process_time()
timeChange = endTime-startTime
print(guess)

#print(timeChange)



print("it took us :", endTime-startTime, "seconds")




# Compare the Code Below

randVal = random() #0.0<=N<1.0

upper = 1.0
lower = 0.0
guess = 0.5

startTime = time.process_time()
while (True):
   
    if guess == randVal:
        break
    elif guess< randVal:
        lower = guess
    else:
        upper = guess
    guess = (upper + lower)/2      # note this input
    
endTime = time.process_time()
timeChange = endTime-startTime
print(guess)