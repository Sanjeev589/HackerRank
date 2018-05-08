'''
Task
You have a non-empty set s,
and you have to execute N commands given in N lines.

The commands will be pop, remove and discard.

'''


n = int(input())
s = set(map(int, input().split())) 
m = int(input())
methods = {
    'pop' : s.pop,
    'remove' : s.remove,
    'discard' : s.discard
}
for _ in range(m):
    method, *args = input().split()
    methods[method](*map(int,args))
print(sum(s))
