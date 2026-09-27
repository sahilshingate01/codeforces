t = int(input())

for _ in range(t) :
    s = input()

    open1 = 0
    open2 = 0
    move = 0

    for ch in s :
        if ch == '(' : open1 += 1 
        elif ch == "[" : open2 += 1
    
        elif ch == ')' :
            if open1 > 0 :
                move += 1
                open1 -= 1

        elif ch == ']' :
            if open2 > 0 :
                move += 1
                open2 -= 1

    print(move)


# stack implementation
# t = int(input())

# for _ in range(t):
#     s = input()

#     stack = []
#     ans = 0

#     for ch in s:
#         if ch == '(' or ch == '[':
#             stack.append(ch)

#         else:
#             if stack:
#                 if (ch == ')' and stack[-1] == '(') or \
#                    (ch == ']' and stack[-1] == '['):
#                     stack.pop()
#                     ans += 1

#     print(ans)