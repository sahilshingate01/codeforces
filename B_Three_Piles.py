t = int(input())

for _ in range(t):
    a,b,c = map(int,input().split())

    v1 = abs(a - b)
    v2 = abs(a + c) - b

    print(max(v1,v2))