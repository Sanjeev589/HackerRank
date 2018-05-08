'''
There is an array of n integers. There are also 2 disjoint sets,A  and B,
each containing m integers.
You like all the integers in set A and dislike all the integers in set B .
Your initial happiness is 0 .
For each i integer in the array, if ,i in A you add 1 to your happiness.
If i in B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.'''

n,m = (int(i) for i in input().split(' '))
arr=(int(i) for i in input().split(' '))
a=set(map(int,input().split(' ')))
b=set(map(int,input().split(' ')))
happy=0
for i in arr:
    if i in a:
        happy+=1
    elif i in b:
        happy-=1
print(happy)
    
