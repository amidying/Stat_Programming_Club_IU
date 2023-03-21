#include"bits/stdc++.h" 
using namespace std;

int Max(int a,int b){
    if(a>b)
        return a;
    return b;
}

int main(){
    int a,b;
    cout<<"Enter a and b: "<<endl;
    cin>>a>>b;
    cout<<Max(a,b)<<endl;
    return 0;
}