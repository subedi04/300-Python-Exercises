#include <iostream>
using namespace std;

void triangle_abc(char v[]){

    int len_v = sizeof(v)/sizeof(v[0]);

    for (int i=0; i<len_v; i++)
    {
        for (int j=0; j<=i; j++ )
        {
            //char ch = char(num);
            //cout << " " << ch;
            cout<<" "<<v[j];
            //num = num + 1;
        }
        cout << endl;
    }
}
 
void contalpha(int n)
{
    int num = 65; // ASCII value 

    for (int i=0; i<n; i++)
    {
        for (int j=0; j<=i; j++ )
        {
            char ch = char(num);
            cout << " " << ch;
            num = num + 1;
        }
        cout << endl;
    }
}
  
int main()
{
    cout << "\n";
    //int n = 7;
    //contalpha(n);
    char v[] = {'A','B','C','D','E','F','G','H','I','J','K','L','M',
                    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};

    triangle_abc(v);
    return 0;
}