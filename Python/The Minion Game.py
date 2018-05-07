'''
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels. 
The game ends when both players have made all possible substrings.
'''

def minion_game(string):
    vowel="AEIOU"
    stuart=0
    kevin=0
    for i in range(len(string)):
        if string[i] in vowel :
            kevin+=len(string)-i
        else:
            stuart += len(string) -i
    if kevin> stuart:
        print("Kevin %d"%(kevin))
    elif stuart> kevin:
        print("Stuart %d"%(stuart))
    else:
        print("Draw")

minion_game(input())
