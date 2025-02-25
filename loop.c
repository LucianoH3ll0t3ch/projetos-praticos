#include <stdio.h>


int main(){
	char operacao;
	double num1, num2;
	
	printf("Escolha a operacao que deseja usar(+/-/*/\):\n" );
	scanf("%c", &operacao);
	//printf("%c", operacao);
	printf("Informe o primeiro numero : \n");
	scanf("%lf", &num1);
	printf("Informe o segundo numero: \n");
	scanf("%lf", &num2);
	
	double resultado;
	switch(operacao){
		case '+':
			resultado = num1 + num2;
			printf("%.1lf", resultado);
			break;
		case '-':
			resultado = num1 - num2;
			printf("%.1lf", resultado);
			break;
		case '*':
			resultado = num1 * num2;
			printf("%.1lf", resultado);
			break;
		case '/':
			resultado = num1 / num2;
			printf("%.1lf", resultado);
			break;
		default :
			printf("operacao invalida");
			
	}
	
	
	
	
	
	return 0;
}
