#include <stdio.h>
#include <math.h>

int main() {
    double pi,A,B,C,p1,p2,p3,p4,p5;
    pi=3.14159;
    scanf("%lf %lf %lf",&A,&B,&C);
    p1=(A*C)/2;
    p2=pow(C,2)*pi;
    p3=((A+B)*C)/2;
    p4=pow(B,2);
    p5=A*B;
    printf("TRIANGULO: %.3lf\n",p1);
    printf("CIRCULO: %.3lf\n",p2);
    printf("TRAPEZIO: %.3lf\n",p3);
    printf("QUADRADO: %.3lf\n",p4);
    printf("RETANGULO: %.3lf\n",p5);
    return 0;
}
