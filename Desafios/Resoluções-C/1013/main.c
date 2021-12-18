#include <stdio.h>
#include <stdlib.h>
 
int main() {
 
    int a,b,c,x;
    scanf("%i %i %i",&a,&b,&c);
    x=(a+b+abs(a-b))/2;
    x=(x+c+abs(x-c))/2;
    printf("%i eh o maior\n",x);
 
    return 0;
}
