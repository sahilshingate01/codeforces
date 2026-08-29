t = int(input())


def printsubsequences(idx,ds,n):
    
    if idx == n:
        if len(ds) == n:
            print(*ds,sep='')
        return
    
    ds.append(0)
    printsubsequences(idx + 1,ds,n)

    ds.pop()
    printsubsequences(idx + 1,ds,n)

    ds.append(1)
    printsubsequences(idx + 1,ds,n)

    ds.pop()
    printsubsequences(idx + 1,ds,n)



for _ in range(t):
    n = int(input())
    printsubsequences(0,[],n)
