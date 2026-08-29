#include <bits/stdc++.h>
using namespace std;

long long f(int idx,long long total,int arr[],int n){
  if(idx >= n){
    return total;
  }
  return f(idx + 1,total + arr[idx],arr,n);
  
}

int main(){
  int n;
  cin>>n;
  int arr[n];
  for(int i = 0; i < n; i++){
    cin>>arr[i];
  }
  cout<<f(0,0,arr,n);
}