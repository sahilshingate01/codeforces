s = input()
num1 = ''
num2 = ''
found = False
op = ''

for ch in s:

    if ch in "-+*/":
        op = ch
        found = True
        continue

    if not found:
        num1 += ch
    else:
        num2 += ch

n1 = int(num1)
n2 = int(num2)

if op == '+':
    print(n1 + n2)
elif op == '-':
    print(n1 - n2)
elif op == '*':
    print(n1 * n2)
elif op == '/':
    print(n1 // n2)

