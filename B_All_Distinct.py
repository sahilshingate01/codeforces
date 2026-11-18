t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))

    dictinct = len(set(arr))
    
    if dictinct % 2 != n % 2 :
        dictinct -= 1
    print(dictinct)

    