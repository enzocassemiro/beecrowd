#include <stdio.h>

int main()
{
    int i,tomadas[4],resultado=0;;
    scanf("%i %i %i %i",&tomadas[0],&tomadas[1],&tomadas[2],&tomadas[3]);
    for ( i = 0; i < 4; i++)
    {
        if (i < 3){
            resultado += tomadas[i]-1;
        }
        if (i==3){
            resultado = resultado + tomadas[i]; 
        }
    }
    printf("%i\n", resultado);
    return 0;
}
