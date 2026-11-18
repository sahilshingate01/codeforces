t = int(input())

for _ in range(t) :
    n = int(input())
    s1 = input()
    s2 = input()
    
    f = True
    for i in range(n) : 
        if s1[i] == 'R' :
            if s2[i] != 'R' :
                f = False
                break
        
        if s2[i] == 'R' :
            if s1[i] != 'R' :
                f = False
                break
    
    print('YES' if f else "NO")