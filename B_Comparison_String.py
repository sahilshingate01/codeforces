t = int(input())

for _ in range(t) :
    n = int(input())
    s = input()
    
    curr = 1
    best = 1

    for i in range(1,n) :
        if s[i - 1] == s[i] : curr += 1
        else : curr = 1 

        best = max(best,curr)
    
    print(best + 1)