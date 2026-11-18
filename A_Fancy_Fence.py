t = int(input())

for _ in range(t) :
    a = int(input())
    
    ans = str(360 / (180 - a))
    point = ans.split('.')

    if point[1] != '0' :
        print("NO")
    else :
        print("YES")

#formula based qestion 

# 3. Convert the formula
# We have:
# \[
# a = \frac{(n-2)\times180}{n}
# \]

# Expand:
# \[
# a = \frac{180n-360}{n}
# \]

# \[
# a = 180-\frac{360}{n}
# \]

# Now rearrange:
# \[
# 180-a = \frac{360}{n}
# \]

# Therefore:
# \[
# \boxed{n = \frac{360}{180-a}}
# \]