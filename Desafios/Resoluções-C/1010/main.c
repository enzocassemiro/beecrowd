#include <stdio.h>
 
int main() {
 
    int cod1,cod2,num1,num2;
    float valor1,valor2,total;
    scanf("%i",&cod1);
    scanf("%i",&num1);
    scanf("%f",&valor1);
    scanf("%i",&cod1);
    scanf("%i",&num2);
    scanf("%f",&valor2);
    total=((num1*valor1)+(num2*valor2));
    printf("VALOR A PAGAR: R$ %.2f\n",total);

    return 0;
}
