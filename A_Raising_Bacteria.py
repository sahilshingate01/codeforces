n = int(input())
binary = ''

while n :
    binary += str(n % 2)
    n //= 2

print(binary.count('1'))