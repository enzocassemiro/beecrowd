#include <stdio.h>

int main()
{

    int tgasto,vmedia;
    double x;
    scanf("%i",&tgasto);
    scanf("%i",&vmedia);
    x = (tgasto*vmedia)/12.0;
    printf("%.3lf\n",x);

    return 0;
}
