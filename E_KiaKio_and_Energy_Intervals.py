# t = int(input())

# for _ in range(t) :
#     n = int(input())
#     arr = list(map(int,input().split()))

#     ans = 0

#     for l in range(n) :
#         xor = 0
#         mx = 0

#         for r in range(l, n) :
#             if l > r : break

#             xor ^= arr[r]
#             mx = max(mx,arr[r])

#             if l < r : ans = max(ans,xor & mx)
        
#     print(ans)
# this is not optimse solution 