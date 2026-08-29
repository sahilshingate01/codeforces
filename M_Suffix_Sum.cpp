#include <iostream>
using namespace std;

long long f(long long n,long long m,long long total,int arr[]){
    if(n <= m){
        return total;
    }
    return f(n,m + 1,total + arr[m],arr);
}


int main(){
    int n,m;
    cin >> n >> m;
    int arr[n];
    for(int i = 0; i < n; i++){
        cin>>arr[i];
    }
    cout<<f(n,n - m,0,arr);
}