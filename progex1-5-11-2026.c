#include <stdio.h>
#include <math.h>
#include <locale.h>
#include <string.h>
#ifndef _WIN32
#include <stdbool.h>
#endif
#include<stdlib.h>

int main(){
    char clearstr[16];
#ifdef _WIN32 
strcpy(clearstr,"cls"); 
#else 
strcpy(clearstr,"clear");
#endif
    setlocale(LC_ALL, ".UTF8");
    float dados[7] = {-3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0}, p;
    char opcao ='0';
    int i;
    system(clearstr);
    while (true){
        printf("Opções:\n");
        printf("1)Função exponencial\n");
        printf("2)Função logarítmica\n");
        printf("3)Ambas as funções\n");
        printf("4)Sair\n");
        if (opcao == '4'){
            system(clearstr);
            break; 
        }       
        if (opcao == '1' || opcao == '3'){
            printf("\n---------------\n%s%11s\n---------------\n", "x", "f(x)");
            for (i = 0; i < 7; i++)
                printf("%6.2f %6.3f\n", dados[i], pow(2, dados[i]));
        }
        if (opcao == '2' || opcao == '3'){
            printf("\n---------------\n%s%11s\n---------------\n", "x", "g(x)");
            for (i = 0; i < 7; i++)
                printf("%6.3f %6.2f\n", pow(2, dados[i]), log(pow(2, dados[i])) / log(2));
        }
        printf("\nDigite a opção desejada: ");
        opcao = getc(stdin);
        while (getchar() != '\n');
        system(clearstr);
    }
    return 0;
}
