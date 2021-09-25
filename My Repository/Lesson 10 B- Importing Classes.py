# Picking from a list

import random as r

simpleList = [2,4,7,9,12]
pickElement = r.choice(simpleList)
print(pickElement)

print(simpleList)
r.shuffle(simpleList)
print(simpleList)

# Calling time library

import time
currentTime = time.process_time()
print("Hello")
print("World")
# pastTime = time.clock() : function has been removed from python use
pastTime = time.process_time()

print(pastTime - currentTime)

print("1")
time.sleep(2)
print(2)

for i in range(1,12): # increments the numbers after 
    print(i)
    time.sleep(i)