
t = int(input())
    
trans = str.maketrans({'p': 'q', 'q': 'p', 'w': 'w'})
    
for i in range(t):
    s = input()
    print(s[::-1].translate(trans))

