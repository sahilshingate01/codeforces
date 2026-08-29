n,x = map(int,input().split())
arr = list(map(int,input().split()))

def f(i,total):

    if i == n:
        if total == x:
            return True
        return False

    if f(i + 1,total + arr[i]):
        return True
    if f(i + 1,total - arr[i]):
        return True

    return False

print("YES" if f(1,arr[0]) else "NO")