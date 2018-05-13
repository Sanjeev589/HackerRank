'''
You are given a function f(x)=x**2 . You are also given k lists. The i list consists of N elements.

You have to pick one element from each list so that the value from the equation below is maximized: 

s=(f(x1)+......)%M

 denotes the element picked from the i list . Find the maximized value  obtained.

 denotes the modulo operator.

'''











from itertools import product

K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))
