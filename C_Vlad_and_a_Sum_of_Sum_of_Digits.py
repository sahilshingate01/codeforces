t = int(input())

digit_sum = [0] * 200001
prefix_sum = [0] * 200001

for i in range(1, 200001):
    digit_sum[i] = digit_sum[i // 10] + i % 10
    prefix_sum[i] = prefix_sum[i - 1] + digit_sum[i]

for _ in range(t):
    n = int(input())
    print(prefix_sum[n])




