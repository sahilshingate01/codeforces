n = int(input())
arr = list(map(int,input().split()))
arr.sort()

cnt = 0
for i in range(1,n,2) : cnt += arr[i] - arr[i - 1]

print(cnt)