
#Code for the day 1 part 1 of Advent For Code -challenge

InputNumbersList = []
copy_NumberList = []
FoundNumber1 = int()
FoundNumber2 = int()

file_handler = open("input.txt", 'r')


for each_line in file_handler: #iterate through the file

    each_line = each_line.rstrip() #remove newlines
    InputNumbersList.append(each_line)


copy_NumberList = InputNumbersList #copy the list


for Each_Number in InputNumbersList: #compare the two lists by iterating through both

    for Each_NumberCopy in copy_NumberList:

        if int(Each_Number) + int(Each_NumberCopy) == 2020:

            FoundNumber1 = int(Each_Number) #save the numbers that matched our search
            FoundNumber2 = int(Each_NumberCopy) 


print("\nThe values are: ", FoundNumber1, "and: ", FoundNumber2, "And the total sum: ", FoundNumber1+FoundNumber2)
print("Multiplying them together produces the following number: ", FoundNumber1 * FoundNumber2, "\n")
exit()
