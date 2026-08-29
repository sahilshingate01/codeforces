n = int(input())

while n >= 10:
    n //= 10

print("EVEN" if n % 2 == 0 else "ODD" )