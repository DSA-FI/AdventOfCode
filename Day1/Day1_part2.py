
#Code for the day 1 part 1 of Advent For Code -challenge

InputNumbersList = []
copy_NumberList = []
Thirdcopy_NumberList = []
FoundNumber1 = int()
FoundNumber2 = int()
FoundNumber3 = int()

file_handler = open("input.txt", 'r')


for each_line in file_handler: #iterate through the file

    each_line = each_line.rstrip() #remove newlines
    InputNumbersList.append(each_line)


copy_NumberList = InputNumbersList #copy the list
Thirdcopy_NumberList = InputNumbersList


for Each_Number in InputNumbersList: #compare the two lists by iterating through both

    for Each_NumberCopy in copy_NumberList:

        for Each_NumberThirdcopy in Thirdcopy_NumberList:

            if int(Each_Number) + int(Each_NumberCopy) + int(Each_NumberThirdcopy) == 2020:

                FoundNumber1 = int(Each_Number) #save the numbers that matched our search
                FoundNumber2 = int(Each_NumberCopy) 
                FoundNumber3 = int(Each_NumberThirdcopy)


print("\nThe values are: ", FoundNumber1, ", ", FoundNumber2, "and: ", FoundNumber3, "And the total sum: ", FoundNumber1+FoundNumber2+FoundNumber3)
print("Multiplying them together produces the following number: ", FoundNumber1 * FoundNumber2 * FoundNumber3, "\n")
exit()
