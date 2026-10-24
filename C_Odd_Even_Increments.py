t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))


    odd = arr[0] % 2 
    even = arr[1] % 2

    f = True

    for i in range(n) :
        if i % 2 == 0 and arr[i] % 2 != odd :
            f = False
        
        if i % 2 != 0 and arr[i] % 2 != even :
            f = False

    print("YES" if f else "NO")
