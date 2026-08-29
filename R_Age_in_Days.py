n = int(input())

y = n // 365
m = (n - (y * 365)) // 30

print(y,"years")
print(m % 30,"months")
print(n - (y * 365) - (m * 30),"days")