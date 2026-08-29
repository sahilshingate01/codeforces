s = input()

a, b = s.split('.')

if int(b) == 0:
    print("int", a)
else:
    print("float", a, "0." + b)