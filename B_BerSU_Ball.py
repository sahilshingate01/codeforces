n = int(input())
boy = list(map(int,input().split()))
boy.sort()

m = int(input())
girl = list(map(int,input().split()))
girl.sort()

cnt = 0
paired = {i: 0 for i in range(m + 1)}

for i in range(n) :
    for j in range(m) :
        if paired[j] == 0 and abs(boy[i] - girl[j]) < 2:
            cnt += 1
            paired[j] = 1
            break

print(cnt)