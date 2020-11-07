''''
Algorithm
1.Remove All non letter characters
2.if string is having even length then all characters must have even count
3.if string is having odd length then all characters must have even count and exactly one character with odd count
In simple words a string can have no more than one character that is odd

'''
import sys


def getcount(count, char):
   count.setdefault(char,0)
   count[char] = count[char]+1

def palindromePermutations(word):

    newstr = ''
    count = {}
   #to extract only characters from string
    for char in word:
        if ord(char)>=65 and ord(char)<=90:
            newstr +=char
            getcount(count,char)

        elif ord(char)>=97 and ord(char)<=122:
            newstr +=char
            getcount(count, char)
    length = len(newstr)
    print('lenght',length)
    if length%2==0:
        for val in count.values():
            if val%2!=0:
                print("Not palindromic Permutations")
                sys.exit()
        print("Palindromic permutations")
        sys.exit()
    else:
        oddcount = 0
        for val in count.values():
            if val%2!=0:
                 oddcount +=1
        if oddcount>1:
             print("Not palindromic Permutations")
        else:
            print("Palindromic permutations")




palindromePermutations("amma")




