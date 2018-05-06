'''
Task 
You are given the year,
and you have to write a function to check if the year is leap or not.

Note that you have to complete the function and remaining code is given as template.

Hint:-
In the Gregorian calendar three criteria must be taken into account to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
'''

def is_leap(year):
    leap = False
    if year%4==0 :
        if(year%100==0):
            if year%400==0:
                leap=True
                
            else:
                leap=False
        else:
            leap=True
    
    return leap


year=int(input())
print(is_leap(year))
