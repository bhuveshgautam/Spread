def isPrime(x):
    if x == 2 or x == 3:
        return True
    if x < 2:
        return False
    counter = 0
    for i in range(2,x):
        if x % i == 0:
            counter = 1
            break
    if counter == 1:
        return False 
    else:
        return True
    
def isSemiPrime(x):
    counter = 0
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            j = int(x / i)
            if isPrime(i) and isPrime(j) and i!=j:
                counter = 1
                break
    if counter == 1:
        return True
    else:
        return False
    
def main():
    counter = 0
    test = int(input())
    for x in range(0, test):
        n = int(input())
        for d1 in range(6, int(n / 2) + 1):
            d2 = n - d1
            if isSemiPrime(d1) and isSemiPrime(d2):
                counter = 1
                break
        if counter == 1:
            print("YES")
        else:
            print("NO")
            
main()
