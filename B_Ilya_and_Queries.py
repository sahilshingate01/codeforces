s = input()
q = int(input())


prefix = [0] * len(s)

for i in range(len(s) - 1) :
    if s[i] == s[i + 1] :
        prefix[i + 1] = prefix[i] + 1
    else :
        prefix[i + 1] = prefix[i]

# if s[-2] == s[-1] : prefix[-1] = prefix[-2] + 1
    
    

for _ in range(q) :
    l,r = map(int,input().split())
    print(prefix[r - 1] - prefix[l - 1])

# print(prefix)
