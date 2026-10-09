n = int(input())
a = list(map(int, input().split()))
b = sorted(a)

if a == b :
    print('yes')
    print(1,1)

else :
    l = 0
    r = 0

    for i in range(n) :
        if a[i] != b[i] :
            l = i
            break
    
    for j in range(n - 1,-1,-1) :
        if a[j] != b[j] :
            r = j
            break
    
    a[l:r + 1] = a[l: r + 1][::-1]

    if a == b :
        print("yes")
        print(l + 1,r + 1)
    else :
        print('no')