counter = 1
while (counter<=100):
    if counter>1 and counter%2 == 0 and counter%counter == 0:
        print("Prime")
    elif counter%3 == 0 and counter%5 == 0:
         print("fizzbuzz")
    
    elif counter%3 ==0:
          print("Fizz")
    elif counter%5 == 0:
         print("Buzz")
  
    else:
         print(counter)
    counter = counter + 1
     
