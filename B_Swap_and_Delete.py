t = int(input())

for _ in range(t):
    s = input()

    one = s.count('1')
    zero = s.count('0')

    for ch in s :
        if ch == '1' :
            zero -= 1
        else :
            one -= 1
    
        if one < 0 or zero < 0 :
            break
        
    
    if one < 0 or zero < 0 :
        print(one + zero + 1)
    
    else :
        print(0)