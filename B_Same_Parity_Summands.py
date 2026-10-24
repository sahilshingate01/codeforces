t = int(input())

for _ in range(t) :
    n ,k = map(int,input().split())
    
    val = n // k
    rem = n % k
    if n < k :
        print('NO')

    elif rem % 2 == 0 :

        print("YES")
        ans = [val] * k
        ans[0] += rem
        print(*ans)

    elif (k-rem) % 2 == 0:

        if val <= 1 :
            print("NO")
        else:
            print("YES")
            ans=[val] * k
            for i in range(rem):
                ans[i] += 1
            l = rem 
            h = k - 1

            while l < h:
                ans[l] -= 1
                ans[h] += 1
                l += 1
                h -= 1
            print(*ans)
    else:
        print("NO")
    