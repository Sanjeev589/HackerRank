'''
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
For example, alison heck should be capitalised correctly as Alison Heck.

'''



def capitalize(string):
    return ' '.join(i.capitalize() for i in string.split(' '))




print(capitalize((input())))
