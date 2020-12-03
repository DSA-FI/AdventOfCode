
#Code for the day 2 part 1 of Advent For Code -challenge

file_handler = open("Day2\\Day2_Data.txt", 'r')

correctPassCounter = 0

for each_line in file_handler:
    each_line = each_line.rstrip()

    each_line = each_line.split(":")
    PasswordPolicy = each_line[0]
    PasswordPolicy = PasswordPolicy.split()
    
    #policy letter
    PasswordPolicy_length = PasswordPolicy[0]
    PasswordPolicy_letter = PasswordPolicy[1]

    #Policy length
    PasswordPolicy_length = PasswordPolicy_length.split("-")
    FromNumber = int(PasswordPolicy_length[0])
    ToNumber = int(PasswordPolicy_length[1])

    #policy check for password
    PasswordArray = list(each_line[1])
    ArrayCharCounter = 0
    for EachChar in PasswordArray:
        if EachChar == PasswordPolicy_letter:
            ArrayCharCounter = ArrayCharCounter +1
    
    if ArrayCharCounter >= FromNumber and ArrayCharCounter <= ToNumber:
        correctPassCounter = correctPassCounter +1
    


print("\n", correctPassCounter, " number of passwords passed the policy-check.\n")

exit()