# t = int(input())

# for _ in range(t) :
#     n = int(input())
#     s = input()

#     freq = {}
#     cnt = 0
#     index = 0

#     for i in range(n) :
#         freq[s[i]] = freq.get(s[i],0) + 1

#         if freq[s[i]] == 2 :
#             index = i
#             break
#         else :
#             cnt += 1

#     if index != 0 :
#         nfreq = set()
#         for i in range(index,len(s)):
#             nfreq.add(s[i])

#         cnt += len(nfreq)
#     print(cnt)

# t = int(input())

# for _ in range(t):
#     n = int(input())
#     s = input()

#     left = set()
#     freq = {}

#     for ch in s:
#         freq[ch] = freq.get(ch, 0) + 1

#     ans = 0

#     for ch in s:
#         left.add(ch)
#         freq[ch] -= 1

#         if freq[ch] == 0:
#             del freq[ch]

#         cur = len(left) + len(freq)
#         ans = max(ans, cur)

#     print(ans)


t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    left = set()
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    ans = 0

    for ch in s :
        left.add(ch)
        freq[ch] -= 1

        if freq[ch] == 0 :
            del freq[ch]
        
        cur = len(left) + len(freq)
        ans = max(ans,cur)
    
    print(ans)
