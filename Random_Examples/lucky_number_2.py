# Given my birthdate show my lucky noretu

# First we will start with your birth month

# Next we will move on to your birth-date

#last we will end with your birth year

print("Hi there do you want to know your lucky number")
month=int(input("Enter your month of birth"))
date=int(input("Enter your date of birth"))
year=int(input("Enter your year of birth"))



def numToSingleDigit(num):
    if (num < 10):
        return num;
    result = 0;

    while num >= 10:
        res = int (num / 10);
        rem = num % 10
        result = rem + res;
        if (result > 10):
            num = result;
        else:
            return result;
    return result;

luckynum = numToSingleDigit(date) + numToSingleDigit(month) + numToSingleDigit(year);

if(luckynum > 9):
    luckyNum = numToSingleDigit(luckynum);

print("Here is your lucky number ", luckyNum);
