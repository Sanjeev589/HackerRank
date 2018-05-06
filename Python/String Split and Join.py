'''
Task 
You are given a string.
Split the string on a " " (space) delimiter and join using a - hyphen.
'''

def split_and_join(line):
    i=line.split(" ")
    new_line="-".join(i)
    return (new_line)

print(split_and_join(input()))
