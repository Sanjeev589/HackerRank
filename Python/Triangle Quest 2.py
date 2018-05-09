'''
You are given a positive integer N. 
Your task is to print a palindromic triangle of size N.
'''

for i in range(1,int(input())+1):
    print(((10**i - 1)//9)**2)
