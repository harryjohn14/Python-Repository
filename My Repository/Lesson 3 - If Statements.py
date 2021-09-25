"""
This is a python script that takes three inputs, whereby two must be equal or greater 
than 70 for a fourth variable to be classified.
"""

Maths = int(input("Please type maths score: "))
English = int(input("Please type english score: "))
Science = int(input("Please type science score: "))
Status = "Promoted"

if Maths >= 70 and English >= 70 :
   Status = "Promoted"

elif Maths >= 70 and Science >= 70 :
   Status = "Promoted"
   
elif English >= 70 and Science >= 70 :
   Status = "Promoted"
    
else:
    Status = "Not Promoted"
      

print(Status)   
