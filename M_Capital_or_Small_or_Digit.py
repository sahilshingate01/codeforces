x = input()

if '0' <= x <= '9':
    print("IS DIGIT")
else:
    print("ALPHA")
    
    if 'A' <= x <= 'Z':
        print("IS CAPITAL")
    else:
        print("IS SMALL")