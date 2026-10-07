t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input()))

    memory = []
    not_printed = []

    for i in range(n) :
        if arr[i] == 1 :
            memory.append(i + 1)
        
        elif arr[i] == 2 :
            if memory :
                memory.pop()
                not_printed.append(i + 1)
    
    not_printed.extend(memory)
    not_printed.sort()

    print(len(not_printed))
    print(*not_printed)


                
