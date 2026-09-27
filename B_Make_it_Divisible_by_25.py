t = int(input())

def f(s, x):
    j = len(s) - 1
    cost = 0

    while j >= 0 and s[j] != x[1]:
        j -= 1
        cost += 1

    j -= 1

    while j >= 0 and s[j] != x[0]:
        j -= 1
        cost += 1

    return cost


for _ in range(t):
    s = input()

    cost = min(
        f(s, '00'),
        f(s, '25'),
        f(s, '50'),
        f(s, '75')
    )

    print(cost)