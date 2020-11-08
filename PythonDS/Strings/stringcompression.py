''''
 input = aabcccccaaa
 comressed string = a2b1c5a3

 '''
def compressedString(originalstr):
    compressed = ''
    count = 0
    for i in range(len(originalstr)):
        count +=1
        if i+1>=len(originalstr) or originalstr[i]!=originalstr[i+1]  :
            compressed += originalstr[i]
            compressed +=str(count)
            count=0
    if len(compressed)<len(originalstr):
        return compressed
    else:
        return originalstr
print(compressedString("aabccccaaa"))
