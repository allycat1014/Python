# Given a birthdate show the birthday day of the week

# first we will start with only 2020

# next we will enhance the program to go all the way up to 1950

# function that given a month returns no. of days in a month
def daysInMonth(monthInNumber, year):
    # lets handle odd months - such as Janaruy, March, May, etc
    if (monthInNumber % 2 == 1 or monthInNumber == 8):
        return 31;
    elif (monthInNumber == 2):  # lets handle febuary where we have to consider year as well
        if (isLeapYear(year)):
            return 29;
        else:
            return 28;
    else:
        return 30;


# function that given a year return no. of days in a year
def daysInYear(year):
    # if a year is leap year, no. of days in the year are 366
    if (isLeapYear(year)):
        return 366;
    else:
        return 365;


def isLeapYear(year):
    return (year % 100 == 0 and year % 400 == 0) or year % 4 == 0;


# function that given day no. returns the day in the week
def dayOfTheWeek(dayNo):
    daysOfTheWeekDict = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday"
    }
    return daysOfTheWeekDict.get(dayNo);


print("Hi There, do you want to know your day of birth?: ")
date = int(input("Enter your date of the birth: "))
month = int(input("Enter your month of the birth: "))
year = int(input("Enter your year of the birth: "))

dayOf_1st_jan_1950 = 0;  # 1st January 1950 was Sunday
totalNoOfDays = 0;
for x in range(1950, year):
    totalNoOfDays = totalNoOfDays + daysInYear(x);
for x in range(1, month):  # lets now calculate total days in the months
    totalNoOfDays = totalNoOfDays + daysInMonth(x, year);
totalNoOfDays = totalNoOfDays + date;  # finally add the no. of days;

rem = (totalNoOfDays) % 7;
dayOfBirth = (((dayOf_1st_jan_1950 - 1) + rem) % 7)
print("Are you ready to know the day of your birth?");
print("Here is the day: >> ", dayOfTheWeek(dayOfBirth));
