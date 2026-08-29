n,m = map(int,input().split())
arr = []
maxval = -10 ** 18

for i in range(n):
    arr.append(list(map(int,input().split())))

def f(i,j):

    if i > n - 1 or j > m - 1:
        return -10 ** 18
    
    if i == n - 1 and j == m - 1:
        return arr[i][j]
    
    right = f(i,j + 1)
    down = f(i + 1,j)

    return arr[i][j] + max(down,right)

print(f(0,0))
    
