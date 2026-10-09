t = int(input())

for _ in range(t) :
    n = int(input())
    s = list(input())

    s.sort()
    for ch in s :
        print(ch,end="")
    print()