'''
The first line contains the length of side AB .
The second line contains the length of side BC.
M is the mid point of AC.
find angle MBC
'''

import math 
ab = int(input()) 
bc = int(input()) 
ang=(math.degrees(math.atan2(ab,bc)))
print ((str(int(round(ang))))+'°')

#  ° from character map from window search
