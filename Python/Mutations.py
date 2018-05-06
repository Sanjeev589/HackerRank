'''
Task 
Read a given string, change the character at a given index and then print the modified string.
'''
def mutate_string(string, position, character):
    li=list(string)
    li[position]=character
    
    return "".join(li)

print(mutate_string(input(),int(input()),input()))
