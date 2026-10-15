t = int(input())

while t :
    n = int(input())
    s = input()
    c = s[-1]
    
    ans = 0
    for ch in s :
        if ch == c :
            ans += 1
    print(n - ans)

    t -= 1
