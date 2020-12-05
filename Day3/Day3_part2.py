
#Code for the day 3 part 2 of Advent For Code -challenge

SlopeMap = open("Day3\\Day3_Data.txt", 'r')

slopes = {"First slope":"1:1", "Second slope":"3:1", "Third slope":"5:1", "Fourth slope":"7:1", "Fift slope":"1:2"} #Dict = {<Slope>:<Right:Down>} 

for slope, pattern in slopes.items():
    
    SlopeMap.seek(0)
    Tree_Counter = 0
    IgnoreFirstTree = True
    PositionCounter = 0
    skip_counter = 1

    pattern = list(pattern)

    if pattern[2] != "1":
        skip_lines = int(pattern[2])
    else:
        skip_lines = 0

    amount_of_movement_right = int(pattern[0])

    for line in SlopeMap:

        if skip_lines != 0: #for skipping lines

            if skip_counter == skip_lines:
                skip_counter = 1
                continue
            else:
                skip_counter = skip_counter +1 

         
        line = line.rstrip()
        map_of_current_line = line
        

        while len(map_of_current_line) <= PositionCounter:
            map_of_current_line = map_of_current_line + line


        if map_of_current_line[PositionCounter] == "#" and IgnoreFirstTree == False:
            Tree_Counter = Tree_Counter + 1


        IgnoreFirstTree = False
        PositionCounter = PositionCounter + amount_of_movement_right


    slopes[slope] = Tree_Counter
            
            
results_multiplication = slopes["First slope"] * slopes["Second slope"] * slopes["Third slope"] * slopes["Fourth slope"] * slopes["Fift slope"] 

print("\nResults of how many trees you hit on each path:", slopes, "\nAnd result of their multiplication:", results_multiplication, "\n")
exit()