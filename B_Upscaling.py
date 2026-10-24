t = int(input())

for _ in range(t):
    n = int(input())

    for i in range(n):
        temp = ''

        for j in range(n):
            if (i + j) % 2 == 0:
                temp += '##'
            else:
                temp += '..'

        print(temp)
        print(temp)