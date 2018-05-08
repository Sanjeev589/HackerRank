'''
Now, let's use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College.
One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.
'''


def average(array):
    height=set(array)
    return (sum(height)/len(height))




array=map(int,input().split(" "))

print(average(array))
