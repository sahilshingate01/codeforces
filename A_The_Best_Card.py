t = int(input())

def isPrime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

for _ in range(t):
    n = int(input())

    print("YES" if isPrime(n + 1) else "NO")

