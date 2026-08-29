a, op, b = input().split()

a = int(a)
b = int(b)

if op == "<":
    print("Right" if a < b else "Wrong")

elif op == ">":
    print("Right" if a > b else "Wrong")

else:  # op == "="
    print("Right" if a == b else "Wrong")