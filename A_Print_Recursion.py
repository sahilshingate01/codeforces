n = int(input())

def f(idx):
    if idx == n:
        return 
    
    print("I love Recursion")
    f(idx + 1)

f(0)
