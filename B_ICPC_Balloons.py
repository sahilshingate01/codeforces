t = int(input())
arr = [2] * 26

for _ in range(t) :
    n = int(input())
    s = input()

    ballons = 0
    seen = set()
    
    for ch in s :
        if ch in seen :
            ballons += 1
        else :
            ballons += 2
            seen.add(ch)
        
    print(ballons)