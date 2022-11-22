#include<iostream>
#include<string.h>
using namespace std;
int main()
{
int t;
cin>>t;
while(t){
    string s;
    int n;
    cin>>n;
    cin>>s;
    int max=0;
    for (int i=0;i<n;i++){
        if(int(s[i])-97+1>max){
            max=int(s[i])-97+1;
        }
    }
    cout<<max<<endl;
    t--;
}
}