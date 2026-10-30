s = input()

t = {'a','e','i','o','u','y'}
ans = ''

for ch in s :
    if ch.lower() not in t :
        ans += '.'
        ans += ch.lower()
    
print(ans)