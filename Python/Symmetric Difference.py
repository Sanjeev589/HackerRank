'''
Task 
Given2 sets of integers, M and N, print their symmetric difference in ascending order.
The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
'''

n=int(input())
a=set(map(int,input().split()))
m=int(input())
b=set(map(int,input().split()))
common=a.intersection(b)
uncommon=a.union(b)
li=[]
li=[i for i in uncommon if i not in common]

li.sort()
for i in li:
    print(i)
