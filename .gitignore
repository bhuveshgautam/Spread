n = int(input())
for x in range(0, n):
    numPeople = int(input())
    assert(numPeople >= 2),"Number of people must be more than 1"
    
    A = input()
    AiList = A.split()
    for i in range(0,len(AiList)) :
        AiList[i] = int(AiList[i])
    day = 0
    people = 0
    while people < numPeople:
        for j in range(0, people + 2):
            if j < len(AiList):
                people = people + AiList[j]
        day = day + 1    
    print(day)
