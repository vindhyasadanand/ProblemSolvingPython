 # program to check all characters in a string are unique
''''
->here first we should look at given string is ASCI or Unicode
-> ASCII represents lowercase letters (a-z), uppercase letters (A-Z), 
 digits (0-9) and symbols such as punctuation marks
 -> punctuation marks : a mark, such as a full stop, comma, or question mark,
  used in writing to separate sentences and their elements and to clarify meaning.
->ASCII uses only one byte two represent a single character
->As ASCII can represent only 128 characters
------------------------------------------------------------------------
 
  Unicode represents letters of English, Arabic, Greek etc., 
  mathematical symbols, historical scripts, and emoji covering a wide range of characters than ASCII.
   Unicode can allocate around 1 million characters,
'''
'''import sys
def Unique(strings):
    list1 = []
    for char in strings:
        if char not in list1:
            list1.append(char)
        else:
            print("Not unique")
            sys.exit()
    print("Unique")
Unique("vindhya")'''
import sys
def Unique(letter):
    count = [None for i in range(129)]
    for char in letter:
        index = ord(char)
        if count[index] is None:
            count[index] = 1
        else:
            print("None unique")
            sys.exit()
    print("unique")


Unique("0123vindhya")



