#include <iostream>
#include <vector>

using namespace std;

bool pali(vector<int>& arr,int i,int j){
    if(i >= j){
        return true;
    }

    if(arr[i] != arr[j]){
        return false;
    }

    return pali(arr,i + 1,j - 1);
}


int main(){
    int n;
    cin>>n;
    vector<int> arr(n);
    
    for(int i = 0;i < n;i++){
        cin>>arr[i];
    }

    if(pali(arr,0,n - 1)){
        cout<<"YES";
    }else{
        cout<<"NO";
    }
    return 0;
}