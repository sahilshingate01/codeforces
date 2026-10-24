t = int(input())

for _ in range(t) :
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))

    
    ans = float('inf')
    even = 0

    for x in arr :
        if x % 2 == 0 :
            even += 1
        
        t = (k - (x % k)) % k
        ans = min(ans,t)

    
    if k == 4 :
        if even >= 2 :
            ans = 0
        elif even == 1 :
            ans = min(ans,1)
        
        else :
            ans = min(ans,2)
        
    print(ans)


    

    
    
    # diff = arr[0] % k
    # ans = []

    # for i in range(1,n) :
    #     diff = min(diff,arr[i] % k)
    #     ans.append(diff)
    #     if diff == 0 :
    #         break
    
    # if diff == 0 :
    #     print(diff)
    # else :
    #     print(abs(min(ans) - k ))


    # diff = arr[0] % k

    # for i in range(1,n) :
    #     diff = min(diff,arr[i] % k)

    
    # print(diff)






# dp = {}

# def f(idx,target,coins,n) :

#     if idx == n - 1 :
#         if target % coins[idx] == 0 :
#             return 
#         else :
#             return float('inf')

#     if (idx,target) in dp :
#         return dp[(idx,target)]

#     take = float('inf')
#     if coins[idx] <= target :
#         take = 1 + f(idx + 1,target - coins[idx],coins,n) 
    
#     skip = 0 + f(idx + 1,target,coins,n)

#     dp[(idx,target)] = min(take,skip)
#     return dp[(idx,taget)]



# coins = [1,2,5,10,20,50,100,500,2000]

# req_coins = 0
# coins.sort(reverse = True)
# for coin in coins :
#     while amount >= coin :
#         amount -= coin
#         req_coins += 1
