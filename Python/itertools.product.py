'''
You are given a two lists A and B.
Your task is to compute their cartesian product A X B.
'''
from itertools import product
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(*product(a,b))
