n = int(input())

for x in range(1,1001) :
    s = str(x) 
    lucky = True

    for ch in s :
        if ch != '4' and ch != '7' :
            lucky = False
            break
    
    if lucky :
        if n % x == 0 :
            print("YES")
            break
else :
    print("NO")