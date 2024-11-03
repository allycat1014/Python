list = [57,14,2,34,134,431,43,43,113,43,13,468,65]

smallest_number = 0;
largest_number = 0;
for number in list :
    if (smallest_number == 0) :
        smallest_number = number;
        largest_number = number;
    if (number < smallest_number) :
        smallest_number = number;
    if (number > largest_number) :
        largest_number = number

print ("largest_number :", largest_number);
print ("smallest_number: ", smallest_number);
