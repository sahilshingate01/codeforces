n = int(input())
arr = list(map(int,input().split()))

one = 0
two = 0
three = 0
four = 0

for x in arr :
    if x == 1 :
        one += 1
    elif x == 2 :
        two += 1
    elif x == 3 :
        three += 1
    else :
        four += 1

ans = four 
ans += three
one = max(0, one - three)
ans += two // 2

if two % 2 != 0  :
    ans += 1
    one = max(0,one - 2)

ans += (one + 3) // 4
print(ans)



# 1 1 1 1 1 1
# 1 1 1 1 1 1
# 1 1 1 1 1 1
# 1 1 1 1 1 1
# 1 1 1 1 1 1
# 1 1 1 1 1 1