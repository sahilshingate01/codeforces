n,k = map(int,input().split())
arr = list(map(int,input().split()))

i = 0
while i < k - 1 :
    i += arr[i]

print("YES" if i == k - 1 else "NO")