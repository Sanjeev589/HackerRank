'''
You are given a string S . 
Your task is to print all possible combinations_with_replacement() of size K  of the string in lexicographic sorted order.
'''


from itertools import combinations_with_replacement
(s,k)=input().split(' ')

print(*[''.join(i) for i in combinations_with_replacement(sorted(s),int(k))],sep='\n')
