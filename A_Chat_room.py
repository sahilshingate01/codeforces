s = input()

word = 'hello'
i = 0
for ch in s :

    if ch == word[i] :
        i += 1

    if i > 4 :
        break

if i > 4 :
    print("YES")
else :
    print("NO")