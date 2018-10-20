def isSorted(arr):
    if (len(arr) == 0 or len(arr) == 1):
        return True
    return arr[0] <= arr[1] and isSorted(arr[1:])

test = int(input())
for n in range(test):
    N = int(input())
    cards = input().split()
    cardsNew = []
    
    for x in range(0, N):
        cards[x] = int(cards[x])
        
    if (isSorted(cards)):
        print("YES")
        break
    
    i = N - 2
    while(i >= 0):
        if (isSorted(cards[0:i + 1])):
            cardsNew  = cards[i + 1:]
            cardsNew.extend(cards[0: i + 1])
            if(isSorted(cardsNew)):
                break
        cardsNew = cards
        i = i - 1
        
    if (isSorted(cardsNew)):
        print("YES")
    else:
        print("NO")
