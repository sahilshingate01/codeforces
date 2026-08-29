t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    count = 0
    total = 0
    found = False

    for water in s:

        if water == ".":
            count += 1
            total += 1

        else:
            count = 0
        
        if count > 2:
            found = True
    if found:
        print(2)
    else:
        print(total)
        