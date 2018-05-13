'''
You are given a string S . 
Your task is to print all possible combinations of size K  of the string in lexicographic sorted order.
'''


from itertools import combinations
(s,k)=input().split(' ')
for j in range(1,int(k)+1):
    print(*[''.join(i) for i in combinations(sorted(s),j)],sep='\n')
