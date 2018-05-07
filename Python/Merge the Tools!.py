'''
We can split S into N/K subsegments where each subsegment, Ti ,
consists of a contiguous block of K characters in S . Then, use each Ti to create string Ui such that:

The characters in Ui are a subsequence of the characters in Ti.
Any repeat occurrence of a character is removed from the string such that each character in Ui occurs exactly once.
In other words, if the character at some index j in Ti occurs at a previous index <j in Ti,
then do not include the character in string Ui.
Given S and K , print N/K lines where each line i denotes string Ui.
'''


def merge_the_tools(string,k):
    li=[]
    nw=""
    
    for i in range(0,len(string),k):
        li.append(string[i:(i+k)])
    for word in li:
        for ch in word:
            if ch not in nw:
                nw+=ch
        print(nw)
        nw=""
        








merge_the_tools(input(),int(input()))
