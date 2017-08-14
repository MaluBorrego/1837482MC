/*
20 DE FEBRERO DEL 2017

CALCULADORA
Descripción: Programa que dado dos números enteros, realiza las operaciones fundamentales: suma, resta, multiplicación y división.
	Nota. Utilizar con if anidados 
*/

#include <stdio.h>

int main()
{
	/*Declaración de variables*/
	int num1, num2, suma, resta, multiplicacion;
	float division;
	char opcion;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
	
	/*Entrada de datos*/
	printf ("\n\n\n\t\tIntroduzca dos numeros\n\t\t\t");
	scanf ("%d",&num1);
	scanf ("%d", &num2);
	printf("\n\n\n\t\tSeleccione el numero que represente la operacion que desea hacer\n\t\t1-suma\n\t\t2-resta\n\t\t3-multiplicacion\n\t\t4-division\n\n\t\t");
	scanf("%d",&opcion);
	
	/*Proceso*/
	if(opcion=1)
			suma = num1 + num2;	
			printf ("\n\t\tLa suma de los numeros es: %d", suma); /*Salida*/
			scanf ("%d",&suma);
	{
	else 
		if(opcion=2)
			resta = num1 - num2;
			printf ("\n\t\tLa resta de los numeros es: %d", resta); /*Salida*/
			scanf ("%d", &resta);
		else
			if(opcion=3)
				multiplicacion = num1 * num2;
				printf ("\n\t\tLa multiplicacion de los numeros es: %d", multiplicacion);/*Salida*/
				scanf ("%d",&multiplicacion);
			else 
				if(opcion=4, num2 != 0)
					division = (float) num1/num2;
					printf ("\n\t\tLa division de los numeros es: %.2f", division);/*Salida*/
					scanf ("%f", &division);
				else 
				printf("\n\n\t\tNo es permitida la division entre cero"); /*Salida*/
	}
	
}
/*Fin de main*/
