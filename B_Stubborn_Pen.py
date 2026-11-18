t = int(input())

for _ in range(t) :
    n = int(input())
    s = input()

    cnt = 0
    for i in range(n - 1) :
        if s[i] == s[i + 1] :
            cnt += 1

    if s[0] != 'R' : cnt += 1
    print(cnt)

        
