n, t = map(int, input().split())
s1 = input()
s2 = input()

same = 0
for i in range(n):
    if s1[i] == s2[i]:
        same += 1
diff = n - same

match = n - t               
k = max(0, match - same)    

if 2 * k > diff:
    print(-1)
else:
    keep_same = match - k   
    copy1 = k
    copy2 = k
    res = ""

    for i in range(n):
        if s1[i] == s2[i]:
            if keep_same > 0:
                res += s1[i]
                keep_same -= 1
            else:
            
                c = "a"
                while c == s1[i]:
                    c = chr(ord(c) + 1)
                res += c
        else:
            if copy1 > 0:
                res += s1[i]
                copy1 -= 1
            elif copy2 > 0:
                res += s2[i]
                copy2 -= 1
            else:
                c = "a"
                while c == s1[i] or c == s2[i]:
                    c = chr(ord(c) + 1)
                res += c

    print(res)