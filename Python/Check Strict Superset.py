'''
You are given a set A and n other sets. 
Your job is to find whether set A is a strict superset of each of the N sets.

Print True, if A is a strict superset of each of the N sets.
Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.
'''

a=set(map(int,input().split()))
n=int(input())
ans=True
for i in range(n):
    count=0
    
    s=set(map(int,input().split()))
    for j in s:
        if j in a:
            count+=1
    if (count<len(a) and count==len(s)):
        ans = ans and True
    else:
        ans = False
    s=set()
print(ans)
