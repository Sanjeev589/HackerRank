'''
Given the names and grades for each student in a Physics class of N students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

'''


if __name__ == '__main__':
    
    n=int(input())
    li=[[input(),float(input())] for _ in range(n)]
    li.sort(key=lambda x: (x[1],x[0]))
    score_set=set([li[x][1] for x in range(n)])
    score_set=sorted(list(score_set))
    li=[x[0] for x in li if x[1]==score_set[1]]
    for name in li:
        print(name)
