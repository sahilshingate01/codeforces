t = int(input())

for _ in range(t):
    n, c = input().split()
    n = int(n)
    s = input()

    i = 0
    j = n - 1
    coin = 0

    while i < j :
        if s[i] != s[j] :
            if s[i] != c : coin += 1
            if s[j] != c : coin += 1

        i += 1
        j -= 1

    print(coin)