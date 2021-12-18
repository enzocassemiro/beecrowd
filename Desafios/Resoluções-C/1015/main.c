#include <stdio.h>
#include <math.h>

int main()
{

    float r,base1,base2,x1, y1, x2, y2;
    scanf("%f %f", &x1, &y1);
    scanf("%f %f", &x2, &y2);
    base1 = x2-x1;
    base2 = y2-y1;
    r = sqrt(pow(base1,2)+pow(base2,2));
    printf("%.4f\n",r);

    return 0;
}
