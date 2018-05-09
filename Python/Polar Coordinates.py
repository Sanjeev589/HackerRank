'''
You are given a complex Z.
Your task is to convert it to polar coordinates.
'''

from cmath import phase
n=complex(input())
print("%.3f\n%.3f"%(abs(n),phase(n)))
