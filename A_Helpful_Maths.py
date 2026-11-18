s = input()
if len(s) == 1 :
    print(s)
else :
    arr = s.split('+')
    arr.sort()
    ans = ''
    for x in arr :
        ans += x
        ans += '+'
    print(ans[:-1])
