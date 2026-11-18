s = input()

up = 0
for i in range(len(s)) :
    if s[i].isupper() : up += 1

if up > len(s) - up : print(s.upper())
else : print(s.lower())