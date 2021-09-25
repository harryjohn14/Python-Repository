# Code on sets and dictionary

Sets = {"Element 1", "Element 2", "Element 3", "Element 4"}
print (Sets)
if  "Element 1"  in Sets: 
    print("Yes")

"""
CountryList = []
for i in range(5):
    Country= input("Please input your country")
    CountryList.append(Country)
CountrySet = set(Country)
print(CountryList)
print(CountrySet)

CountryDictionary = {}

for Country in CountryList:
    if Country in CountryDictionary:
        CountryDictionary[Country] +=1
    else:
        CountryDictionary[Country] = 1
print(CountryDictionary)

"""

# The script below is used to track shoe purchases

"""
blackShoes = {44:5, 43: 7, 42: 6, 41: 2, 40: 3} # This is a dictionary
print(blackShoes)
while(True): # This could be written as  while(True==True)
    purchaseSize = int(input("Which shoes size do you want to purchase"))
    if purchaseSize < 0:
        break
    if blackShoes[purchaseSize] > 0: 
        blackShoes[purchaseSize] = blackShoes [purchaseSize] - 1   # This means Decrement blachshoes by 1
    else:        # compare d above code by blackshoes[purchaseSize] -= 1
        print("Shoes are no longer in stock")
    print(blackShoes)

"""
"""
s={1,2,3,[4,5]}
print(s)


dict = {}
dict[1] = 2
dict['1'] = 4
dict[1] += 2
count = 0

for key in dict:
    count += dict[key]

print(count)

"""

