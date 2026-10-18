t = int(input())

for _ in range(t) :
    s = input()
    
    one = 0
    zero = 0
    for ch in s :
        if ch == '1' :
            one += 1
        else :
            zero += 1
    #
    if min(one,zero) % 2 != 0 :
        print("DA")
    else :
        print("NET")