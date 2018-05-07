'''
Given an integer,n , print the following values for each integer i from  1to n:

Decimal
Octal
Hexadecimal (capitalized)
Binary
The four values must be printed on a single line in the order specified above for each i from 1 to n .
Each value should be space-padded to match the width of the binary value of  n .'''




def print_formatted(n):
    
    width = len("{0:b}".format(n))
    
    for i in range(1,n+1):
        print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))


n=int(input())
print_formatted(n)
