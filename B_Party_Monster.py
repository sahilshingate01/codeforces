t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    count = 0

    for i in range(n):
        if s[i] == '(':
            count += 1
        else:
            count -= 1
    
    print("YES" if count == 0 else "NO")
    