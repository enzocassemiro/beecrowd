#include <stdio.h>

int main() {
    int funcionario,horasTrabalhadas;
    float salarioHora,salario;
    scanf("%i %i %f",&funcionario,&horasTrabalhadas,&salarioHora);
    salario=horasTrabalhadas*salarioHora;
    printf("NUMBER = %i\n",funcionario);
    printf("SALARY = U$ %.2f\n",salario);
    
    return 0;
}
