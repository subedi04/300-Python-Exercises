#include <iostream>
using namespace std;

void Dec_to_Binary(int n){
    int binary_num[32];

    int i = 0;

    while(n>0){
        binary_num[i] = n%2;
        n = n/2;
        i++;
    }

    for(int j = i-1; j>=0; j--){
        cout<<binary_num[j];
    }
}

int main(){
    int n;
    cout<<"Enter a number : ";
    cin>>n;


    cout<<"Your number in Binary is : ";
    Dec_to_Binary(n);
    cout<<endl;

    return 0;
}
