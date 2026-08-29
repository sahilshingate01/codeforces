a, op, b, eq, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if op == '+':
    ans = a + b
elif op == '-':
    ans = a - b
else:
    ans = a * b

if ans == c:
    print("Yes")
else:
    print(ans)