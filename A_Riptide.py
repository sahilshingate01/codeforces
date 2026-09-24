
def solve(a,b,c):
    cnt = 0
    while True:
        if a == b or b == c or a == c:
            return cnt

        max_val = max(a,b,c)
        min_val = min(a,b,c)

        if max_val == a : a -= 1
        elif max_val == b : b -= 1
        else : c -= 1

        if min_val == a : a += 1
        elif min_val == b : b += 1
        else : c += 1

        cnt += 1


t = int(input())

for _ in range(t):
    a,b,c = map(int,input().split())

    print(solve(a,b,c))