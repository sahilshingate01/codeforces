n = int(input())

while True :
    add = 0
    t = n
    while n :
        add += n % 10
        n //= 10
    if add % 4 == 0:
        print(t)
        break
    
    n = t + 1
