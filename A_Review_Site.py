t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))

    one = arr.count(1)
    three = arr.count(3)

    print(one + three)