t = int(input())

for _ in range(t):
    s = input()

    a = int(s[0]) + int(s[1]) + int(s[2])
    b = int(s[3]) + int(s[4]) + int(s[5])

    if a == b : print("YES") 
    else : print("NO")