
Length = 10
ToPrint = "d"
for pos in range(1,Length + 1):
    print(ToPrint*pos)

for pos in range(Length-1,0,-1): # scripts means start at 0 and reduce at rate of one at a time.
    print(ToPrint*pos)
    