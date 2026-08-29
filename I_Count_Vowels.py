s = input()

def f(idx,count):
    if idx == len(s):
        return count
    
    if s[idx] in "aeiouAEIOU":
        count += 1
    
    return f(idx + 1,count)

print(f(0,0))
