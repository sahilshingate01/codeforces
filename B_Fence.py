n,k = map(int,input().split())
arr = list(map(int,input().split()))


index = 0

total = sum(arr[:k])
ans = total

for i in range(k, n):
    total = total - arr[i-k] + arr[i]

    if total < ans:
        ans = total
        index = i - k + 1

print(index + 1)





# index = 0
# ans = float('inf')

# for i in range(n - k) :

#     t = k
#     idx = i
#     total = 0
#     while t :
#         total += arr[idx]
#         idx += 1
#         t -= 1

#     if ans > total :
#         ans = min(ans,total)
#         index = i
# print(index + 1)