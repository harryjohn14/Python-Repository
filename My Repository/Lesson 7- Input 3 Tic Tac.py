# The script below illustrates how to print a shape.
#  /  /  0
# -----  1
#  /  /  2
# -----  3
#  /  /  4
#  01234
"""

def drawField() :
    for row in range(5) :
        if row%2 == 0:
            for column in range(5) :
                if column%2 == 0 :
                    if column != 4:
                        print (" ", end = " ")
                else:
                    print (" ")
            else:
                print("|",end= "")
    else:
        print("-----")
drawField()

"""
def drawField(field) :
    for row in range(5) :           # 0,1,2,3,4
                                    # 0,.,1,.,2
        if row%2 == 0:              # 0 2 4 only passes
           practicalRow = int(row/2)     # 0,1,2
           for column in range(5) : # 0,1,2,3,4
                                    # 0,.,1,.,2
                if column%2 == 0 :  # 0 2 4 only passes
                    practicalColumn = int(column/2)   # 0,1,2
                    if column != 4:
                        print (field[practicalColumn][practicalRow],end = "")
                    else:
                        print(field[practicalColumn][practicalRow])
                else:
                    print("|",end= " ")
        else:
            print("---------")

Player = 1
currentField = [["  ", "  ", "  "], ["  ", "  ","  " ], ["  ", "  ", "  " ]]
## print(currentField) ...Alternatively, use
drawField(currentField)
while (True) :
    print("Players turn : ", Player)
    moveRow = int(input("Please enter the row number\n"))
    moveColumn = int(input("Please enter the column number\n"))
    if Player == 1 :  # make move for player one
        if currentField[moveColumn][moveRow] == " ":  # This prevent player 2 from overiding player 1
             currentField[moveColumn][moveRow]  = "X"
             Player = 2 
    else:
        # make move for player 2
        if currentField[moveColumn][moveRow] == " ":  #  # This prevent player 1 from overiding player 2
             currentField[moveRow][moveColumn]  = "O"
             Player = 1
    ## print(currentField) Alternatively, use
    drawField(currentField)





