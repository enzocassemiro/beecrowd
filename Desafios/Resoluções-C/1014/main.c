#include <stdio.h>
 
int main() {
 
    int distancia;
    float combgasto,kmplitro;
    scanf("%i %f",&distancia,&combgasto);
    kmplitro = distancia/combgasto;
    printf("%.3f km/l\n",kmplitro);
 
    return 0;
}
