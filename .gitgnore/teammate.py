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
        k = 1
        l = 0
        for m in range(i+2, len(Si)):
            if Si[i + 1] == Si[m]:
                l = l + 1
            else:
                break    
        
        if l != 0:    
            number = number * (l + k)
        i = i + 2
        k = k + 1
        
    print(number)    
        
