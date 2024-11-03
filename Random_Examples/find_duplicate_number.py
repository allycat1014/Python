
list = [1 , 2,2,3,4,4,5,6,6,7,8,8,9,10,10,11,12,12,13,14,14,15,16,16,17,18,18,19,20,20,12,13,14,15,16,17,18,19,20]

s = set([]);
for number in list: # iterate over each element in the given list
    if (number in s) :
        print("found the duplicate number ", number)
    s.add(number);

