t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    if s[0] == '1':
        print(s.count('0'))
    elif '1' not in s:
        print(0)
    else:
        p = s.index('1')
        ones = 0                   
        zeros = s[p:].count('0')   
        best = zeros                

        for c in s[p:]:             
            if c == '1':
                ones += 1
            else:
                zeros -= 1
            best = min(best, ones + zeros)

        print(best)