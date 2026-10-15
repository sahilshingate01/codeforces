
t = int(input())

for _ in range(t):
    s = input().strip()

    long = False
    short = False

    for i in range(1,len(s) - 1) :
        if s[i - 1] == s[i] == s[i + 1] :
            long = True
        
        elif s[i - 1] == s[i + 1] :
            short = True
        
    print(1 + int(long) + int(short))