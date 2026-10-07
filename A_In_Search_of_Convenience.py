t = int(input())

for _ in range(t) :
    x,y,r = map(int,input().split())

    # f = False
    # ans = []
    # for x1 in range(x - r,x + r + 1) :
    #     for y1 in range(y - r,y + r + 1) :
    #         if (( x - x1 ) ** 2) + (( y - y1 ) ** 2) == (r ** 2) :
    #             ans.append(x1)
    #             ans.append(y1) 
    #             f = True
    #             break
    #     if f :
    #         break
        
    # print(*ans)
    print(x,y + r)
                