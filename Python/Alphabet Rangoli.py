'''
You are given an integer, N. Your task is to print an alphabet rangoli of size N.
(Rangoli is a form of Indian folk art based on creation of patterns.)
'''



import string
alpha = string.ascii_lowercase
def srange(N):
    return list(range(N))+list(range(N-2,-1,-1))

def print_rangoli(num):
    for i in srange(num):
        print('-'.join([alpha[num-j-1] for j in srange(i+1)]).center(4*(num-1)+1,'-'))



print_rangoli(int(input()))
