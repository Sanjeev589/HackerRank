'''
You are given two sets, A and B. 
Your job is to find whether set A is a subset of set B.

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.
'''

test_case=int(input())
for i in range(test_case):
    c=[]
    a_no=int(input())
    a=set(map(int,input().split()))
    b_no=int(input())
    b=set(map(int,input().split()))
    c=[1 for i in a if i in b]
    if len(c)==len(a):
        print('True')
    else:
        print('False')
