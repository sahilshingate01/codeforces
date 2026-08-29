A, B = map(int, input().split())

x = A / B

floor_val = A // B
ceil_val = (A + B - 1) // B
round_val = int(x + 0.5)

print(f"floor {A} / {B} = {floor_val}")
print(f"ceil {A} / {B} = {ceil_val}")
print(f"round {A} / {B} = {round_val}")