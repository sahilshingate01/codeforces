t = int(input())

for _ in range(t):
    s, target = input().split()

    freq = {}
    need = {}

    for ch in s :
        freq[ch] = freq.get(ch,0) + 1
    
    for ch in target :
        need[ch] = need.get(ch,0) + 1
    
    remove = {}

    for ch in freq :
        remove[ch] = freq[ch] - need.get(ch,0)
    
    ans = ''

    for ch in s :
        if remove[ch] > 0 :
            remove[ch] -= 1
        else : 
            ans += ch
    
    if ans == target :  print("YES")
    else : print("NO")