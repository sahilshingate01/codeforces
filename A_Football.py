n = int(input())
teams = []

for _ in range(n) :
    s = input()
    teams.append(s)

freq = {}
mx = float('-inf')
ans = []

for team in teams :
    freq[team] = freq.get(team,0) + 1
    if mx < freq[team] :
        mx = freq[team]
        ans.append(team)
    
print(ans[-1])
        
