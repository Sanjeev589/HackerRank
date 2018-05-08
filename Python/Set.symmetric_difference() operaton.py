'''
Task
Students of District College have a subscription to English and French newspapers. Some students have subscribed to only the English newspaper, some have subscribed to only the French newspaper, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper.
Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.
'''

eng_count=int(input())
eng_roll=set(map(int,input().split(' ')))
french_count=int(input())
french_roll=set(map(int,input().split(' ')))
roll=eng_roll.symmetric_difference(french_roll)
print(len(roll))
