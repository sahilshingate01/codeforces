#include<bits/stdc++.h>
using namespace std;

long long dp[31][31];

long long ncr(int n, int r){
    if(r > n) return 0;
    if(r == 0 || r == n) return 1;
    if(dp[n][r] != -1) return dp[n][r];
    return dp[n][r] = ncr(n-1, r-1) + ncr(n-1, r);
}

int main(){
    memset(dp, -1, sizeof(dp));
    int n, r;
    cin >> n >> r;
    cout << ncr(n, r);
}