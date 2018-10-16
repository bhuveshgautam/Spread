def fact(x):
    if x == 0 or x == 1:
        return 1
    return x * fact(x - 1)

test = int(input())
for n in range(0, test):
    N = int(input())
    Si = input().split()
    
    for x in range(0, len(Si)):
        Si[x] = int(Si[x])
        
    Si.sort(reverse = True)
    
    number = 1
    i = 0
    
    while(i < len(Si)):
        l = 1
        iClone = i
        for m in range(i+1, len(Si)):
            if Si[i] == Si[m]:
                l = l + 1
            else:
                i = m
                break   
        if iClone == i:
            i = len(Si)
        
        if l != 0 and l != 1:
            number = number * fact(l)/2
    
    print(number)
