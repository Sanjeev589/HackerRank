'''
Task
The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets.
Your task is to find the total number of students who have subscribed to at least one newspaper.

'''

eng_count=int(input())
eng_roll=set(map(int,input().split(' ')))
french_count=int(input())
french_roll=set(map(int,input().split(' ')))
roll=eng_roll.union(french_roll)
print(len(roll))
