#include <iostream>

using namespace std;

bool voc(char ch)
{
    return ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u';
}

int main()
{
    int i=1, nr=0;
    char s[256];
    cin.getline(s,256);
    while(s[i+1]!='\0')
    {
        if(voc(s[i])==1)
            if(voc(s[i-1])==0 and s[i-1]!=' ')
               if(voc (s[i+1])==0 and s[i+1]!=' ')
                   nr++;
       i++;
    }
    cout<<nr;
    return 0;
}
