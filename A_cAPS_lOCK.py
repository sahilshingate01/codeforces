s = input()

cnt = 0 
for ch in s :
    if ch.isupper() :
        cnt += 1

if cnt == len(s) - 1: 
    if s[0].islower() :
        print(s[0].upper()+s[1:len(s)].lower())
    else :
        print(s)

elif cnt == len(s) :
    print(s.lower())
    
else :
    print(s)
