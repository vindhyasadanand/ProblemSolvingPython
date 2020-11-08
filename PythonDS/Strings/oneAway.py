''''
pale, ple = here by inserting a we can get same strings
pales , pale = here by removing s we can get same two strings
pable , bale = by replacing one character we can get two strings as same
pale , bake = here in single edit we cant make two strings as same

'''


def oneeditreplace(s1, s2):
    matchfound = False
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            if matchfound:
                return False
        matchfound = True
    return True

def oneeditInsert(s1, s2):
    index1 = 0
    index2 = 0
    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] != s2[index2]:
            if index1 != index2:
                return False
            index2 = index2 + 1
        else:
            index1 = index1 + 1
            index2 = index2 + 1
    return True


def oneway(s1,s2):
    s1_len = len(s1)
    s2_len = len(s2)
    if s1_len ==s2_len:
        print(oneeditreplace(s1,s2))
    elif s1_len+1 ==s2_len:
        print(oneeditInsert(s1,s2))
    elif s1_len-1 == s2_len:
        print(oneeditInsert(s1,s2))
oneway("pale","bale")
oneway("pales","pale")
oneway("pal","pale")
oneway("cake","book")
