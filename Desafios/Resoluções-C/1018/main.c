#include <stdio.h>

int main()
{
    int i,vRecebido,qtdNotas,notas[7]={100,50,20,10,5,2,1};
    scanf("%i",&vRecebido);
    printf("%i\n",vRecebido);

    for ( i = 0; i < 7; i++)
    {
        qtdNotas = vRecebido/notas[i];
        vRecebido= vRecebido-(qtdNotas*notas[i]);
        printf("%i nota(s) de R$ %i,00\n",qtdNotas,notas[i]);
    }
    return 0;
}
