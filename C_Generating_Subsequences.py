s = input()
ans = []

def generate_subsequence(idx,cur):

    for i in range(idx,len(s)):
        ans.append(cur + s[i])
        generate_subsequence(i + 1,cur + s[i] )

generate_subsequence(0,"")

ans.sort()
for i in range(len(ans)):
    print(ans[i],sep='')