t = int(input())

for _ in range(t) :
    n = int(input())
    s = input()
    target = sorted("Timur")

    if n == 5 and sorted(s) == target:
        print("YES")
    else:
        print("NO")