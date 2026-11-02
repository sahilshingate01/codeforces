n = int(input())

if n == 0 : # this was edge case found in test case 
    print(1)
elif n % 4 == 0 :
    print(6)
elif n % 4 == 1 :
    print(8)
elif n % 4 == 2 :
    print(4)
else :
    print(2)
