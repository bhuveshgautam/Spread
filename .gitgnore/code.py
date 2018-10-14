n = int(input())
for x in range(0, n):
    numPeople = int(input())
    assert(numPeople >= 2)
    
    A = input()
    AiList = A.split()
    for i in range(0,len(AiList)) :
        AiList[i] = int(AiList[i])
    day = 0
    people = 1
    while(people < numPeople):
        for j in range(people):
            if(j < len(AiList)):
                people = people + AiList[j]
        
        day = day + 1    
    print(day)
