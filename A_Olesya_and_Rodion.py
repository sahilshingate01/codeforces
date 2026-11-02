n,t = map(int,input().split())

# numbers = [1,2,3,4,5,6,7,8,9]
# ans = ''

# if t == 2 :
#     for i in range(n - 1) :
#         ans += str(numbers[i])
#     ans += '2'

# elif t == 3 :
#     for i in range(n) :
#         ans += str(numbers[2])

# elif t == 4 :
#     for i in range(n) :
#         ans += str(numbers[3])

# elif t == 5 :
#     for i in range(n - 1) :
#         ans += str(numbers[0])
#     ans += '0'

# elif t == 6 :
#     for i in range(n - 2) :
#         ans += str(numbers[1])
#     ans += '12'


# # elif t == 7 :

# # elif t == 3 :

# # elif t == 9 :

# # elif t == 10 :

# print(int(ans))

ans = ''

if n == 1 and t == 10 :
     ans += '-1'

elif t == 10 :
    for i in range(n - 1) :
        ans += '1'
    ans += '0'

else :
    for i in range(n) :
        ans += str(t)
print(int(ans))