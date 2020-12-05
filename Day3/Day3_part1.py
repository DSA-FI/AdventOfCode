
#Code for the day 3 part 1 of Advent For Code -challenge

SlopeMap = open("Day3\\Day3_Data.txt", 'r')

Tree_Counter = 0
IgnoreFirstTree = True
PositionCounter = 0

for line in SlopeMap:

    line = line.rstrip()
    map_of_current_line = line
    

    while len(map_of_current_line) <= PositionCounter:
        map_of_current_line = map_of_current_line + line



    if map_of_current_line[PositionCounter] == "#" and IgnoreFirstTree == False:
        Tree_Counter = Tree_Counter + 1

     
    IgnoreFirstTree = False
    PositionCounter = PositionCounter + 3


print("\nOn current path you encounter", Tree_Counter, "trees.\n")
exit()
