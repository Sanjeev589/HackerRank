'''
You are given a list of N lowercase English letters. For a given integer  K,
you can select any K indices (assume 1-based indexing) with a uniform probability from the list.

Find the probability that at least one of the K indices selected will contain the letter: 'a'.
'''











from itertools import combinations

n = int(input())
l = input().split()
k = int(input())

li = list(combinations(l, k))
x = filter(lambda c: 'a' in c, li)
print("{0:.3}".format(len(list(x))/len(li)))
