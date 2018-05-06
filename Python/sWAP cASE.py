'''
You are given a string and your task is to swap cases. In other words,
convert all lowercase letters to uppercase letters and vice versa.'''


def swap_case(s):
    new_s=""
    for i in s:
        if i.isupper():
            new_s+=i.lower()
        else :
            new_s+=i.upper()
    return new_s

print(swap_case(input()))
