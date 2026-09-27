t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))

    one = arr.count(1)
    zero = arr.count(0)
    print(one * (2 ** zero))