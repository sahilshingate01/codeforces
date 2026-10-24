t = int(input())

for _ in range(t) :
    s = input()

    ans = []
    for i in range(len(s)) :
        if s[i] != '0' :
            ans.append(s[i] + (len(s) - i - 1) * '0' )
    
    print(len(ans))
    print(*ans)
