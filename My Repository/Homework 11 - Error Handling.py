"""
This is a python script that takes three inputs, whereby two must be equal or greater 
than 70 for a fourth variable to be classified.
"""

Maths = 23
English = 102
Science = 90
Status = "Promoted"

if Maths >= 70 and English >= 70 :
   Status = "Promoted"


elif Maths >= 70 and Science >= 70 :
     Status = "Promoted"

       
elif English >= 70 and Science >= 70 :
    Status = "Promoted"
    
else:
     Status = "Not Promoted"

try:
    if Maths<0 and English >100 :
        print("This is an error")
except:
    print("entered eception")

try:
    if Maths<0 and Science >100 :
        print("This is an error")
except:
    print("entered eception")
    
print("final")      

print(Status)   
