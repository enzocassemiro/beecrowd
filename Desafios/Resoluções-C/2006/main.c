#include <stdio.h>

int main()
{
    int i,t,v[5],c=0;
    scanf("%i",&t);
    scanf("%i %i %i %i %i",&v[0],&v[1],&v[2],&v[3],&v[4]);
    for ( i = 0; i < 5; i++)
    {
        if (v[i]==t){
            c++;
        }
    }
    printf("%i\n",c);
    return 0;
}
