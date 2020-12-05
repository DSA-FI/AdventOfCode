
#Code for the day 3 part 1 of Advent For Code -challenge

SlopeMap = open("Day3\\Day3_Data.txt", 'r')

Tree_Counter = 0
IgnoreFirstTree = True
counter = 0

for line in SlopeMap:

    line = line.rstrip()

    counter = counter + 3
    SquareArray = list(line)
    
    while True: #problem starts here

        try:

            CurrentSquare = SquareArray[counter]
            break

        except IndexError:

            SquareArray.extend(SquareArray)
            

    if CurrentSquare == "#" and IgnoreFirstTree == False:
        Tree_Counter = Tree_Counter + 1

    IgnoreFirstTree = False



print("\nOn current path you encounter", Tree_Counter, "trees.\n")
exit()