t = int(input())

for _ in range(t) :
    s = input()
    f = False

    for i in range(1,len(s)) :
        if s[i - 1] == s[i] :
            f = True
            break
    
    if f : print(1)
    else : print(len(s))