t = int(input())

while t :
    s = input()
    a = s.count('A')
    b = s.count('B')

    print("A" if a > b else 'B')

    t -= 1