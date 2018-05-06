'''
Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer e at position i.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer  at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above.
Iterate through each command in order and perform the corresponding operation on your list.
'''


if __name__ == '__main__':
    N = int(input())
    li=[]
    for i in range(0,N):
        fun=input()
        fun_s=fun.split()
        if fun_s[0]=="insert":
            li.insert(int(fun_s[1]),int(fun_s[2]))
        elif fun_s[0]=="print":
            print(li)
        elif fun_s[0]=="remove":
            li.remove(int(fun_s[1]))
        elif fun_s[0]=="append":
            li.append(int(fun_s[1]))
        elif fun_s[0]=="sort":
            li.sort()
        elif fun_s[0]=="pop":
            li.pop()
        elif fun_s[0]=="reverse":
            li.reverse()
