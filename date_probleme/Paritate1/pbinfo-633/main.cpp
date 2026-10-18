#include <iostream>

using namespace std;

int main()
{
    int n, i, nrp=0, nrimp=0;
    cin>>n;
    int v[n];
     for(int i=1; i<=n; i++)
        cin>>v[i];
    for(i=1; i<=n; i++)
    {
        if(v[i]%2==0)
          nrp++;
        else
          nrimp++;
    }
    if(nrp>nrimp)
        cout<<nrp-nrimp;
    else
        cout<<nrimp-nrp;
    return 0;
}
