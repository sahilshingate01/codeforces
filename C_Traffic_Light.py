t = int(input())

for _ in range(t) :
    temp = input()
    n,k = temp.split()
    s = input()
    n = int(n)

    circle = s + s 
    nextGreen = -1
    ans = 0

    for i in range(2 * n -1, -1, -1 ) :
        if circle[i] == 'g' :
            nextGreen = i
        
        if i < n and circle[i] == k :
            distance = nextGreen - i
            ans = max(ans,distance)
        
    print(ans)