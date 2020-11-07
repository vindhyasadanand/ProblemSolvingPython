def isAnagram(a,b):
    count = [0 for i in range(129)]
    
    for char in a:
        index = ord(char)
        if count[index] is None:
               count[index] = 1
        else:
            count[index] +=1
    
    for char in b:
        index = ord(char)
        count[index] = count[index]-1
        if count[index]<0:
            return False
    return True
