T = int(input())
for i in range(T):
    S = input()
    K = int(input())
    for char in S:
        if char == " ":
           S = S.replace(" ",'%20')
    print(S)
    
    
