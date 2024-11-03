# Given my birthdate show me my lucky no

# first we will start your birth month

# next we will move on to your birth-date

# last we will end with your year of birth

print("Hi There do you want to know your lucky number")
month = int(input("Enter your month of the birth: "))
date = int(input("Enter your date of the birth: "))
year = int(input("Enter your year of the birth: "))



def numToSingleDigit(num):
    if (num < 10):
            return num;
    result = 0;
    while num >= 10:
     res = int(num / 10);  # division
     rem = num % 10;  # reminder
     result = rem + res;
     if (result > 10) :
         num = result;
     else:
         return result;
    return result;

luckyNum = numToSingleDigit(date) + numToSingleDigit(month) + numToSingleDigit(year);

if (luckyNum > 9) :
    luckyNum = numToSingleDigit(luckyNum);

print ("Here is your Lucky Number: ", luckyNum);

# print("8: > " , numToSingleDigit(8))
#
# print("12: > " , numToSingleDigit(12))
#
# print("29: > " , numToSingleDigit(29))
#
# print("1980: > " , numToSingleDigit(1980))
#
# print("234567: > " , numToSingleDigit(234567))

# if (month > 9):
#  if(month == 10):
#      month = 1;
#  elif(month == 11):
#      month = 2;
#  elif( month == 12):
#       month = 3;
#
# if (date > 9):
