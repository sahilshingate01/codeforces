t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    if x == 1:
        print(0)
        continue

    # Find prime factors of x
    primes = []
    temp = x
    d = 2
    while d * d <= temp:
        if temp % d == 0:
            primes.append(d)
            while temp % d == 0:
                temp //= d
        d += 1
    if temp > 1:
        primes.append(temp)

    # Check each prime factor
    ans = 0
    for p in primes:
        current_sum = 0
        for val in a:
            if val % p == 0:
                current_sum += val
        if current_sum > ans:
            ans = current_sum

    print(ans)