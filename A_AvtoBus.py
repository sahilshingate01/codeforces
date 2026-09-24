t = int(input())

for _ in range(t):
    n = int(input())

    if n < 4 or n % 2 != 0 : 
        print(-1)
    
    else :
        max_bus = n // 4
        min_bus = ((n + 5) // 6)

        print(min_bus,max_bus)