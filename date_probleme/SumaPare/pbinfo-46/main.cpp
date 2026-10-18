#include <iostream>

using namespace std;

int main()
{
    int n, i, S=0;
    cin>>n;
    for(i=2; i<=2*n; i=i+2)
           S=S+i;
    cout<<"Suma este"<<" "<<S;
    return 0;
}
