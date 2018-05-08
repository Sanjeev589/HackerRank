'''
TASK
You are given a set A and N number of other sets.
These N number of sets have to perform some specific mutation operations on set A.

Your task is to execute those operations and print the sum of elements from set A.
'''


a=int(input())
a_set=set(map(int,input().split(' ')))
methods={'intersection_update': a_set.intersection_update,
         'update': a_set.update ,
         'symmetric_difference_update': a_set.symmetric_difference_update,
         'difference_update': a_set.difference_update }
m=int(input())
for _ in range(m):
    method, n = input().split()
    b_set=set(map(int,input().split()))
    methods[method](b_set)
print(sum(a_set))
