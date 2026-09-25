#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin >> t;

    while(t--){
        int n;
        cin >> n;
        vector<int> arr(n);
        for(int i = 0; i < n; i++) cin >> arr[i];

        unordered_map<int,int> freq;
        int mx = 0;
        int op = 0;

        for(int x : arr){
            freq[x] = freq[x] + 1;

            if(freq[x] > mx){
                mx = freq[x];
            }
        }

        while(mx < n){
            int take = min(mx, n - mx);
            mx += take;

            op += 1 + take;
        }

        cout << op << "\n";
    }

    return 0;
}