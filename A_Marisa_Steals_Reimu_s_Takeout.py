t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    ops = 0

    zero = 0
    one = 0
    two = 0
    
    for x in arr:
        if x == 0:
            zero += 1
        elif x == 1:
            one += 1
        else:
            two += 1
     
    pair = min(one,two)
    one -= pair
    two -= pair

    print(pair + (one // 3) + (two // 3) + zero)