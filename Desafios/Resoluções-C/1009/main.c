#include <stdio.h>

int main() {
    char funcionario[10];
    double salarioFixo,vendas,salario;
    scanf("%s",funcionario);
    fflush(stdin);
    scanf("%lf %lf",&salarioFixo,&vendas);
    salario=(salarioFixo+(vendas*0.15));
    printf("TOTAL = R$ %.2lf\n",salario);
    
    return 0;
}
